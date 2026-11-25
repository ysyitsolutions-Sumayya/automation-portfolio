import requests

URL = "https://api.open-meteo.com/v1/forecast?latitude=25.2&longitude=55.27&current=temperature_2m,wind_speed_10m"

def get_weather():
    response = requests.get(URL)
    if response.status_code != 200:
        raise Exception(f"Weather service failed with status {response.status_code}")
    data = response.json()
    return {
        "city": "Dubai",
        "temperature": data["current"]["temperature_2m"],
        "wind": data["current"]["wind_speed_10m"],
    }

def make_report(weather):
    return f"In {weather['city']} it is {weather['temperature']} °C, with wind at {weather['wind']} km/h."

weather = get_weather()
print(make_report(weather))