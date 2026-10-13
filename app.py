import streamlit as st
from src.database import init_db, add_task, get_tasks

st.set_page_config(page_title="Local Python App")

init_db()

st.title("My Local Application")
st.write("Python UI + local SQLite database")

with st.form("task_form"):
    title = st.text_input("Task name")
    submitted = st.form_submit_button("Add task")

    if submitted:
        if title.strip():
            add_task(title.strip())
            st.success("Task added")
        else:
            st.warning("Enter a task name")

st.subheader("Saved tasks")

for task_id, title, completed in get_tasks():
    st.write(f"{task_id}. {title}")