
import requests
import os
from datetime import datetime
user_api = os.environ['current_weather_data']
location = input ('enter the city name:')
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid=" +user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()
if api_data['cod'] =='404':
    print ("Invalid City :Please Enter Valid City ")
else:
    temp_city = (api_data["main"]["temp"])
    weather_desc =api_data['weather'][0]['description']
    wind_speed =api_data['main']['temp']
    humidity = api_data['main']['temp']
    date_string = datetime.now().strftime('%d/%m/%m||%H:%M:%S')
    print ("Weather State Of - {}||{}".format(location.upper(),date_string))
    print (".......................................................................")
    print (".......................................................................")
    print ("current temperature is :",temp_city,"kelvin")
    print ("current weather desc is:",weather_desc)
    print ("current wind speed:" ,wind_speed,"kmph")
    print ("current humidity :" ,humidity,"%")



        


