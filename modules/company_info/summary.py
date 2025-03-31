import streamlit as st
from utils.dummy_data import DUMMY_DATA, get_firmographics_data


# This function renders the summary tab, displaying key company information including firmographics, financial statements, and ownership details.
def view():

    
    # Define sections to display key company information
    firmographics = get_firmographics_data()
    sections = [
        # ("Company Firmographics", DUMMY_DATA['firmographics']),
        ("Financial Statement", DUMMY_DATA['financial_statement']),
        ("Ownership Summary", DUMMY_DATA['ownership_summary'])
    ]

    with st.container(border=True):
        st.markdown("### Company Firmographics")
        for key, value in firmographics.items():
            with st.expander(f"{key}", expanded=False):
                for key, item in value[0].items():
                    st.write(f"**{key}:** {item}")

    # Loop through each section to display company information
    for title, data in sections:
            with st.container(border=True):
                st.markdown(f"### {title}")
                for key, value in data.items():
                    st.write(f"**{key}:** {value}")
     
