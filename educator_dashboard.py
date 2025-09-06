# pages/educator_dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px
from database.db import get_all_quiz_results

st.title("👨‍🏫 Educator Dashboard")

data = get_all_quiz_results()

if data:
    df = pd.DataFrame(data, columns=["Username", "Question", "Answer", "Score", "Date"])
    st.dataframe(df)

    avg_scores = df.groupby("Username")["Score"].mean().reset_index()
    fig = px.bar(avg_scores, x="Username", y="Score", title="Average Score per Student")
    st.plotly_chart(fig)
else:
    st.info("No student quiz data available yet.")
 