import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()


def convert_to_rub(amount, currency):
    """
    Конвертирует сумму в рубли с использованием внешнего API.

    """
    if currency == "RUB":
        return float(amount)

    # Получаем токен API из переменных окружения
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY не найден в переменных окружения.")

    # URL для получения курса валют
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

    # Заголовки для запроса
    headers = {
        "apikey": api_key
    }

    # Выполняем запрос к API
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Ошибка при запросе к API: {response.status_code}")

    # Получаем результат конвертации
    result = response.json()
    return float(result['result'])