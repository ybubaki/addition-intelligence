import streamlit as st

def view(firmographic_data):
    st.markdown('### Firmographics')

    st.write(f'**Company Name:** {firmographic_data['name']}')

    col1, col2 = st.columns(2)

    with col1:
        st.write(f'**Sector:** {firmographic_data['sector']}')
        st.write(f'**Country:** {firmographic_data['country']}')
    
    with col2:
        st.write(f'**Listed:** {firmographic_data['listed']}')

    st.markdown(f'<div style="padding: 1em"></div>', unsafe_allow_html=True)
    st.markdown('##### Identifiers')
    col1, col2 = st.columns(2)

    with col1:
        st.write(f'**AI Code:** {firmographic_data['ai_code']}')
    
    with col2:
        st.write(f'**ISIN:** {firmographic_data['isin']}')
    
    st.markdown(f'<div style="padding: 1em"></div>', unsafe_allow_html=True)
    st.markdown('##### Market Information')

    for market in firmographic_data['market_listings']:
        st.write(f'**Listed in {market['country']}**')
        col1, col2 = st.columns(2)
        with col1:
            st.write(f'**Date Listed:** {market['date_listed']}')
            st.write(f'**Stock Exchange:** {market['stock_exchange']}')
        
        with col2:
            st.write(f'**Symbol:** {market['symbol']}')
    
    st.markdown(f'<div style="padding: 1em"></div>', unsafe_allow_html=True)
    st.markdown('##### Competitors')

    for competitors in firmographic_data['competitors']:
        st.write(f'{competitors['competitor_name']}')