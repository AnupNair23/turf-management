import requests
from app.core.config import settings

def get_geo(query: str) -> dict:
    # db = get_db()
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={query}&limit=1&appid={settings.OPENWEATHER_API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        # Handle API request errors
        response.raise_for_status()
        
def get_forecast_weather_data(lat: str, long: str) -> dict:
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={long}&units=metric&appid={settings.OPENWEATHER_API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        # Handle API request errors
        response.raise_for_status()
        
def get_weather_data(lat: str, long: str) -> dict:
    # https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid={API key}
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&units=metric&appid={settings.OPENWEATHER_API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        # Handle API request errors
        response.raise_for_status()