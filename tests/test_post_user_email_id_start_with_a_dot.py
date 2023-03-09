import logging
from read_with_json_file import read_data


def test_post_user_email_id_start_with_a_dot(user):
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)

    log.debug("STEP 1. Create a new user using POST request.")
    user_data = read_data("../assert/user_email_id_start_with_a_dot.json")
    response = user.post_user(json=user_data)

    log.debug("STEP 2. Check response status code equals 422 and message equals 'is invalid'.")
    assert response.status_code == 422, f'user data: {response.json()}'
    assert response.json()[0]['message'] == 'is invalid'
