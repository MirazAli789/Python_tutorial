# using weather api ==> https://api.weatherapi.com/
# 'requests' modules helps to get the http request (get request or post request)
# 'json' module helps us to convert hte string into dictionary
import requests
import json
import time

while True:
    print()
    print("Welcome to Weather.com")
    city = input("Enter the name of the city, or press q to close\n")
    if city == "q":
        break
    url = f"https://api.weatherapi.com/v1/current.json?key=c86c83165cac49bdab1135835242206&q={city}"
    r = requests.get(url)
    dic = json.loads(r.text)
    
    print("Loading ...")
    time.sleep(1)
    print("Current temparature: ", dic["current"]["temp_c"], "°C",sep="")
    time.sleep(0.1)
    print("Feels like: ", dic["current"]["feelslike_c"], "°C",sep="")
    time.sleep(0.1)
    print(dic["current"]["condition"]["text"])
    time.sleep(0.1)
    print("Current wind speed: ", dic["current"]["wind_mph"], "kmph",sep="")
    time.sleep(0.1)
    print("Humidity: ", dic["current"]["humidity"], "%",sep="")
    time.sleep(0.1)
# print(r.text)
