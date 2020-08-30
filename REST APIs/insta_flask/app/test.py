import requests

BASE = "http://0.0.0.0:5000"

response = requests.put(BASE + "/p/asdasd",{"likes":100, "comments":12})
print(response.json)

input()

response = requests.get(BASE + "/p/asdasd")
