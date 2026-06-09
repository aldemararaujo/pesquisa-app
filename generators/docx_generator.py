import io
import re
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH


def markdown_para_docx(texto_md: str, titulo: str = "") -> bytes:
    doc = Document()

    # Margens
    for section in doc.sections:
        section.top_margin = Cm(2.5)
        section.bottom_margin = Cm(2.5)
        section.left_margin = Cm(3.0)
        section.right_margin = Cm(2.5)

    # Estilo padrão
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)
    style.paragraph_format.space_after = Pt(6)

    if titulo:
        h = doc.add_heading(titulo.replace("-", " ").title(), level=1)
        h.runs[0].font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)

    for linha in texto_md.splitlines():
        if linha.startswith("### "):
            p = doc.add_heading(linha[4:], level=3)
        elif linha.startswith("## "):
            p = doc.add_heading(linha[3:], level=2)
            p.runs[0].font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)
        elif linha.startswith("# "):
            p = doc.add_heading(linha[2:], level=1)
            p.runs[0].font.color.rgb = RGBColor(0x1F, 0x49, 0x7D)
        elif linha.startswith("- ") or linha.startswith("* "):
            doc.add_paragraph(linha[2:], style="List Bullet")
        elif re.match(r"^\d+\. ", linha):
            doc.add_paragraph(re.sub(r"^\d+\. ", "", linha), style="List Number")
        elif linha.strip() == "":
            doc.add_paragraph("")
        else:
            p = doc.add_paragraph()
            _adicionar_inline(p, linha)

    buf = io.BytesIO()
    doc.save(buf)
    return buf.getvalue()


def _adicionar_inline(paragraph, texto: str):
    # Suporte básico a **negrito** e *itálico*
    partes = re.split(r"(\*\*.*?\*\*|\*.*?\*)", texto)
    for parte in partes:
        if parte.startswith("**") and parte.endswith("**"):
            run = paragraph.add_run(parte[2:-2])
            run.bold = True
        elif parte.startswith("*") and parte.endswith("*"):
            run = paragraph.add_run(parte[1:-1])
            run.italic = True
        else:
            paragraph.add_run(parte)
