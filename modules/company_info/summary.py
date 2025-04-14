import streamlit as st
from utils.helper import get_value_of_list_from_key

# This function renders the summary tab, displaying key company information including firmographics, financial statements, and ownership details.
def view(firmographics_data):
    
    sections = []

    with st.container(border=True):
        st.markdown("### Firmographics")
        st.write(f'**Company Name:** {firmographics_data["name"]}')
        col1, col2 = st.columns(2)
        with col1:
            st.write(f'**AI Code:** {firmographics_data['ai_code']}')
            st.write(f'**ISIN:** {firmographics_data['isin']}')
            st.write(f'**Listed:** {firmographics_data['listed']}')
            st.write(f'**Country:** {firmographics_data["country"]}')
        with col2:
            st.write(f'**Sector:** {firmographics_data['sector']}')
            st.write(f'**Number of employees:** {get_value_of_list_from_key(firmographics_data['employees'], 'count')}')
            st.write(f'**Number of branches:** {get_value_of_list_from_key(firmographics_data['branches'], 'count')}')

    # Loop through each section to display company information
    for title, data in sections:
            with st.container(border=True):
                st.markdown(f"### {title}")
                for key, value in data.items():
                    st.write(f"**{key}:** {value}")