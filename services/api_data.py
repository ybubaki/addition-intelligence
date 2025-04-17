import requests

_BASE_URL = "https://addi-server.onrender.com/"

def get_company_firmographics(ai_code_or_isin: str):
    try:
        url = f"{_BASE_URL}/firmographics/{ai_code_or_isin}"
        response = requests.get(url)
        print(response.json())
        return response.json()
    except Exception as e:
        print(e)
        return None


def get_company_ownership(ai_code_or_isin: str):
    try:
        url = f"{_BASE_URL}/ownership/{ai_code_or_isin}"
        response = requests.get(url)
        print(response.json())
        return response.json()
    except Exception as e:
        print(e)
        return None

