import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '36f11d263623236d507c05274d8a9dde'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = "6723"

def teststatus_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

    def test_name():
        response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
        assert response_get.json()["data"][0]["trainer_name"] == "Тренер"