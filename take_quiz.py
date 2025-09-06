# pages/take_quiz.py
import streamlit as st
from database.db import log_quiz, create_quiz_table
from datetime import datetime

st.title("📝 Take a Quiz")

create_quiz_table()

question = "What is the capital of France?"
answer = "Paris"
options = ["London", "Paris", "Rome", "Berlin"]

selected = st.radio(question, options)

if st.button("Submit"):
    score = 1 if selected == answer else 0
    log_quiz(st.session_state["username"], question, selected, score, datetime.now().strftime("%Y-%m-%d"))
    st.success(f"Your Score: {score}/1")
