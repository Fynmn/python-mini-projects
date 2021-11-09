import requests

url = "https://community-open-weather-map.p.rapidapi.com/climate/month"

city = input("Enter city: ")

querystring = {"q":city}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "d7d361dd5bmsh025fd0ec605e154p1278d2jsnfaf1f0b3d451"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

result = response.json()

temp = round(result["list"][0]["temp"]["average"] - 273.15)

print(f"Temperature in {city} is {temp} degrees celsius")