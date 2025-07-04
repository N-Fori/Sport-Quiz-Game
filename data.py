import requests


parameters = {
    "amount": 40,
    "type": "boolean",
    "category": 21,
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]

