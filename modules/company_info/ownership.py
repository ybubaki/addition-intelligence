import streamlit as st
from services.api_data import get_company_ownership

def view(ai_isin_code: str):
    # Get the ownership data of a company.
    _data = get_company_ownership(ai_isin_code)

    st.markdown('### Ownership')

    # If no data return No Data.
    if _data is None:
        st.markdown('#### No data available.')
        return
    
    for owner in _data['ownerships']:
        with st.expander(f'Year {owner['year']}'):
            st.write(f'**Total Shares:** {owner['total_shares']}')
            st.write(f'**Total Percentage:** {owner['total_percentage']}')

            st.markdown(f'##### Beneficial Owners')
            for benefactor in owner['beneficial_owners']:
                st.write(f'**Name:** {benefactor['name']}')

                col1, col2 = st.columns(2)

                with col1:
                    st.write(f'**Amount:** {benefactor['amount']}')
                    st.write(f'**Percentage:** {benefactor['percentage']}')
                
                with col2:
                    st.write(f'**Country:** {benefactor['country']}')
                    st.write(f'**Type:** {benefactor['type']}')
                
                st.markdown(f'<div style="padding: 0.5em"></div>', unsafe_allow_html=True)