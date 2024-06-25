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
    print("Searching ...")
    time.sleep(1)
    print("Current temparature:", dic["current"]["temp_c"], "°C")
    print("Feels like:", dic["current"]["feelslike_c"], "°C")
    print(dic["current"]["condition"]["text"])
    print("Current wind speed:", dic["current"]["wind_mph"], "kmph")
    print("Humidity:", dic["current"]["humidity"], "%")

# print(r.text)
