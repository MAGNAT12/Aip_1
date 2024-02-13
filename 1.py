import requests

respons = requests.get("https://jsonplaceholder.typicode.com/todos")

n = respons.json()

print(n[1])
