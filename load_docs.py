# load_docs.py - Day 2: read every PDF in the docs folder

from pathlib import Path
from pypdf import PdfReader


def find_pdfs(folder):
    """Return a list of every PDF inside the folder (and its subfolders)."""
    return list(Path(folder).rglob("*.pdf"))


def read_pdf(pdf_path):
    """Read one PDF and return a list of pages.
    Each page is a dictionary with its text and where it came from."""
    reader = PdfReader(pdf_path)
    pages = []
    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        pages.append({
            "source": pdf_path.name,
            "subject": pdf_path.parent.name,
            "page": page_number,
            "text": text,
        })
    return pages


def load_all_documents(folder):
    """Read every PDF in the folder and return all their pages in one list."""
    all_pages = []
    for pdf_path in find_pdfs(folder):
        print(f"Reading {pdf_path} ...")
        all_pages.extend(read_pdf(pdf_path))
    return all_pages


if __name__ == "__main__":
    pages = load_all_documents("docs")
    print(f"\nLoaded {len(pages)} pages in total.\n")

    # Show a short preview of the first page
    first = pages[0]
    print(f"--- {first['source']} | subject: {first['subject']} | page {first['page']} ---")
    print(first["text"][:500])

    # Find pages where almost no text came out (probably scanned images)
    empty_pages = [p["page"] for p in pages if len(p["text"].strip()) < 50]
    print(f"\nPages with almost no text: {empty_pages}")