import requests

def fetch_data(endpoint, filters={}):
    url = f"https://rickandmortyapi.com/api/{endpoint}"
    response = requests.get(url, params=filters)

    if response.status_code == 200:
        return response.json()
    else:
        return None

characters = fetch_data("character", {"nome": "Rick"})

if characters:
    print(characters)
else:
    print("Failed to fetch data")
