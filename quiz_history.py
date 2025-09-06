# pages/take_quiz.py
import streamlit as st
from datetime import datetime
from database.db import log_quiz, create_quiz_table

create_quiz_table()

st.title("📝 Take a Simple Quiz")

question = "What is the capital of France?"
answer = "Paris"
options = ["London", "Paris", "Berlin", "Madrid"]

st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("#### ❓ Question:")
selected = st.radio(question, options)

if st.button("✅ Submit Answer"):
    score = 1 if selected == answer else 0
    log_quiz(st.session_state["username"], question, selected, score, datetime.now().strftime("%Y-%m-%d"))
    if score:
        st.success("🎉 Correct! Well done.")
    else:
        st.error(f"❌ Incorrect. The correct answer was: {answer}")

st.markdown("</div>", unsafe_allow_html=True)
