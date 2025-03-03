import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8a88b93abc3840848bf3496e3bb389c5'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create )
print(response_create.text) 

POKEMONS_ID = response_create.json()['id']
print(POKEMONS_ID)

body_change = {
    "pokemon_id": POKEMONS_ID,
    "name": "generate"
}

response_change = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = body_change )
print(response_change.text) 

body_catch = {
    "pokemon_id": POKEMONS_ID
}

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch )
print(response_catch.text)
