from abc import ABC, abstractmethod
from typing import Iterator


class AuthenticationError(Exception):
    pass


class BaseLLMProvider(ABC):
    @abstractmethod
    def stream_response(self, system: str, messages: list, model: str, api_key: str) -> Iterator[str]:
        pass


class AnthropicProvider(BaseLLMProvider):
    def stream_response(self, system: str, messages: list, model: str, api_key: str) -> Iterator[str]:
        import anthropic
        try:
            client = anthropic.Anthropic(api_key=api_key)
            with client.messages.stream(
                model=model,
                max_tokens=8096,
                system=system,
                messages=messages,
            ) as stream:
                for text in stream.text_stream:
                    yield text
        except anthropic.AuthenticationError as e:
            raise AuthenticationError(str(e)) from e


class OpenAIProvider(BaseLLMProvider):
    def __init__(self, base_url: str | None = None):
        self.base_url = base_url

    def stream_response(self, system: str, messages: list, model: str, api_key: str) -> Iterator[str]:
        from openai import OpenAI, AuthenticationError as OAIAuthError
        kwargs: dict = {"api_key": api_key}
        if self.base_url:
            kwargs["base_url"] = self.base_url
        try:
            client = OpenAI(**kwargs)
            openai_messages = [{"role": "system", "content": system}] + messages
            response = client.chat.completions.create(
                model=model,
                max_tokens=8096,
                messages=openai_messages,
                stream=True,
            )
            for chunk in response:
                content = chunk.choices[0].delta.content
                if content:
                    yield content
        except OAIAuthError as e:
            raise AuthenticationError(str(e)) from e


class GeminiProvider(BaseLLMProvider):
    def stream_response(self, system: str, messages: list, model: str, api_key: str) -> Iterator[str]:
        import google.generativeai as genai
        try:
            genai.configure(api_key=api_key)
            gemini_model = genai.GenerativeModel(
                model_name=model,
                system_instruction=system,
            )
            gemini_history = []
            for msg in messages[:-1]:
                role = "user" if msg["role"] == "user" else "model"
                gemini_history.append({"role": role, "parts": [msg["content"]]})
            chat = gemini_model.start_chat(history=gemini_history)
            last_content = messages[-1]["content"] if messages else ""
            response = chat.send_message(last_content, stream=True)
            for chunk in response:
                if chunk.text:
                    yield chunk.text
        except Exception as e:
            msg = str(e).lower()
            if any(k in msg for k in ("api_key", "api key", "authentication", "401", "invalid")):
                raise AuthenticationError(str(e)) from e
            raise


def get_provider(provider_id: str) -> BaseLLMProvider:
    if provider_id == "anthropic":
        return AnthropicProvider()
    if provider_id == "openai":
        return OpenAIProvider()
    if provider_id == "deepseek":
        return OpenAIProvider(base_url="https://api.deepseek.com")
    if provider_id == "gemini":
        return GeminiProvider()
    raise ValueError(f"Provedor desconhecido: {provider_id}")
