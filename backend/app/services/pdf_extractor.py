from pathlib import Path

from pypdf import PdfReader


def extract_text_from_pdf(file_path: str | Path) -> str:
    """
    Extract text from all pages of a PDF.

    Args:
        file_path: Path to the PDF file.

    Returns:
        Combined text from all pages.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF file not found: {path}")

    reader = PdfReader(path)

    pages = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages.append(text)

    return "\n\n".join(pages)
