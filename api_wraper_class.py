import json

import requests
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Animal:
    name: str
    taxonomy: Dict[str, str]
    locations: List[str]
    characteristics: Dict[str, str]


class AnimalsAPIService:
    def __init__(self, base_url='https://api.api-ninjas.com', api_key='o67YxgljiNghUkMMJChOow==mXi6Qsx88dRzxWzD'):
        self.base_url = base_url
        self.api_key = api_key

    def get_animals_by_name(self, name):
        try:
            response = requests.get(f'{self.base_url}/v1/animals?name={name}', headers={'X-Api-Key': self.api_key})
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"An error occurred while making the request: {e}")
            return []

        if not response.text:  # If the response is empty, return an empty list
            print("Empty response received from the API.")
            return []

        try:
            data = response.json()
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}. \nResponse received: {response.text}")
            return []

        animals = [Animal(**animal) for animal in data]
        return animals


def main():
    api = AnimalsAPIService()
    animal_name = "Lion"
    animals = api.get_animals_by_name(animal_name)

    for animal in animals:
        print("Name:", animal.name)
        print("Locations:", ", ".join(animal.locations))
        print("Characteristics:")
        print("Lifespan:", animal.characteristics.get("lifespan", "Unknown"))
        print("Weight:", animal.characteristics.get("weight", "Unknown"))
        print("Diet:", animal.characteristics.get("diet", "Unknown"))
        print()


if __name__ == "__main__":
    main()
