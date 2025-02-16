from fastapi.testclient import TestClient
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

from api import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == 'Welcome to the API'
""" 
from fastapi import status
import requests
import json

def test_check_client_id():
    Test la fonction check_client_id() de l'API avec un client faisant partie de la base de données.
    url = API_URL + str(192535)
    response = requests.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert json.loads(response.content) == True


def test_check_client_id_2():
    Test la fonction check_client_id() de l'API avec un client ne faisant pas partie de la base de données.
    url = API_URL + str(100000)
    response = requests.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert json.loads(response.content) == False


def test_get_prediction():
    Test la fonction get_prediction() de l'API.s
    url = API_URL + "prediction/" + str(192535)
    response = requests.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert json.loads(response.content) == 0.4805479971101088


"""

