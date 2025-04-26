import streamlit as st
from app.interface.company_interface import company_section
from app.interface.candidate_interface import candidate_section

st.title("📄 Intelligent ATS System")

tab1, tab2 = st.tabs(["For Companies", "For Candidates"])

with tab1:
    company_section()

with tab2:
    candidate_section()
