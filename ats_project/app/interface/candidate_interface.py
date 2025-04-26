import streamlit as st
from app.services.candidate_service import process_candidate

def candidate_section():
    st.header("Candidate ATS Section")
    jd_file = st.file_uploader("Upload Job Description (JD)", type=['pdf', 'docx'])
    resume_file = st.file_uploader("Upload Resume", type=['pdf', 'docx'], key="candidate_resume_upload")


    if jd_file and resume_file:
        if st.button("Analyze Resume"):
            with st.spinner('Processing...'):
                result = process_candidate(jd_file, resume_file)
                st.success("Processing Completed!")

                st.write(f"**Score:** {result['Score']}%")
                st.write(f"**Status:** {result['Status']}")
                st.write("**Strong Points:**")
                st.write(", ".join(result['Strong Points']))
                st.write("**Weak Points:**")
                st.write(", ".join(result['Weak Points']))
                st.write("**Suggestions:**")
                st.write(", ".join(result['Suggestions']))
