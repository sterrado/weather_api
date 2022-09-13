from datetime import datetime
from secrets import weather_api_key
from fastapi import FastAPI, HTTPException, Response
from adapters.weather import WeatherAdapter
import requests
from decimal import Decimal


app = FastAPI()


@app.get('/weather', response_model=WeatherAdapter)
def get_weather_data(city: str = "Bogota", country: str = "CO"):
    try:
        q = city + "," + country.lower() + "&appid=" + weather_api_key
        r = requests.get(
            "http://api.openweathermap.org/data/2.5/weather?q="+q).json()
        if r['cod'] == '404':
            detail = r['message']
            print(detail, "DETAILLLLL")
            return Response( status_code=404, content= detail, )
        content = WeatherAdapter(
            location_name=city,
            temperature_celsius=round((Decimal(r['main']['temp']) - 32)*5/9, 2),
            temperature_farenheit=r['main']['temp'],
            wind=str(r['wind']),
            cloudiness=str(r['clouds']),
            pressure=r['main']['pressure'],
            humidity=r['main']['humidity'],
            sunrise=  r['sys']['sunrise'],
            sunset=r['sys']['sunset'],
            geo_coordinates=str(r['coord']),
            requested_time=datetime.now(),
            forecast=r['weather'][0])
        return content
    except Exception:
        # I know this is not OK. I just didn't have enough time to see the api.openweathermap.org docs to handle different error responses
        raise HTTPException(status_code=500,
                            detail=Exception)
