# transcribe_pdf.py - use Gemini's vision to turn scanned PDF pages into clean text

import os
import time
from pathlib import Path

import pymupdf
from dotenv import load_dotenv
from google import genai
from google.genai import errors, types

# ---------- Setup ----------
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODELS = ["gemini-3.5-flash-lite", "gemini-3.8-flash", "gemini-3.6-flash"]
INPUT_FOLDER = Path("docs")
OUTPUT_FOLDER = Path("clean_docs")

PROMPT = r"""This is a scanned page of an IOE (Institute of Engineering, Tribhuvan University, Nepal) exam paper.
Transcribe it into clean Markdown.

Rules:
- On the first line, write: Exam: <year and session, e.g. 2082 Baishakh>
- Keep question numbers, sub-parts (a, b, c) and marks like [2+3] exactly as printed.
- Write all math in LaTeX, e.g. $H(z) = \frac{1}{1 - 0.5z^{-1}}$
- If there is a figure or graph, describe it briefly like [Figure: ...]
- Skip the standard instructions (Candidates are required..., Attempt All questions, etc.).
- Do not add anything that is not on the page.
- If the page is blank or unreadable, write only: BLANK PAGE
"""


# ---------- Functions ----------
def page_to_image(page):
    """Turn one PDF page into a PNG image (kept in memory, not saved)."""
    return page.get_pixmap(dpi=150).tobytes("png")


def transcribe_image(image_bytes):
    """Send an image to Gemini and get clean text back. Tries each model in turn."""
    image = types.Part.from_bytes(data=image_bytes, mime_type="image/png")
    for model_name in MODELS:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=[image, PROMPT],
            )
            return response.text
        except errors.APIError as e:
            print(f"   {model_name} failed (error {e.code}), trying next...")
    return None  # every model failed


def transcribe_pdf(pdf_path):
    """Transcribe every page of one PDF and save each page as its own .md file."""
    # e.g. docs/past_questions/dsp/DSAP.pdf -> clean_docs/past_questions/dsp/DSAP/
    out_dir = OUTPUT_FOLDER / pdf_path.parent.relative_to(INPUT_FOLDER) / pdf_path.stem
    out_dir.mkdir(parents=True, exist_ok=True)

    doc = pymupdf.open(pdf_path)
    for page_number, page in enumerate(doc, start=1):
        out_file = out_dir / f"page_{page_number:02d}.md"

        # Skip pages we already finished (so we can safely re-run after errors)
        if out_file.exists():
            print(f"Page {page_number}: already done, skipping")
            continue

        print(f"Page {page_number}/{len(doc)}: transcribing...")
        text = transcribe_image(page_to_image(page))

        if text is None:
            print(f"Page {page_number}: all models failed. Run the script again later.")
            continue

        out_file.write_text(text, encoding="utf-8")
        time.sleep(5)  # be polite to the free tier: max ~12 requests per minute


# ---------- Run ----------
if __name__ == "__main__":
    for pdf_path in INPUT_FOLDER.rglob("*.pdf"):
        print(f"\n=== {pdf_path} ===")
        transcribe_pdf(pdf_path)
    print("\nDone! Check the clean_docs folder.")