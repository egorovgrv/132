import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '36f11d263623236d507c05274d8a9dde'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = "6723"

body_create = {
        "name" : "pokejoke",
        "photo_id" : 5

}

body_change_name = {
        "pokemon_id": "45899",
        "name": "pokejokes",
        "photo_id": 5

}
body_pokeball = {
     "pokemon_id": "45899",
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

id_pokemon = response_create.json()['id']
print(id_pokemon)

response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response_change_name.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers= HEADER, json = body_pokeball)
print(response_pokeball.text)