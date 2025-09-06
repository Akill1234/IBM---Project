import streamlit as st
from streamlit_option_menu import option_menu
from auth.login import login_form

# Page settings
st.set_page_config(page_title="Educational AI", layout="wide")

# Load global CSS (common buttons, cards, titles, etc.)
with open("static/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Top Menu
selected = option_menu(
    menu_title=None,
    options=["Student Panel", "Educator Panel", "Quiz", "Quiz History"],
    icons=["person", "person-badge", "pencil", "bar-chart"],
    orientation="horizontal"
)

# 🎨 Dynamic Styles for Each Panel
page_styles = {
    "Student Panel": {
        "bg": "linear-gradient(-45deg, #6c5ce7, #00cec9, #ffeaa7), url('https://picsum.photos/1920/1080?blur=8')",
        "navbar": "linear-gradient(90deg, #6c5ce7, #00cec9, #ffeaa7)"
    },
    "Educator Panel": {
        "bg": "linear-gradient(-45deg, #2c3e50, #27ae60, #f1c40f), url('https://picsum.photos/id/1015/1920/1080?blur=8')",
        "navbar": "linear-gradient(90deg, #27ae60, #2ecc71, #f1c40f)"
    },
    "Quiz": {
        "bg": "linear-gradient(-45deg, #e74c3c, #8e44ad, #3498db), url('https://picsum.photos/id/1025/1920/1080?blur=8')",
        "navbar": "linear-gradient(90deg, #e74c3c, #8e44ad, #3498db)"
    },
    "Quiz History": {
        "bg": "linear-gradient(-45deg, #d35400, #f39c12, #16a085), url('https://picsum.photos/id/1031/1920/1080?blur=8')",
        "navbar": "linear-gradient(90deg, #d35400, #f39c12, #16a085)"
    }
}

# Apply dynamic CSS for current page
style = f"""
<style>
.stApp {{
    background: {page_styles[selected]["bg"]};
    background-size: 400% 400%, cover;
    background-blend-mode: overlay;
    animation: gradientShift 18s ease infinite;
}}

nav[role="navigation"], .css-1d391kg {{
    background: {page_styles[selected]["navbar"]} !important;
    background-size: 300% 300%;
    animation: navbarGradient 12s ease infinite;
}}
</style>
"""
st.markdown(style, unsafe_allow_html=True)

# =============================
# Route Pages
# =============================
if selected == "Student Panel":
    st.title("🎓 Student Panel")
    login_form("student")

elif selected == "Educator Panel":
    st.title("👩‍🏫 Educator Panel")
    login_form("educator")

elif selected == "Quiz":
    st.title("📝 Quiz")
    st.write("Quiz content goes here...")

elif selected == "Quiz History":
    st.title("📊 Quiz History")
    st.write("Quiz history content goes here...")
