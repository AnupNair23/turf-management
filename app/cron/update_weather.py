import schedule
import time
from app.db.database import get_db
from app.crud.weather import get_forecast_weather_data, get_weather_data
from datetime import datetime
import json


def format_weather_data(weather_data):
    weather_info = {}
    for data in weather_data:
        date = datetime.utcfromtimestamp(data['dt'])
        weather_info[date.strftime("%Y-%m-%d %H:%M:%S")] = data['rain'] if data.get("rain") else None

    return weather_info

def format_weather_today(weather_data):
    

def update_pitch_values():
    # Implement the logic to update pitch values here
    print("Updating pitch values...")
    db = get_db()
    db_pitches= db["pitches"].find()
    if db_pitches:
        for pitch in db_pitches:
            print("pitch>>>", pitch)
            lat = pitch['lat']
            long = pitch['long']
            weather_forecast_data = get_forecast_weather_data(lat, long)
            print('forcecastDsta???', weather_forecast_data)
            weather_forecast_formatted_data = format_weather_data(weather_forecast_data['list'])
            weather_forecast_json_data = json.dumps(weather_forecast_formatted_data, default=str)  # Convert dictionary to JSON string
            print('weatherData>>>', weather_forecast_json_data)
            weather_today = get_weather_data(lat, long)
            print('weatherData>>>', weather_today)
            formatted_weather_today = format_weather_today(weather_today)
    print("done>>>>")

# Schedule the function to run hourly
schedule.every().minute.do(update_pitch_values)



# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep for 1 second to avoid consuming too much CPU
