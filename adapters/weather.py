from pydantic import BaseModel
from datetime import datetime


class WeatherAdapter(BaseModel):
    location_name: str
    temperature_celsius: str
    temperature_farenheit: str
    wind: str
    cloudiness: str
    pressure: str
    humidity: str
    sunrise: str
    sunset: str
    geo_coordinates: str
    requested_time: datetime
    forecast: dict
