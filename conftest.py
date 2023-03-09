import pytest
import requests

from Api import Api
from User import User
from read_with_json_file import read_data


@pytest.fixture(scope="function")
def user(global_var):
    yield User()
    if global_var['client_id'] is not None:
        print("f")
        print(global_var['client_id'])
        User().delete_user(global_var['client_id'])


@pytest.fixture(scope="function")
def post_user_auto_delete(user):
    response = user.post_user(json=read_data('assert/good_user.json'))
    yield response
    user.delete_user(id_user=response.json()["id"])


@pytest.fixture(scope='session')
def global_var():
    return {"client_id": 1}
