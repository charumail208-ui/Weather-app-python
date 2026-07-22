import requests
from config import API_KEY
city=input("Enter city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response=requests.get(url)
if response.status_code==200:
    data=response.json()
    temperature=data['main']['temp']
    humidity=data['main']['humidity']
    condition=data['weather'][0]['main']
    description=data['weather'][0]['description']
    wind_speed=data['wind']['speed']
    print("--------------------------------------")
    print(f"Weather in {city}:")
    print("---------------------------------------")
    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather condition: {condition}")
    print(f"Weather description: {description}")
    print(f"Wind speed: {wind_speed} m/s")
else:
    print("Error: Unable to fetch weather data. Please check the city name and try again.")
if response.status_code == 404:
    print("City not found. Please check the city name and try again.")