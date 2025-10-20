import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.api-ninjas.com/v1/animals?name="

def fetch_data(animal_name):
    """
    Fetches animals data from the API.
    Returns a list of animals (dictionaries) or an empty list if none found.
    """
    response = requests.get(
        f"{BASE_URL}{animal_name}",
        headers={"X-Api-Key": API_KEY}
    )

    if response.status_code == 200:
        data = response.json()
        return data if data else []
    else:
        print(f"Error {response.status_code}: {response.text}")
        return []
