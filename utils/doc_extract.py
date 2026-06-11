"""Extração de texto de documentos enviados pelo usuário (.pdf, .docx, .md, .txt)."""

from io import BytesIO

_MIN_CHARS_POR_PAGINA = 200


def extrair_texto(uploaded_file) -> tuple[str, str | None]:
    """Extrai o texto de um arquivo enviado via st.file_uploader.

    Retorna (texto, aviso). aviso é None quando a extração foi limpa;
    caso contrário contém uma mensagem para exibir ao usuário (ex.: PDF
    possivelmente escaneado, sem texto extraível).
    """
    nome = uploaded_file.name.lower()
    dados = uploaded_file.read()

    if nome.endswith(".pdf"):
        return _extrair_pdf(dados)

    if nome.endswith(".docx"):
        from docx import Document as DocxDocument
        doc = DocxDocument(BytesIO(dados))
        texto = "\n".join(p.text for p in doc.paragraphs if p.text.strip())
        if not texto.strip():
            return "", "O arquivo .docx não contém texto extraível."
        return texto, None

    texto = dados.decode("utf-8", errors="replace")
    if not texto.strip():
        return "", "O arquivo está vazio ou não contém texto legível."
    return texto, None


def _extrair_pdf(dados: bytes) -> tuple[str, str | None]:
    from pypdf import PdfReader

    try:
        reader = PdfReader(BytesIO(dados))
    except Exception as e:
        return "", f"Não foi possível ler o PDF: {e}"

    paginas = []
    for page in reader.pages:
        try:
            paginas.append(page.extract_text() or "")
        except Exception:
            paginas.append("")

    texto = "\n\n".join(p for p in paginas if p.strip())
    n_paginas = max(len(reader.pages), 1)

    if len(texto) < _MIN_CHARS_POR_PAGINA * n_paginas * 0.3:
        if not texto.strip():
            return "", (
                "O PDF não contém texto extraível. Provavelmente é um documento "
                "escaneado (imagem). Converta para texto (OCR) antes de enviar."
            )
        return texto, (
            "O PDF contém pouco texto extraível em relação ao número de páginas. "
            "Pode ser parcialmente escaneado: a análise pode ficar incompleta."
        )

    return texto, None
