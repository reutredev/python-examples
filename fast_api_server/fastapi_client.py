import requests

response = requests.get("http://127.0.0.1:5000/tasks")
print(response.json())

response = requests.get("http://127.0.0.1:5000/tasks/1")
print(response.json())