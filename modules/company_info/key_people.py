import streamlit as st

def view(key_people):
    st.markdown('### Key People')

    for person in key_people:
        st.write(f'**Name:** {person['name']}')

        col1, col2 = st.columns(2)
        with col1:
            st.write(f'**Title:** {person['title']}')
            st.write(f'**Profession:** {person['profession']}')
        
        with col2:
            st.write(f'**Age:** {person['age'] if person['age']  else 'N/A'}')
            st.write(f'**Nationality:** {person['nationality']}')
        
        st.write(f'**Education:** {person['education']}')
        st.markdown(f'<div style="padding: 0.5em"></div>', unsafe_allow_html=True)
