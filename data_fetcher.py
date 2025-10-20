import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.api-ninjas.com/v1/animals?name="

def fetch_data(animal_name):
    """
    Fetches the animals data for the given 'animal_name'.
    Returns a list of animals (each is a dictionary with keys: name, taxonomy, locations, characteristics)
    """
    response = requests.get(
        f"{BASE_URL}{animal_name}",
        headers={"X-Api-Key": API_KEY}
    )
    if response.status_code == 200:
        return response.json() if response.json() else []
    else:
        print(f"Error {response.status_code}: {response.text}")
        return []
