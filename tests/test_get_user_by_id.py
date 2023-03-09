import logging
from read_with_json_file import read_data


def test_get_user_by_id(user, global_var):
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)

    log.debug("STEP 1. Create a new user using POST request.")
    user_data = read_data('../assert/good_user.json')
    response_post_user = user.post_user(user_data)

    log.debug("STEP 2. Check response status code equals 201.")
    assert response_post_user.status_code == 201, f'{response_post_user.json()}'

    log.debug("STEP 3. Add user id to `global_var` fixture.")
    global_var['client_id'] = response_post_user.json()['id'] if 'id' in response_post_user.json() else None

    log.debug("STEP 4. Get user information using GET request.")
    response_get_user = user.get_user(params={'page': 1, 'id': response_post_user.json()["id"]})

    log.debug("STEP 5. Check response status code equals 200.")
    assert response_get_user.status_code == 200, response_get_user.json()
