import streamlit as st
from app.services.company_service import process_company

def company_section():
    st.header("Company ATS Section")
    jd_file = st.file_uploader("Upload Job Description (JD)", type=['pdf', 'docx'], key="candidate_jd_upload")
    resume_files = st.file_uploader("Upload Multiple Resumes", type=['pdf', 'docx'], accept_multiple_files=True)

    if jd_file and resume_files:
        if st.button("Analyze Resumes"):
            with st.spinner('Processing...'):
                results = process_company(jd_file, resume_files)
                st.success("Processing Completed!")
                st.dataframe(results)
                st.download_button(
                    label="Download Report",
                    data=open('output_company.xlsx', 'rb'),
                    file_name='output_company.xlsx',
                    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
