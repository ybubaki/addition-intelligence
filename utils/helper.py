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


def ownership_type_transformer(owner_type: str):
    if owner_type == "E":
        return "Mutual & Pension Fund & Trustee & Nominee"
    elif owner_type == 'B':
        return 'Bank'
    elif owner_type == 'VC':
        return 'Venture Capital'
    elif owner_type == "P":
        return "Private Equity"
    elif owner_type == "J":
        return "Foundation, Research Institute"
    elif owner_type == "C":
        return "Corporate"
    elif owner_type == "F":
        return "Financial Company"
    elif owner_type == "I":
        return "Insurance Company"
    else:
        return "N/A"