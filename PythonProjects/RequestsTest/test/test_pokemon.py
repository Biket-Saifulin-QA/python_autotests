import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8a88b93abc3840848bf3496e3bb389c5'
HEADER = {'Content-Type':'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '22792'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', headers = HEADER, params = {'trainer_id':TRAINER_ID})
    assert response.status_code == 200

def test_name():
    response_get = requests.get(url = f'{URL}/trainers', headers = HEADER, params = {'trainer_id':TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'Kass'
