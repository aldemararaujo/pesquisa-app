import re
from pathlib import Path

SKILLS_DIR = Path(__file__).parent


def _strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("---", 3)
        if end != -1:
            return text[end + 3:].lstrip("\n")
    return text


def load_system_prompt(skill_id: str) -> str:
    skill_dir = SKILLS_DIR / skill_id
    skill_file = skill_dir / "SKILL.md"

    if not skill_file.exists():
        raise FileNotFoundError(f"SKILL.md não encontrado para: {skill_id}")

    prompt = _strip_frontmatter(skill_file.read_text(encoding="utf-8"))

    refs_dir = skill_dir / "references"
    if refs_dir.exists():
        ref_parts = []
        for ref_file in sorted(refs_dir.glob("*.md")):
            content = ref_file.read_text(encoding="utf-8")
            ref_parts.append(f"### Referência: {ref_file.stem}\n\n{content}")
        if ref_parts:
            prompt += "\n\n---\n\n## DOCUMENTOS DE REFERÊNCIA\n\n" + "\n\n---\n\n".join(ref_parts)

    return prompt
