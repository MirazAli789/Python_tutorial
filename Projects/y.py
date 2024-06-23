import requests

loc = input("Enter Location \n")
url = f"https://api.weatherapi.com/v1/current.json?key=c86c83165cac49bdab1135835242206&q={loc}"
r = requests.get(url)
print(r.text)
