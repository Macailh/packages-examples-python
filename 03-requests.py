import requests

url = "https://jsonplaceholder.typicode.com/users"

r = requests.get(url, timeout=10)

r = r.json()

for user in r:
    print(user["name"])
