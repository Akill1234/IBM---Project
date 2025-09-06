# database/db.py
import sqlite3

conn = sqlite3.connect("edu_ai.db", check_same_thread=False)
c = conn.cursor()
def create_user_table():
    c.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)")
    conn.commit()

def add_user(username, password):
    c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()

def get_user(username, password):
    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    return c.fetchone()

def create_quiz_table():
    c.execute("CREATE TABLE IF NOT EXISTS quiz(username TEXT, question TEXT, answer TEXT, score INTEGER, date TEXT)")
    conn.commit()

def log_quiz(username, question, answer, score, date):
    c.execute("INSERT INTO quiz (username, question, answer, score, date) VALUES (?, ?, ?, ?, ?)",
              (username, question, answer, score, date))
    conn.commit()

def get_user_quizzes(username):
    c.execute("SELECT * FROM quiz WHERE username=?", (username,))
    return c.fetchall()
# ✅ ADD THIS FUNCTION TO FIX THE ERROR
def get_all_quiz_results():
    c.execute("SELECT username, question, answer, score, date FROM quiz")
    return c.fetchall()
