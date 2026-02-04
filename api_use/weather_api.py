import os
import requests
from dotenv import load_dotenv

load_dotenv(override=True)

class WeatherTool:
    def __init__(self):
        self.key = os.getenv("WEATHER_API_KEY")
        if not self.key:
            raise RuntimeError("WEATHER_API_KEY missing")

    def get_weather(self, city: str) -> dict:
        r = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={"q": city, "appid": self.key, "units": "metric"},
            timeout=10
        )
        r.raise_for_status()
        data = r.json()

        return {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
