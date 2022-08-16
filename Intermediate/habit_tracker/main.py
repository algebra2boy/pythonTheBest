import requests
import datetime

# Create a user without going to the website GUI directly
pixela_endpoints = "https://pixe.la/v1/users"

USERNAME = "algebra2boy"
TOKEN = "yongyeshishuaige"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoints, json=user_params)
# print(response.text) -> it returns {"message":"Success. Let's visit https://pixe.la/@algebra2boy , it is your profile page!","isSuccess":true}

graph_endpoint = f"{pixela_endpoints}/{USERNAME}/graphs"

# graph_config = {
#     "id": "graph1",
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai"
# }
#
headers = {
    "X-USER-TOKEN": TOKEN
}
# # header is used to authenticate users
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# post value to the graph
ID = "graph1"
pixel_post_endpoint = f"{pixela_endpoints}/{USERNAME}/graphs/{ID}"


today = datetime.datetime.now()
body = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10.2"
}
response2 = requests.post(url=pixel_post_endpoint, json=body, headers=headers)
print(response2.text)
