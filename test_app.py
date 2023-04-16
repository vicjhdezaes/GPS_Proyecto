import pytest
import json
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_sumar(client):
    response = client.get('/sumar?a=3&b=4')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['resultado'] == 7

def test_restar(client):
    response = client.get('/restar?a=3&b=4')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['resultado'] == -1

def test_multiplicar(client):
    response = client.get('/multiplicar?a=3&b=4')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['resultado'] == 12

def test_dividir(client):
    response = client.get('/dividir?a=12&b=4')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['resultado'] == 3
