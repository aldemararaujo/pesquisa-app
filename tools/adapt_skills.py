"""
Copia as skills de projeto-pesquisa-git para pesquisa-app/skills/,
removendo referências locais incompatíveis com o ambiente web.
"""

import re
import shutil
from pathlib import Path

ORIGEM = Path(r"C:\Users\aldem\Documents\Claude\Projects\Projeto de Pesquisa - Redação com IA\projeto-pesquisa-git\skills")
DESTINO = Path(__file__).parent.parent / "skills"

# Padrões a remover ou substituir em SKILL.md
REMOCOES = [
    # allowed-tools no frontmatter YAML
    (re.compile(r"^allowed-tools:.*$", re.MULTILINE), ""),
    # Caminhos Windows locais
    (re.compile(r"C:\\\\Users\\\\aldem\\\\[^\s\n\"']+", re.IGNORECASE), "[arquivo gerado pelo sistema]"),
    (re.compile(r"C:/Users/aldem/[^\s\n\"']+", re.IGNORECASE), "[arquivo gerado pelo sistema]"),
    # Instruções de invocar próxima skill via /nome
    (re.compile(r"`/[a-z][a-z0-9-]+`", re.MULTILINE), lambda m: f"`{m.group(0)[1:-1]}`"),
    # Referências a Claude Code como ferramenta
    (re.compile(r"\b(claude code|claude\s+code)\b", re.IGNORECASE), "esta ferramenta"),
    # Instruções de salvar em disco local
    (re.compile(
        r"(Salvar|Salve|Gravar|Grave|Escrever|Escreva)\s+(em|no|na|o arquivo|o documento)[^\n]*C:\\[^\n]*",
        re.IGNORECASE,
    ), "[O sistema gerará o arquivo para download]"),
]

SUBSTITUICAO_BLOCO_PORTATIL = (
    re.compile(
        r"(cole\s+(este|o)\s+bloco\s+no\s+pr[oó]ximo\s+prompt[^\n]*\n?)",
        re.IGNORECASE,
    ),
    "O sistema transferirá este contexto automaticamente para a próxima etapa.\n",
)


def adaptar_skill_md(texto: str) -> str:
    for padrao, substituicao in REMOCOES:
        if callable(substituicao):
            texto = padrao.sub(substituicao, texto)
        else:
            texto = padrao.sub(substituicao, texto)

    padrao, sub = SUBSTITUICAO_BLOCO_PORTATIL
    texto = padrao.sub(sub, texto)

    # Remove linhas em branco duplicadas geradas pelas remoções
    texto = re.sub(r"\n{3,}", "\n\n", texto)
    return texto


def main():
    if not ORIGEM.exists():
        print(f"ERRO: diretório de origem não encontrado: {ORIGEM}")
        return

    copiadas = 0
    for skill_dir in sorted(ORIGEM.iterdir()):
        if not skill_dir.is_dir():
            continue

        destino_skill = DESTINO / skill_dir.name
        destino_skill.mkdir(parents=True, exist_ok=True)

        skill_md = skill_dir / "SKILL.md"
        if skill_md.exists():
            original = skill_md.read_text(encoding="utf-8")
            adaptado = adaptar_skill_md(original)
            (destino_skill / "SKILL.md").write_text(adaptado, encoding="utf-8")
            print(f"  OK {skill_dir.name}/SKILL.md")
            copiadas += 1

        refs_origem = skill_dir / "references"
        if refs_origem.exists():
            refs_destino = destino_skill / "references"
            refs_destino.mkdir(exist_ok=True)
            for ref in refs_origem.glob("*.md"):
                shutil.copy2(ref, refs_destino / ref.name)
                print(f"    + references/{ref.name}")

    print(f"\n{copiadas} skills copiadas para {DESTINO}")


if __name__ == "__main__":
    main()
