import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)

st.set_page_config(page_title="ToDo-Web")

st.title("ToDo-Web")
st.subheader("Organise your tasks with Todo Web or Todo Desktop App")

st.text_input(label="Enter Your Task", placeholder="Add tasks", key="new_todo",
               on_change=add_todo)

if st.text_input:
    for index, todo in enumerate(todos):
        checkbox = st.checkbox(todo, key=todo)
        if checkbox:
            todos.pop(index)
            functions.write_todos(todos)
            to_do = st.session_state[todo]
            del to_do
            st.experimental_rerun()
else:
    st.info("No text to Add")






