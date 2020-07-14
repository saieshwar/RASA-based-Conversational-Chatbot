
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import requests
import json 

class ActionWeather(Action):
 def name(self):
  return "action_weather"
 def run(self,dispatcher,tracker,domain):
  city = tracker.get_slot('location')
  response = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&APPID=2609ba33a23594fb5182c41263daa18c".format(city))
  data = response.json()
  main=data['main']
  wind = data['wind']
  sys = data['sys']
  weather = data['weather']
  ##desc=a[2]['weather']
  place = data["name"]
  country = sys["country"]
  temp = round(main['temp'] - 273.15, 2)
  feels_like = round(main['feels_like'] - 273.15, 2)
  temp_min = round(main['temp_min'] - 273.15, 2)
  temp_max = round(main['temp_max'] - 273.15, 2)
  speed = wind['speed']
  ##degree = wind['deg']
  desc = weather[0]['description']
  weather_data = "Weather in {} , {} is {}.It's currently {}*C which feels like {} with max temp and min temp {}, {} respectively. The wind speed is {}. Overall, the weather is {}".format(place, country, desc, temp, feels_like,temp_max,temp_min,speed,desc)
  dispatcher.utter_message(weather_data)
  return [SlotSet("location", city)]
##print(weather_data)
# http://api.openweathermap.org/data/2.5/weather?q=hyderabad&APPID=2609ba33a23594fb5182c41263daa18c
##"https://api.openweathermap.org/data/2.5/weather?q={}&APPID=2609ba33a23594fb5182c41263daa18c".format(city)