import requests

Parameter = {
    "lat": 36.7201600,
    "lng": -4.4203400,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=Parameter)
print(response)
print(response.json())