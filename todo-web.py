import streamlit as st
import functions

todos = functions.get_todos()


st.title("ToDo - Web")
st.subheader("Organise your tasks with Todo Web or Todo Desktop App")


for todo in todos:
    st.checkbox(todo)


st.text_input(label="Enter Your Task", placeholder="Add tasks")