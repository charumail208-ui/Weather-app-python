import requests
from config import API_KEY
city=input("Enter city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response=requests.get(url)
if response.status_code==200:
    print("Request successful!")
else:
    print("Error occurred while fetching weather data.")