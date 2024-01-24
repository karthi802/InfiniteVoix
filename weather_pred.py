from math import floor
import requests

def tellWeather(city_name):
    api_key="api key"
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    
    complete_url=base_url+"appid="+api_key+"&q="+city_name
    response = requests.get(complete_url)
    x=response.json()
    if x["cod"]!="404":
        y=x["main"]
        current_temperature = y["temp"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]

        temperature_celius = floor(current_temperature - 273.15)
        
        res = "temperature is " + str(temperature_celius) +" humidity is (in percentage) "+str(current_humidiy) +"\n description = " + str(weather_description)+"present this"
        return res
    
