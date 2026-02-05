import streamlit as st

st.title("Student Result Analyzer")

if "students" not in st.session_state:
    st.session_state.students = {}

students = st.session_state.students


name = st.text_input("Student Name")
marks = st.number_input("Marks", min_value=0, max_value=100)

if st.button("Add Student"):
    if name:
        students[name] = marks
        st.success(f"Added {name} with marks {marks}")
    else:
        st.warning("Please enter student name")

st.write("Current Students:", students)
