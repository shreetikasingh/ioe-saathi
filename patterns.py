# patterns.py - the "Exam Patterns" analysis and page for IOE Saathi

import json
import re
from collections import Counter
from pathlib import Path

import pandas as pd

CHUNKS_FILE = Path("chunks.json")
LABELS_FILE = Path("topic_labels.json")

# Marks are written like [5] or [2+3] or $[6+2]$; we take the last one in the question
MARKS = re.compile(r"\[\s*(\d+(?:\s*\+\s*\d+)*)\s*\]")


def total_marks(text):
    """'... find its period. [2+3]' -> 5. Returns 0 if no marks are found."""
    found = MARKS.findall(text)
    if not found:
        return 0
    return sum(int(part) for part in found[-1].split("+"))


def exam_year(exam):
    """'2082 Baishakh' -> 2082 (or None if there's no year)."""
    match = re.search(r"20\d\d", exam)
    return int(match.group()) if match else None


def load_questions():
    """All questions + their topic, as a table (one row per question)."""
    chunks = json.loads(CHUNKS_FILE.read_text(encoding="utf-8"))
    labels = json.loads(LABELS_FILE.read_text(encoding="utf-8")) if LABELS_FILE.exists() else {}
    rows = []
    for c in chunks:
        rows.append({
            "id": c["id"],
            "subject": c["subject"],
            "exam": c["exam"],
            "year": exam_year(c["exam"]),
            "question_no": c["question_no"],
            "topic": labels.get(c["id"], "Unlabelled"),
            "marks": total_marks(c["text"]),
            "text": c["text"],
        })
    return pd.DataFrame(rows)


def topic_summary(df):
    """One row per topic: how often, how many marks, where in the paper, when last asked."""
    papers = df.loc[df["exam"] != "Unknown exam", "exam"].nunique()
    summary = []
    for topic, group in df.groupby("topic"):
        known = group[group["exam"] != "Unknown exam"]
        papers_with_topic = known["exam"].nunique()
        usual_q = Counter(group["question_no"]).most_common(1)[0][0]
        summary.append({
            "Topic": topic,
            "Questions": len(group),
            "Appears in": f"{papers_with_topic}/{papers} papers",
            "Avg marks per paper": round(known["marks"].sum() / papers, 1) if papers else 0,
            "Usually asked as": f"Q{usual_q}",
            "Last asked": known.sort_values("year")["exam"].iloc[-1] if len(known) else "-",
        })
    return pd.DataFrame(summary).sort_values("Questions", ascending=False)


# ---------- The Streamlit page ----------
def render_patterns(st, subject):
    import altair as alt

    df = load_questions()
    df = df[df["subject"] == subject]
    if (df["topic"] == "Unlabelled").all():
        st.info("Run `python topics.py` first to tag questions with topics.")
        return

    summary = topic_summary(df)
    top = summary.iloc[0]

    st.markdown(f"### 📊 What IOE asks most in {subject.upper()}")
    st.caption(
        f"Based on {len(df)} questions from {df['exam'].nunique()} exam papers. "
        "Topics were tagged by AI, so treat this as a study guide, not an official weighting."
    )

    # Headline tiles
    c1, c2, c3 = st.columns(3)
    c1.metric("Most asked topic", top["Topic"])
    c2.metric("Its marks per paper", f"~{top['Avg marks per paper']}")
    c3.metric("Usually asked as", top["Usually asked as"])

    # Bar chart: questions per topic (one colour, sorted, hover for details)
    chart = (
        alt.Chart(summary)
        .mark_bar(color="#DC143C", cornerRadiusEnd=4, height=18)
        .encode(
            x=alt.X("Questions:Q", title="Number of past questions"),
            y=alt.Y("Topic:N", sort="-x", title=None),
            tooltip=["Topic", "Questions", "Appears in", "Avg marks per paper", "Usually asked as", "Last asked"],
        )
        .properties(height=alt.Step(30))
        .configure_axis(grid=False, labelLimit=260)
        .configure_view(strokeWidth=0)
    )
    st.altair_chart(chart)

    # The same data as a table
    st.dataframe(summary, hide_index=True)

    # Drill down into one topic
    st.markdown("### 🔎 See every past question on a topic")
    chosen = st.selectbox("Pick a topic", summary["Topic"].tolist())
    questions = df[df["topic"] == chosen].sort_values("year", ascending=False)
    st.caption(f"{len(questions)} questions, newest first")
    for _, q in questions.iterrows():
        body = q["text"].split("\n", 1)[-1].replace("***", "").strip()
        with st.container(border=True):
            st.markdown(
                f'<span class="badge badge-exam">{q["exam"]}</span>'
                f'<span class="badge badge-q">Q{q["question_no"]}</span>'
                + (f'<span class="badge badge-subj">{q["marks"]} marks</span>' if q["marks"] else ""),
                unsafe_allow_html=True,
            )
            st.markdown(body)