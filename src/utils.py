import json
import requests


url = "https://drive.google.com/file/d/1C0bUdTxUhck-7BoqXSR1wIEp33BH5YXy/view"
def load_transactions(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем, что запрос успешен
        data = response.json()
        if isinstance(data, list):
            return data
        else:
            return []
    except (requests.RequestException, json.JSONDecodeError):
        return []

# Пример использования
if __name__ == "__main__":
    url = "https://drive.google.com/file/d/1C0bUdTxUhck-7BoqXSR1wIEp33BH5YXy/view"
    transactions = load_transactions(url)
    print(transactions)