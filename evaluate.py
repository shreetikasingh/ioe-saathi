# evaluate.py - measure how good IOE Saathi really is, with numbers
#
# Three checks:
#   1. Retrieval: does the search find the right past questions?      (no AI calls, free)
#   2. Refusal:   does the bot refuse off-topic questions?             (AI calls)
#   3. Honesty:   are all exam citations in answers real, or invented? (AI calls)

import json
import re
import time

from rag import retrieve, build_prompt, generate

# ---------- The test set ----------
# "keywords": the search passes if ANY retrieved past question contains ANY of these words.
# Many questions are worded differently from the papers on purpose, to test search by MEANING.
TOPIC_TESTS = [
    {"question": "Has the Remez exchange algorithm been asked?", "keywords": ["remez"]},
    {"question": "How do I draw the butterfly diagram for FFT?", "keywords": ["butterfly"]},
    {"question": "Questions on region of convergence of z-transform", "keywords": ["roc", "region of convergence"]},
    {"question": "Difference between FIR and IIR filters", "keywords": ["fir", "iir"]},
    {"question": "Design Butterworth filter using bilinear transformation", "keywords": ["bilinear"]},
    {"question": "How to realize a filter using lattice structure?", "keywords": ["lattice"]},
    {"question": "Why do ripples appear near the band edge when we truncate the impulse response?", "keywords": ["gibbs"]},
    {"question": "What problems happen because registers have limited bits?", "keywords": ["quantization", "limit cycle", "word length", "rounding", "truncation"]},
    {"question": "Find circular convolution of two sequences", "keywords": ["circular convolution"]},
    {"question": "Which window functions are used in FIR design?", "keywords": ["window"]},
    {"question": "Energy signal vs power signal", "keywords": ["energy"]},
    {"question": "Converting an analog filter by sampling its impulse response", "keywords": ["impulse invariance", "impulse invariant"]},
    {"question": "Is the system causal and time invariant?", "keywords": ["causal", "time invariant", "time-invariant"]},
    {"question": "How many multiplications does FFT save compared to DFT?", "keywords": ["fft", "fast fourier"]},
        {"question": "Linear phase FIR filter questions", "keywords": ["linear phase"]},
    # Nepali questions (Romanized and Devanagari)
    {"question": "Z-transform ko ROC ke ho?", "keywords": ["roc", "region of convergence"]},
    {"question": "FFT ko butterfly diagram kasari banaune?", "keywords": ["butterfly"]},
    {"question": "FIR र IIR फिल्टरमा के फरक छ?", "keywords": ["fir", "iir"]},

]

OFF_TOPIC_TESTS = [
    "What is the capital of Australia?",
    "Who won the FIFA World Cup in 2022?",
    "Give me a recipe for chicken momo",
    "Explain normalization in DBMS",
]

REFUSAL_PHRASE = "couldn't find this in the past papers"

# Finds citations like "(2082 Baishakh, Q3)" or "2081 Bhadra Q2" in an answer
CITATION = re.compile(r"(20\d\d)\s+([A-Za-z]+),?\s*Q\.?\s*(\d{1,2})", re.IGNORECASE)
LABEL = re.compile(r"^\[.+? \| (20\d\d) ([A-Za-z]+) \| Q(\d+)\]")


def labels_of(chunks):
    """The real (year, session, question) of each retrieved chunk."""
    found = set()
    for chunk in chunks:
        m = LABEL.match(chunk)
        if m:
            found.add((m.group(1), m.group(2).lower(), m.group(3)))
    return found


def citations_in(answer):
    return {(y, s.lower(), q) for y, s, q in CITATION.findall(answer)}


if __name__ == "__main__":
    results = {"retrieval": [], "refusal": [], "honesty": []}

    # ---------- 1. Retrieval (free, no AI calls) ----------
    print("1) RETRIEVAL: does search find the right past questions?\n")
    for test in TOPIC_TESTS:
        chunks = retrieve(test["question"])
        text = " ".join(chunks).lower()
        passed = any(k in text for k in test["keywords"])
        results["retrieval"].append({"question": test["question"], "passed": passed})
        print(f"  {'PASS' if passed else 'FAIL'}  {test['question']}")
        time.sleep(1)

    # ---------- 2 + 3. Answers (uses AI calls) ----------
    print("\n2) REFUSAL: does it refuse off-topic questions?\n")
    for question in OFF_TOPIC_TESTS:
        answer = generate(build_prompt(question, retrieve(question)))
        passed = REFUSAL_PHRASE in answer.lower()
        results["refusal"].append({"question": question, "passed": passed, "answer": answer[:200]})
        print(f"  {'PASS' if passed else 'FAIL'}  {question}")
        time.sleep(2)

    print("\n3) HONESTY: are the exam citations real? (testing 8 on-topic answers)\n")
    total_cited, total_real = 0, 0
    for test in TOPIC_TESTS[:8]:
        chunks = retrieve(test["question"])
        answer = generate(build_prompt(test["question"], chunks))
        cited = citations_in(answer)
        real = cited & labels_of(chunks)
        fake = cited - real
        total_cited += len(cited)
        total_real += len(real)
        results["honesty"].append({
            "question": test["question"],
            "citations": len(cited),
            "invented": [f"{y} {s.title()} Q{q}" for y, s, q in fake],
        })
        note = f"invented: {', '.join(results['honesty'][-1]['invented'])}" if fake else "all real"
        print(f"  {len(real)}/{len(cited)} citations real ({note})  {test['question']}")
        time.sleep(2)

    # ---------- Summary ----------
    def score(items):
        return sum(i["passed"] for i in items), len(items)

    r_ok, r_all = score(results["retrieval"])
    f_ok, f_all = score(results["refusal"])
    honesty = (total_real / total_cited * 100) if total_cited else 0

    summary = {
        "retrieval_accuracy": f"{r_ok}/{r_all} ({r_ok / r_all:.0%})",
        "refusal_accuracy": f"{f_ok}/{f_all} ({f_ok / f_all:.0%})",
        "citation_honesty": f"{total_real}/{total_cited} citations real ({honesty:.0f}%)",
    }
    results["summary"] = summary

    print("\n========== SUMMARY ==========")
    for name, value in summary.items():
        print(f"  {name:20} {value}")

    with open("eval_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print("\nSaved details to eval_results.json")