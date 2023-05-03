import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)

st.title("ToDo - Web")
st.subheader("Organise your tasks with Todo Web or Todo Desktop App")


for todo in todos:
    st.checkbox(todo)


st.text_input(label="Enter Your Task", placeholder="Add tasks", key="new_todo",
               on_change=add_todo)