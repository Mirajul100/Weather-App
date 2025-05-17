import requests as rs
import os

API_KEY = os.getenv("API")

def get_data(city_name , days=None):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"
    response = rs.get(url)
    data = response.json()
    return data

if __name__ == ("__main__"):
    print(get_data(city_name="Dhaka"))
