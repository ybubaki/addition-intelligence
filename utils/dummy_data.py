import pandas as pd

DUMMY_DATA = {"firmographics": {
    "Company Name": "Example Corp",
    "Industry": "Technology",
    "Location": "San Francisco, CA",
    "Founded": "2010",
    "Employees": 500,
    "Revenue": "$100M"
},
"financial_statement": {
    "Total Assets": "$1,000,000",
    "Total Liabilities": "$400,000",
    "Equity": "$600,000",
    "Revenue": "$500,000",
    "Net Income": "$100,000"
},
"ownership_summary": {
    "Major Shareholder": "John Doe",
    "Ownership Percentage": "25%",
    "Institutional Investors": "ABC Capital, XYZ Investments",
    "Total Shares Outstanding": "1,000,000",
    "Insider Ownership": "15%"
},
"cash_flow_data": {
    "Description": [
        "Net Income",
        "Depreciation & Amortization",
        "Change in Working Capital",
        "Cash from Operations",
        "Capital Expenditures",
        "Cash from Investing Activities",
        "Dividends Paid",
        "Cash from Financing Activities",
        "Net Change in Cash"
    ],
    "Amount": [
        "$120,000",
        "$30,000",
        "$10,000",
        "$160,000",
        "$-20,000",
        "$-10,000",
        "$-5,000",
        "$-15,000",
        "$110,000"
    ]
},
"income_statement_data": {
    "Description": [
        "Revenue",
        "Cost of Goods Sold",
        "Gross Profit",
        "Operating Expenses",
        "Operating Income",
        "Other Income",
        "Net Income Before Tax",
        "Income Tax Expense",
        "Net Income"
    ],
    "Amount": [
        "$500,000",
        "$300,000",
        "$200,000",
        "$50,000",
        "$150,000",
        "$10,000",
        "$160,000",
        "$40,000",
        "$120,000"
    ]
}
}


def get_firmographics_data():
    df = pd.read_excel(r'platform-requirement.xlsx', sheet_name='Firmographic')

    main_columns = df.columns
    main_columns.to_list()

    df.columns = df.iloc[0]
    df = df[1:].reset_index(drop=True)
    sub_columns = df.columns.to_list()

    data = {}
    counter = 4
    count = 0
    data['Firmographic'] = {}
    firmographic = data['Firmographic']

    name_index = ""
    while count < counter:
      ds = df.iloc[count]
      index = 0
      while index < len(main_columns):
        if "Unnamed" not in main_columns[index]:
          if name_index != "" and firmographic.get(name_index) == None:
            firmographic[name_index] = []
          if not len(name_index) == 0:
            firmographic[name_index].append(temp_data)
          name_index = main_columns[index]
          temp_data = {}
        temp_data[sub_columns[index]] = ds[sub_columns[index]]
        index += 1
      count += 1
    return data['Firmographic']

# get_firmographics_data()