import streamlit as st
from interview_engine import evaluate_answer, generate_question
from resume_parser import generate_questions_from_resume
from text_to_speech import speak
import json, os

st.set_page_config(page_title="AI Interview Bot", layout="centered")

st.title("🎤 AI Interview Bot (Offline)")

# ---- Session State ----
if "question" not in st.session_state:
    st.session_state.question = ""
if "history" not in st.session_state:
    st.session_state.history = []

# ---- Mode Selection ----
mode = st.selectbox("Choose Mode", [
    "Auto Interview",
    "Custom Question",
    "Resume Based Interview"
])

# -------------------------------
# AUTO INTERVIEW
# -------------------------------
if mode == "Auto Interview":
    if st.button("Generate Question"):
        st.session_state.question = generate_question("software development")

    if st.session_state.question:
        st.info("Question:")
        st.write(st.session_state.question)

        answer = st.text_area("Your Answer")

        if st.button("Submit Answer"):
            result = evaluate_answer(st.session_state.question, answer)
            st.success("Evaluation Complete")
            st.write(result)

            st.session_state.history.append({
                "question": st.session_state.question,
                "answer": answer,
                "feedback": result
            })

# -------------------------------
# CUSTOM QUESTION
# -------------------------------
if mode == "Custom Question":
    q = st.text_input("Enter your interview question")

    if q:
        ans = st.text_area("Your Answer")
        if st.button("Evaluate"):
            result = evaluate_answer(q, ans)
            st.write(result)

# -------------------------------
# RESUME BASED
# -------------------------------
if mode == "Resume Based Interview":
    resume = st.text_area("Paste your resume text here")

    if st.button("Generate Questions"):
        qs = generate_questions_from_resume(resume)
        st.write(qs)

# -------------------------------
# HISTORY
# -------------------------------
st.divider()
st.subheader("📜 Interview History")

for h in st.session_state.history[::-1]:
    st.markdown(f"**Q:** {h['question']}")
    st.markdown(f"**A:** {h['answer']}")
    st.markdown(f"**Feedback:** {h['feedback']}")
    st.markdown("---")
