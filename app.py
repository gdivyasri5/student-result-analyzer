import streamlit as st
import json
import os

st.title("Student Result Analyzer")
st.write("My first deployed Python project")

FILE = "students.json"

# Load data from file
if os.path.exists(FILE):
    with open(FILE, "r") as f:
        students = json.load(f)
else:
    students = {}

# Inputs
name = st.text_input("Student Name")
marks = st.number_input("Marks", min_value=0, max_value=100, step=1)

if st.button("Add Student"):
    if name:
        students[name] = marks
        with open(FILE, "w") as f:
            json.dump(students, f)
        st.success(f"Added {name} with marks {marks}")
    else:
        st.warning("Please enter student name")

st.subheader("Current Students:")
st.json(students)
