import streamlit as st
import pandas as pd
from utils.helper import create_tabs
from utils.dummy_data import DUMMY_DATA


def view():
    """
    Displays the financial statements tab content with three sub-tabs:
    - Cash Flow: Shows the company's cash flow statement
    - Income Statement: Shows the company's profit and loss statement 
    - Balance Sheet: Shows the company's assets, liabilities and equity

    The function creates tabs using create_tabs() helper and renders the appropriate
    view for each financial statement when its tab is selected.
    """
    cash_flow, income_statement, balance_sheet = create_tabs(['Cash Flow', 'Income Statement', 'Balance Sheet'])

    with cash_flow:
        _cash_flow_view()

    with income_statement:
        _income_statement_view()
        


def _cash_flow_view():
    cash_flow_df = pd.DataFrame(DUMMY_DATA['cash_flow_data'])

    st.markdown("### Cash Flow Statement")
    st.table(cash_flow_df)

def _income_statement_view():
    income_statement_df = pd.DataFrame(DUMMY_DATA['income_statement_data'])

    st.markdown("### Income Statement")
    st.table(income_statement_df)