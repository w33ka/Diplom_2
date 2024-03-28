import pytest
import requests
import helpers
from data import Urls


@pytest.fixture
def registered_user_return_response():
    payload = helpers.payload
    response = requests.post(Urls.REGISTER_USER, json=payload)
    yield response
    access_token = response.json()['accessToken']
    requests.delete(Urls.DELETE_USER, headers={'Authorization': access_token})


@pytest.fixture
def registered_user_return_log_pass():
    payload = helpers.payload
    response = requests.post(Urls.REGISTER_USER, json=payload)
    yield payload
    access_token = response.json()['accessToken']
    requests.delete(Urls.DELETE_USER, headers={'Authorization': access_token})


@pytest.fixture
def registered_user_return_token():
    payload = helpers.payload
    response = requests.post(Urls.REGISTER_USER, json=payload)
    access_token = response.json()['accessToken']
    yield access_token
    requests.delete(Urls.DELETE_USER, headers={'Authorization': access_token})
