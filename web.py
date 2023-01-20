import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ''



todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my to-do app")
st.write("To increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo, key='new_todo')


st.session_state