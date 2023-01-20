import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my to-do app")
st.write("To increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new todo...")
