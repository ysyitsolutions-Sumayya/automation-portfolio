import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=25.2&longitude=55.27&current=temperature_2m,wind_speed_10m"

response = requests.get(url)

print(response.status_code)
print(response.json())

data = response.json()

temperature = data["current"]["temperature_2m"]
wind = data["current"]["wind_speed_10m"]

print(f"Temperature: {temperature} °C")
print(f"Wind: {wind} km/h")