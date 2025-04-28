import requests
import json

# URL de la Azure Function
url = "https://miapp.azurewebsites.net/api/fa-de-challenge"

payload = {
    "table": "hired_employees",
    "data": [{"id": 1, "name": "Juan"}, {"id": 2, "name": "Ana"}]
}


response = requests.post(url, json=payload)

if response.status_code == 200:
    print("Data correctly written")
else:
    print(f"Error : {response.text}")
