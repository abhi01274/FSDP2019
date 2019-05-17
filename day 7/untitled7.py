"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""

import requests
entry = input("enter the city name")

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q="+entry
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
response = requests.get(url)

res1= response.json()

print("longitude >>",res1["coord"]["lon"])
print("latitude >>",res1["coord"]["lat"])
print("weather conditions >>", res1["weather"][0]["description"])
print("wind speed >>", res1["wind"]["speed"])
print("Sunrise >>", res1["sys"]["sunrise"])
print("Sunset >>", res1["sys"]["sunset"])
