import logging
from read_with_json_file import read_data


def test_post_existed_user(user, global_var):
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)

    log.debug("STEP 1. Create a new user using POST request.")
    user_data = read_data('../assert/good_user.json')
    response_post_user = user.post_user(user_data)

    log.debug("STEP 2. Check response status code equals 201.")
    assert response_post_user.status_code == 201, f'{response_post_user.json()}'

    log.debug("STEP 3. Create an existed user using POST request.")
    response_post_existed_user = user.post_user(user_data)

    log.debug("STEP 4. Check response status code equals 422 and message equals 'has already been taken'")
    assert response_post_existed_user.status_code == 422
    assert response_post_existed_user.json()[0]['message'] == 'has already been taken'

    log.debug("STEP 5. Add user id to `global_var` fixture.")
    global_var['client_id'] = response_post_user.json()['id'] if 'id' in response_post_user.json() else None
