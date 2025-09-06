# pages/student_dashboard.py
import streamlit as st
from model.ai_model import concept_explanation, quiz_generator

st.title("🎓 Student Dashboard")
# Cards in Columns
col1, col2 = st.columns(2)
with col1:
    st.markdown("#### 📘 Concept Explanation")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        concept = st.text_input("Enter Concept")
        if st.button("🔍 Explain Concept"):
            if concept:
                with st.spinner("Generating explanation..."):
                    result = concept_explanation(concept)
                st.text_area("AI Explanation", result, height=250)
            else:
                st.warning("Please enter a concept.")
        st.markdown("</div>", unsafe_allow_html=True)
with col2:
    st.markdown("#### 🧪 Quiz Generator")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        topic = st.text_input("Enter Quiz Topic")
        if st.button("🧠 Generate Quiz"):
            if topic:
                with st.spinner("Generating quiz..."):
                    result = quiz_generator(topic)
                st.text_area("AI Quiz", result, height=300)
            else:
                st.warning("Please enter a topic.")
        st.markdown("</div>", unsafe_allow_html=True)
