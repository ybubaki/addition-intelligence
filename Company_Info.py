import streamlit as st
from utils.helper import create_tabs
from modules.company_info import summary, financial, ownership, quantitative

def main():
    # Configure page title for the homepage.
    st.set_page_config(page_title="Addition Intelligence")

    # This section creates a search form for users to input a company name.
    with st.form(key='search_form', border=False):
        col1, col2 = st.columns([5, 1])

        with col1:
            search_query = st.text_input("", placeholder='Search company...', label_visibility='collapsed')
        
        with col2:
            submit_button = st.form_submit_button(label="Search", use_container_width=True)
    
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
    with st.container():
        st.markdown('<div class="centered-container">company name</div>', unsafe_allow_html=True)
    
        
    # Create tabs to display different types of company information
    summary_tab, financial_tab, ownership_tab, quantitative_tab = create_tabs(['Summary', 'Financial Statement', 'Ownership', 'Quantitative Disclosure'])
    
    with summary_tab:
        summary.view()
    
    with financial_tab:
        financial.view()
    
    with ownership_tab:
        ownership.view()
    
    with quantitative_tab:
        quantitative.view()

if __name__ == '__main__':
    main()
