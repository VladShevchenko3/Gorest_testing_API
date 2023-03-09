import logging
from read_with_json_file import read_data


def test_delete_user(user):
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)

    log.debug("STEP 1. Create a new user using POST request.")
    user_data = read_data('../assert/good_user.json')
    response_post_user = user.post_user(user_data)

    log.debug("STEP 2. Check response status code equals 201.")
    assert response_post_user.status_code == 201, f'{response_post_user.json()}'

    log.debug("STEP 3. Delete user using DELETE request.")
    response = user.delete_user(id_user=response_post_user.json()["id"])

    log.debug("STEP 4. Check response status code equals 204.")
    assert response.status_code == 204
