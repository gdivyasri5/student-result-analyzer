import streamlit as st

st.title("Student Result Analyzer")
st.write("My first deployed Python project")

# ✅ SESSION STATE (THIS IS THE KEY PART)
if "students" not in st.session_state:
    st.session_state.students = {}

# Inputs
name = st.text_input("Student Name")
marks = st.number_input("Marks", min_value=0, max_value=100, step=1)

# Button
if st.button("Add Student"):
    if name:
        st.session_state.students[name] = marks
        st.success(f"Added {name} with marks {marks}")
    else:
        st.warning("Please enter student name")

# Display students
st.subheader("Current Students:")
st.json(st.session_state.students)
