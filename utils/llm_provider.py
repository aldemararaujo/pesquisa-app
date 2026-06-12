from abc import ABC, abstractmethod
from typing import Iterator


class AuthenticationError(Exception):
    pass


class BaseLLMProvider(ABC):
    @abstractmethod
    def stream_response(self, system: str, messages: list, model: str, api_key: str, on_tokens=None) -> Iterator[str]:
        pass


class AnthropicProvider(BaseLLMProvider):
    def stream_response(self, system: str, messages: list, model: str, api_key: str, on_tokens=None) -> Iterator[str]:
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
                if on_tokens:
                    msg = stream.get_final_message()
                    on_tokens(msg.usage.input_tokens, msg.usage.output_tokens)
        except anthropic.AuthenticationError as e:
            raise AuthenticationError(str(e)) from e


class OpenAIProvider(BaseLLMProvider):
    def __init__(self, base_url: str | None = None):
        self.base_url = base_url

    def stream_response(self, system: str, messages: list, model: str, api_key: str, on_tokens=None) -> Iterator[str]:
        from openai import OpenAI, AuthenticationError as OAIAuthError
        kwargs: dict = {"api_key": api_key}
        if self.base_url:
            kwargs["base_url"] = self.base_url
        try:
            client = OpenAI(**kwargs)
            openai_messages = [{"role": "system", "content": system}] + messages
            create_kwargs: dict = {
                "model": model,
                "max_tokens": 8096,
                "messages": openai_messages,
                "stream": True,
            }
            if on_tokens:
                create_kwargs["stream_options"] = {"include_usage": True}
            response = client.chat.completions.create(**create_kwargs)
            for chunk in response:
                if chunk.choices:
                    content = chunk.choices[0].delta.content
                    if content:
                        yield content
                elif on_tokens and chunk.usage:
                    on_tokens(chunk.usage.prompt_tokens, chunk.usage.completion_tokens)
        except OAIAuthError as e:
            raise AuthenticationError(str(e)) from e


class GeminiProvider(BaseLLMProvider):
    def stream_response(self, system: str, messages: list, model: str, api_key: str, on_tokens=None) -> Iterator[str]:
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
            if on_tokens:
                try:
                    meta = response.usage_metadata
                    on_tokens(meta.prompt_token_count, meta.candidates_token_count)
                except Exception:
                    pass
        except Exception as e:
            msg = str(e).lower()
            if any(k in msg for k in ("api_key", "api key", "authentication", "401", "invalid")):
                raise AuthenticationError(str(e)) from e
            raise


def testar_conexao(provider_id: str, model: str, api_key: str) -> None:
    """Valida a chave com uma chamada mínima ao provedor.

    Levanta AuthenticationError para chave inválida; outras exceções
    indicam problema de rede, modelo ou cota."""
    provider = get_provider(provider_id)
    for _ in provider.stream_response(
        system="Responda somente: ok",
        messages=[{"role": "user", "content": "oi"}],
        model=model,
        api_key=api_key,
    ):
        break


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
