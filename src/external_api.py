import os
from http.client import responses
import requests
from dotenv import load_dotenv
load_dotenv('.env')

API_KEY = os.getenv("API_KEY")

def convert_current(valuta, rub, amount) -> float:
    """ Функция обращается к внешнему API и производит конвертацию валюты. """
    response = requests.get(
        f"https://api.apilayer.com/exchangerates_data/convert?to={rub}&from={valuta}&amount={amount}&apikey={API_KEY}")

    if response.status_code == 200:
        currency_rate = response.json()['info']['rate']#Определяем текущий курс
        result = response.json()['result']
        print(f"\nБыла произведена конвертация валюты из {valuta} в {rub} по курсу: {currency_rate}")
        return result
    else:
        print("\nЧто-то пошло не так с запросом на конвертацию валюты.")
