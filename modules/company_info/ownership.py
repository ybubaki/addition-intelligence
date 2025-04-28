import streamlit as st
import pandas as pd
from services.api_data import get_company_ownership
from utils.helper import ownership_type_transformer

def view(ai_isin_code: str):
    # Get the ownership data of a company.
    _data = get_company_ownership(ai_isin_code)

    st.markdown('### Ownership')

    # If no data return No Data.
    if _data is None:
        st.markdown('#### No data available.')
        return
    
    for owner in _data['ownerships']:
        with st.expander(f'Year {owner["year"]}'):
            st.write(f'**Total Shares:** {owner["total_shares"]}')
            st.write(f'**Total Percentage:** {owner["total_percentage"]}')

            st.markdown(f'##### Beneficial Owners')
            dt = {
                'Name': [],
                'Amount': [],
                'Percentage': [],
                'Country': [],
                'Type': []
            }

            for benefactor in owner['beneficial_owners']:
                dt['Name'].append(str(benefactor['name']))
                dt['Amount'].append(benefactor['amount'])
                dt['Percentage'].append(str(benefactor['percentage']))
                dt['Country'].append("N/A" if str(benefactor['country']) == "None" else str(benefactor['country']))
                dt['Type'].append(ownership_type_transformer(str(benefactor['type'])))
            
            df = pd.DataFrame(dt)
            st.dataframe(df)