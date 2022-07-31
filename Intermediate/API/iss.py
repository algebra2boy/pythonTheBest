import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status() # will raise an exception if any error occurs
print(response)
print(response.json())




