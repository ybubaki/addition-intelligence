import streamlit as st
from utils.helper import create_tabs
from modules.company_info import summary, firmographics, key_people, ownership, financial, financial_ratios
from services.api_data import get_company_firmographics

def main():
    # Configure page title for the homepage.
    st.set_page_config(page_title="Addition Intelligence")

    _firmographics_data = None
    _data_loaded = False

    # This section creates a search form for users to input a company name.
    with st.form(key='search_form', border=False):
        col1, col2 = st.columns([5, 1])

        with col1:
            search_query = st.text_input("", placeholder='Search company...', label_visibility='collapsed')
        
        with col2:
            submit_button = st.form_submit_button(label="Search", use_container_width=True)
    
    if submit_button and search_query:
        _data_loaded = True
        _firmographics_data = get_company_firmographics(search_query.strip().upper())

    # Styles for the company name div
    st.markdown(
        """
        <style>
        .centered-container {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 1em;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            background-color: #f0f0f0; /* Light gray background */
            border-radius: 10px;
            margin-bottom: 32px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # this code shows the company name.
    if search_query and search_query != '':
        with st.container():
            st.markdown(f'<div class="centered-container">{search_query}</div>', unsafe_allow_html=True)
    
        
    # Create tabs to display different types of company information
    if _data_loaded and _firmographics_data is not None:
        summary_tab, firmographics_tab, key_people_tab, ownership_details_tab, financial_statement_tab, financial_ratios_tab = create_tabs(['Summary', 'Firmographics', 'Key People', 'Ownership Details', 'Financial Statement', 'Financial Ratios'])
        
        with summary_tab:
            summary.view(_firmographics_data)
        
        with firmographics_tab:
            firmographics.view(_firmographics_data)
        
        with key_people_tab:
            key_people.view(_firmographics_data['key_people'])
        
        with ownership_details_tab:
            ownership.view(search_query)
        
        with financial_statement_tab:
            financial.view()
        
        with financial_ratios_tab:
            financial_ratios.view()
    
    elif _data_loaded and _firmographics_data is None:
        st.markdown(
            """
            <div style="text-align: center;">
                <p style="font-size:20px;">Company not found. Please try again.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <div style="text-align: center;">
                <p style="font-size:20px;">Search for a company to get started</p>
            </div>
            """,
            unsafe_allow_html=True)
if __name__ == '__main__':
    main()
