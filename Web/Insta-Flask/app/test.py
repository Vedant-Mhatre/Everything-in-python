import requests

BASE = "http://0.0.0.0:5000"

print(f"{BASE} + /p/ashok")
response = requests.put(BASE + "/p/ashok",{"likes":999, "comments":12})
print(response.json)

# print(f"{BASE} + /p/ashok")
# response = requests.get(BASE + "/p/ashok")
# print(response.json)


# input()
# print(f"{BASE} + /ram")
# response = requests.put(BASE + "/ram",{"name":"ram", "email":"dsa"})
# print(response.json)
