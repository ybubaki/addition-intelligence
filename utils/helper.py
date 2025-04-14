import streamlit as st
from streamlit.components.v1 import html

# Function to change the page title using JavaScript
def set_page_title(title: str) -> None:
    js = f"""
    <script>
        document.title = "{title}";
    </script>
    """
    html(js)

# This function takes a list of tab names as input and creates corresponding tabs in the Streamlit app.
# It utilizes the st.tabs method to render the tabs and allows users to switch between them.
def create_tabs(tab_names: list[str]):
    """Creates Streamlit tabs and returns the selected tab."""
    return st.tabs(tab_names)

def get_value_of_list_from_key(employees, key: str):
    value = employees[-1][key] if employees[-1][key] != 0 else employees[-2][key]
    return value
