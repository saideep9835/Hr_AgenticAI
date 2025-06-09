import streamlit as st
import requests

st.title(" HR Agentic Planner")
prompt = st.text_area("Describe the role you want to hire for:")

if st.button("Generate Plan"):
    with st.spinner("Thinking..."):
        response = requests.post("http://localhost:8000/plan", json={"prompt": prompt})
        if response.status_code == 200:
            result = response.json()
            st.json(result["plan"])
        else:
            st.error("Error generating plan.")
