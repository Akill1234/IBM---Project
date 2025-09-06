# auth/login.py
import streamlit as st
from database.db import create_user_table, add_user, get_user
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def login_form(role="student"):
    create_user_table()
    st.subheader(f"{role.capitalize()} Login")
    
    login_method = st.radio("Login Method", ["Manual Login", "Google (Coming Soon)"])
    if login_method == "Manual Login":
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            user = get_user(username, hash_password(password))
            if user:
                st.success(f"Welcome {username}")
                st.session_state["username"] = username
                st.session_state["role"] = role
                if role == "student":
                    st.switch_page("pages/student_dashboard.py")
                else:
                    st.switch_page("pages/educator_dashboard.py")
            else:
                st.error("Invalid credentials")
    if st.checkbox("Create New Account"):
        new_user = st.text_input("New Username")
        new_pass = st.text_input("New Password", type="password")
        if st.button("Sign Up"):
            add_user(new_user, hash_password(new_pass))
            st.success("Account created. Please login.")
