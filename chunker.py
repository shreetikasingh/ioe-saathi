# chunker.py - split the clean exam pages into one chunk per question

import json
import re
from pathlib import Path

CLEAN_FOLDER = Path("clean_docs")
OUTPUT_FILE = Path("chunks.json")

# A line that starts a new question, e.g. "1. ...", "**2.** ...", "10. ..."
# (but NOT "0.8 <= ..." because a real question number is followed by a space)
QUESTION_START = re.compile(r"^\s*(?:\*\*)?(\d{1,2})\.(?:\*\*)?\s+")

# The first line Gemini wrote, e.g. "Exam: 2082 Baishakh"
EXAM_LINE = re.compile(r"^\s*Exam:\s*(.+)$", re.IGNORECASE)


def find_exam(lines):
    """Return the exam session (e.g. '2082 Baishakh') if the page names one."""
    for line in lines[:3]:
        match = EXAM_LINE.match(line)
        if match and re.search(r"20\d\d", match.group(1)):  # must contain a year
            return match.group(1).strip()
    return None


def split_into_questions(lines):
    """Group lines into questions. Returns a list of (question_number, text)."""
    questions = []
    current_number = None
    current_lines = []

    for line in lines:
        match = QUESTION_START.match(line)
        if match:
            # A new question starts: save the previous one first
            if current_number is not None:
                questions.append((current_number, "\n".join(current_lines).strip()))
            current_number = int(match.group(1))
            current_lines = [line]
        elif current_number is not None:
            # Continuation of the current question (sub-parts, formulas...)
            current_lines.append(line)

    if current_number is not None:
        questions.append((current_number, "\n".join(current_lines).strip()))
    return questions


def chunk_document(doc_folder):
    """Turn every page of one transcribed PDF into question chunks."""
    subject = doc_folder.parent.name  # e.g. "dsp"
    chunks = []
    last_exam = "Unknown exam"

    for page_file in sorted(doc_folder.glob("page_*.md")):
        text = page_file.read_text(encoding="utf-8")
        if "BLANK PAGE" in text[:50]:
            continue

        lines = text.splitlines()
        page_number = int(page_file.stem.split("_")[1])

        # If a page has no exam header, it's probably a continuation of the previous paper
        exam = find_exam(lines) or last_exam
        last_exam = exam

        for q_number, q_text in split_into_questions(lines):
            chunks.append({
                "id": f"{subject}-{doc_folder.name}-p{page_number:02d}-q{q_number}",
                "subject": subject,
                "source": f"{doc_folder.name}.pdf",
                "page": page_number,
                "exam": exam,
                "question_no": q_number,
                # Context at the start helps both the search and the AI's citations
                "text": f"[{subject.upper()} | {exam} | Q{q_number}]\n{q_text}",
            })
    return chunks


if __name__ == "__main__":
    all_chunks = []
    for doc_folder in sorted(CLEAN_FOLDER.rglob("*")):
        if doc_folder.is_dir() and list(doc_folder.glob("page_*.md")):
            chunks = chunk_document(doc_folder)
            print(f"{doc_folder}: {len(chunks)} questions")
            all_chunks.extend(chunks)

    OUTPUT_FILE.write_text(json.dumps(all_chunks, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nSaved {len(all_chunks)} chunks to {OUTPUT_FILE}\n")

    # Show two examples
    for chunk in all_chunks[:2]:
        print(f"--- {chunk['id']} ---")
        print(chunk["text"][:300])
        print()