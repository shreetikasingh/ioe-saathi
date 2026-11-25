# app.py - IOE Saathi: a friendly, good-looking chat interface (Streamlit)

import re
import streamlit as st
from rag import retrieve, build_prompt, generate, collection

# ---------- Page setup ----------
st.set_page_config(
    page_title="IOE Saathi · DSP Exam Buddy",
    page_icon="📚",
    layout="centered",
)

# ---------- Custom styling ----------
st.markdown(
    """
<style>
#MainMenu, footer {visibility: hidden;}
.block-container {padding-top: 2rem; max-width: 820px;}

/* Hero banner in Nepal's flag colours: crimson to blue */
.hero {
  background: linear-gradient(135deg, #DC143C 0%, #7a1fa2 55%, #003893 100%);
  border-radius: 20px; padding: 28px 30px; color: white; margin-bottom: 18px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.30);
}
.hero h1 {margin: 0; font-size: 2.3rem; color: white;}
.hero p {margin: 6px 0 0 0; opacity: 0.92; font-size: 1.02rem;}
.hero .tag {
  display: inline-block; background: rgba(255,255,255,0.18); padding: 3px 12px;
  border-radius: 999px; font-size: 0.75rem; margin-bottom: 10px; letter-spacing: 1px;
}

/* Stat cards */
.stats {display: flex; gap: 12px; margin: 4px 0 22px 0;}
.stat {
  flex: 1; background: rgba(127,127,127,0.08); border: 1px solid rgba(127,127,127,0.22);
  border-radius: 14px; padding: 14px; text-align: center;
}
.stat .num {font-size: 1.6rem; font-weight: 700;}
.stat .lbl {font-size: 0.8rem; opacity: 0.7;}

/* Little coloured labels on source cards */
.badge {
  display: inline-block; padding: 2px 10px; border-radius: 999px;
  font-size: 0.75rem; font-weight: 600; margin-right: 6px;
}
.badge-subj {background: rgba(127,127,127,0.25);}
.badge-exam {background: #003893; color: white;}
.badge-q {background: #DC143C; color: white;}

/* Suggestion buttons */
div.stButton > button {
  width: 100%; border-radius: 12px; text-align: left; padding: 0.7rem 1rem;
}
.hint {text-align: center; opacity: 0.75; margin: 6px 0 10px 0;}
</style>
""",
    unsafe_allow_html=True,
)


# ---------- Helpers ----------
@st.cache_data
def get_stats():
    """Count questions and exam papers in the database (cached, runs once)."""
    metadatas = collection.get(include=["metadatas"])["metadatas"]
    exams = {m["exam"] for m in metadatas if m["exam"] != "Unknown exam"}
    return len(metadatas), len(exams)


LABEL = re.compile(r"^\[(.+?) \| (.+?) \| Q(\d+)\]\s*")


def split_label(chunk):
    """'[DSP | 2082 Baishakh | Q3]\\n3. Define...' -> (('DSP','2082 Baishakh','3'), '3. Define...')"""
    match = LABEL.match(chunk)
    if not match:
        return None, chunk
    return match.groups(), chunk[match.end():]


def show_sources(chunks):
    """Show the retrieved past questions as neat cards inside a collapsible box."""
    with st.expander(f"📄 See the {len(chunks)} past questions behind this answer"):
        for chunk in chunks:
            label, body = split_label(chunk)
            if label:
                subject, exam, q_no = label
                st.markdown(
                    f'<span class="badge badge-subj">{subject}</span>'
                    f'<span class="badge badge-exam">{exam}</span>'
                    f'<span class="badge badge-q">Q{q_no}</span>',
                    unsafe_allow_html=True,
                )
            st.markdown(body.replace("***", "").strip())
            st.divider()


# ---------- Sidebar ----------
with st.sidebar:
    st.markdown("## 📚 IOE Saathi")
    st.caption("AI study buddy for IOE students")

    if st.button("🗑️ Start a new chat"):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.markdown("### ⚙️ How it works")
    st.markdown(
        "1. **Search**: finds the past questions closest in *meaning* to yours\n"
        "2. **Read**: Gemini reads only those questions\n"
        "3. **Answer**: explains simply and cites the exact exam & question"
    )
    st.divider()
    st.caption("Built with Python · Gemini · ChromaDB · Streamlit")
    st.caption("Made by Shreetika Singh · [GitHub](https://github.com/shreetikasingh/ioe-saathi)")

# ---------- Hero + stats ----------
st.markdown(
    """
<div class="hero">
  <span class="tag">IOE · TRIBHUVAN UNIVERSITY</span>
  <h1>📚 IOE Saathi</h1>
  <p>Your AI study buddy for <b>Digital Signal Analysis &amp; Processing</b>.
  Ask a concept, find past questions, spot exam patterns.</p>
</div>
""",
    unsafe_allow_html=True,
)

num_questions, num_papers = get_stats()
st.markdown(
    f"""
<div class="stats">
  <div class="stat"><div class="num">{num_questions}</div><div class="lbl">past questions</div></div>
  <div class="stat"><div class="num">{num_papers}</div><div class="lbl">exam papers</div></div>
  <div class="stat"><div class="num">2066–2083</div><div class="lbl">years covered</div></div>
</div>
""",
    unsafe_allow_html=True,
)

# ---------- Chat memory ----------
# Streamlit re-runs this whole file on every click, so we keep the chat in session_state
if "messages" not in st.session_state:
    st.session_state.messages = []

# A question chosen by clicking a suggestion button
pending_question = st.session_state.pop("pending", None)

# ---------- Suggestions (only on an empty chat) ----------
SUGGESTIONS = [
    "🔁 What questions have come on FFT?",
    "⚖️ Explain FIR vs IIR filters simply",
    "🔍 Has the Remez exchange algorithm been asked?",
    "🧮 What is the significance of the Z-transform?",
]

if not st.session_state.messages and not pending_question:
    st.markdown('<p class="hint">Not sure where to start? Try one of these 👇</p>', unsafe_allow_html=True)
    cols = st.columns(2)
    for i, suggestion in enumerate(SUGGESTIONS):
        if cols[i % 2].button(suggestion, key=f"suggestion_{i}"):
            st.session_state.pending = suggestion[2:].strip()  # drop the emoji
            st.rerun()

# ---------- Show the conversation so far ----------
AVATARS = {"user": "🧑‍🎓", "assistant": "📚"}

for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar=AVATARS[message["role"]]):
        st.markdown(message["content"])
        if message.get("sources"):
            show_sources(message["sources"])

# ---------- New question ----------
typed_question = st.chat_input("Ask anything about DSP… e.g. 'Which Z-transform questions have come?'")
question = typed_question or pending_question

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user", avatar=AVATARS["user"]):
        st.markdown(question)

    with st.chat_message("assistant", avatar=AVATARS["assistant"]):
        with st.spinner("Searching 18 years of past papers..."):
            chunks = retrieve(question)
            answer = generate(build_prompt(question, chunks))
        st.markdown(answer)
        show_sources(chunks)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer, "sources": chunks}
    )