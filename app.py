import streamlit as st

st.title("🧠 AI Resume Generator")
st.write("Create a smart, job-ready resume using AI")

# Input fields
name = st.text_input("Full Name")
skills = st.text_input("Skills (comma-separated)")
work_history = st.text_area("Work History / Experience")
job_role = st.text_input("Target Job Role")

# Button
if st.button("Generate Resume"):
    st.warning("🚧 AI functionality coming soon...")

# Footer
st.caption("Built by Maham Imran – Aspiring AI Developer")
