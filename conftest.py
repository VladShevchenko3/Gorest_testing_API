import pytest
import requests

from read_with_json_file import read_data


@pytest.fixture(scope='session')
def base_url():
    return 'https://gorest.co.in/public/v2'


@pytest.fixture(scope='session')
def api_client():
    bearer = 'a28db959a3da8d6d9a137120dd6c585e2cce6254441b4017fc3dd915300a38e3'
    headers = {'Authorization': f'Bearer {bearer}', "accept": "application/json", "Content-Type": "application/json"}
    client = requests.Session()
    client.headers.update(headers)
    return client


@pytest.fixture(scope='session')
def global_var():
    return {"client_id": None}


@pytest.fixture(scope="function")
def post_user_auto_delete(base_url, api_client):
    endpoint = '/users'
    response = api_client.post(url=base_url + endpoint, json=read_data('assert/good_user.json'))
    yield response
    endpoint = f'/users/{response.json()["id"]}'
    api_client.delete(url=base_url + endpoint)
