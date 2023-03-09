import pytest
import requests

from Api import Api
from User import User
from read_with_json_file import read_data


@pytest.fixture(scope="session")
def user():
    return User()


@pytest.fixture(scope="function")
def post_user_auto_delete(user):
    response = user.post_user(json=read_data('assert/good_user.json'))
    yield response
    user.delete_user(id_user=response.json()["id"])
