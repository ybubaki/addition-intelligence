import streamlit as st
import pandas as pd
from utils.helper import create_tabs
from utils.dummy_data import DUMMY_DATA

def view():
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