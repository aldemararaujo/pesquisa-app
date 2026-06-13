import io
from xml.sax.saxutils import escape

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


_AZUL = colors.HexColor("#1F497D")


def docx_para_pdf(docx_bytes: bytes) -> bytes | None:
    """Gera PDF a partir do DOCX, preservando títulos, listas, negrito e itálico."""
    try:
        from docx import Document
        import io as _io

        doc = Document(_io.BytesIO(docx_bytes))
        return _docx_para_pdf(doc)
    except Exception:
        return None


def _runs_para_markup(paragraph) -> str:
    """Converte os runs do parágrafo em marcação inline do ReportLab."""
    partes = []
    for run in paragraph.runs:
        trecho = escape(run.text)
        if not trecho:
            continue
        if run.bold:
            trecho = f"<b>{trecho}</b>"
        if run.italic:
            trecho = f"<i>{trecho}</i>"
        partes.append(trecho)
    if partes:
        return "".join(partes)
    return escape(paragraph.text)


def _docx_para_pdf(doc) -> bytes:
    buf = io.BytesIO()
    documento = SimpleDocTemplate(
        buf,
        pagesize=A4,
        leftMargin=3 * cm,
        rightMargin=2.5 * cm,
        topMargin=2.5 * cm,
        bottomMargin=2.5 * cm,
    )

    estilos = getSampleStyleSheet()
    normal = ParagraphStyle(
        "Normal_PT", parent=estilos["Normal"],
        fontName="Helvetica", fontSize=11, leading=16, spaceAfter=6,
    )
    h1 = ParagraphStyle(
        "H1_PT", parent=estilos["Heading1"],
        fontName="Helvetica-Bold", fontSize=16, leading=20,
        textColor=_AZUL, spaceBefore=14, spaceAfter=10,
    )
    h2 = ParagraphStyle(
        "H2_PT", parent=estilos["Heading2"],
        fontName="Helvetica-Bold", fontSize=13, leading=17,
        textColor=_AZUL, spaceBefore=12, spaceAfter=8,
    )
    h3 = ParagraphStyle(
        "H3_PT", parent=estilos["Heading3"],
        fontName="Helvetica-Bold", fontSize=12, leading=16,
        textColor=colors.HexColor("#333333"), spaceBefore=10, spaceAfter=6,
    )
    h4 = ParagraphStyle(
        "H4_PT", parent=estilos["Heading4"],
        fontName="Helvetica-BoldOblique", fontSize=11, leading=15,
        textColor=colors.HexColor("#333333"), spaceBefore=8, spaceAfter=4,
    )
    lista = ParagraphStyle(
        "Lista_PT", parent=normal,
        leftIndent=0.8 * cm, bulletIndent=0.3 * cm, spaceAfter=3,
    )

    estilos_heading = {
        "Heading 1": h1, "Heading 2": h2, "Heading 3": h3,
        "Heading 4": h4, "Title": h1,
    }

    elementos = []
    contador_lista = 0
    for par in doc.paragraphs:
        nome_estilo = par.style.name if par.style is not None else "Normal"
        markup = _runs_para_markup(par)

        if not par.text.strip():
            contador_lista = 0
            elementos.append(Spacer(1, 0.25 * cm))
            continue

        if nome_estilo in estilos_heading:
            contador_lista = 0
            elementos.append(Paragraph(markup, estilos_heading[nome_estilo]))
        elif nome_estilo.startswith("List Number"):
            contador_lista += 1
            elementos.append(
                Paragraph(markup, lista, bulletText=f"{contador_lista}.")
            )
        elif nome_estilo.startswith("List"):
            contador_lista = 0
            elementos.append(Paragraph(markup, lista, bulletText="•"))
        else:
            contador_lista = 0
            elementos.append(Paragraph(markup, normal))

    documento.build(elementos)
    return buf.getvalue()
