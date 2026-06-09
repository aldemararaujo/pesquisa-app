import io
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


_AZUL = colors.HexColor("#1F497D")


def docx_para_pdf(docx_bytes: bytes) -> bytes | None:
    """Gera PDF a partir do texto extraído do DOCX (via python-docx)."""
    try:
        from docx import Document
        import io as _io

        doc = Document(_io.BytesIO(docx_bytes))
        paragrafos = [p.text for p in doc.paragraphs]
        return _texto_para_pdf(paragrafos)
    except Exception:
        return None


def _texto_para_pdf(paragrafos: list[str]) -> bytes:
    buf = io.BytesIO()
    doc = SimpleDocTemplate(
        buf,
        pagesize=A4,
        leftMargin=3 * cm,
        rightMargin=2.5 * cm,
        topMargin=2.5 * cm,
        bottomMargin=2.5 * cm,
    )

    estilos = getSampleStyleSheet()
    estilo_normal = ParagraphStyle(
        "Normal_PT",
        parent=estilos["Normal"],
        fontName="Helvetica",
        fontSize=11,
        leading=16,
        spaceAfter=6,
    )
    estilo_titulo = ParagraphStyle(
        "Titulo_PT",
        parent=estilos["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=14,
        textColor=_AZUL,
        spaceAfter=12,
    )
    estilo_h2 = ParagraphStyle(
        "H2_PT",
        parent=estilos["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=12,
        textColor=_AZUL,
        spaceAfter=8,
    )

    elementos = []
    for texto in paragrafos:
        if not texto.strip():
            elementos.append(Spacer(1, 0.3 * cm))
            continue
        if texto.isupper() or len(texto) < 80 and texto == texto.title():
            elementos.append(Paragraph(texto, estilo_titulo))
        elif texto.startswith("  "):
            elementos.append(Paragraph(texto.strip(), estilo_h2))
        else:
            elementos.append(Paragraph(texto, estilo_normal))

    doc.build(elementos)
    return buf.getvalue()
