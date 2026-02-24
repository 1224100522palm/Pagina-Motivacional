import requests

API_KEY = "6ba9aed68f96f0a67696d980b0c089b4"
CITY = "Guanajuato"
URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather():
    params = {
        "q": CITY,
        "appid": API_KEY,
        "units": "metric",
        "lang": "es"
    }

    response = requests.get(URL, params=params)
    data = response.json()

    return data