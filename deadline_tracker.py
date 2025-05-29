import streamlit as st
from datetime import datetime

st.title("🗓️ Simple Deadline Tracker")

# Sidebar mein task add karne ka form
st.sidebar.header("Naya Task Add Karein")

task_name = st.sidebar.text_input("Task ka naam")
deadline_date = st.sidebar.date_input("Deadline ki tareekh")

if st.sidebar.button("Add Task"):
    if "tasks" not in st.session_state:
        st.session_state.tasks = []
    st.session_state.tasks.append({"task": task_name, "deadline": deadline_date})
    st.sidebar.success(f"Task '{task_name}' add ho gaya hai!")

# Tasks ko display karna
st.header("Tasks aur Deadlines")

if "tasks" in st.session_state and st.session_state.tasks:
    # Tasks ko deadline ke hisaab se sort karo
    tasks_sorted = sorted(st.session_state.tasks, key=lambda x: x["deadline"])
    
    for task in tasks_sorted:
        days_left = (task["deadline"] - datetime.now().date()).days
        if days_left < 0:
            status = "⏰ Deadline guzar chuki hai!"
        elif days_left == 0:
            status = "🚨 Aaj deadline hai!"
        else:
            status = f"⌛ {days_left} din baaqi hain."
        
        st.write(f"**{task['task']}** — Deadline: {task['deadline']} — {status}")
else:
    st.write("Koi task add nahi hua hai.")
