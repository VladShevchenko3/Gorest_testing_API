import logging
from read_with_json_file import read_data


def test_patch_user_name(user):
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)

    log.debug("STEP 1. Create a new user using POST request.")
    user_data = read_data('../assert/good_user.json')
    response_post_user = user.post_user(user_data)

    log.debug("STEP 2. Check response status code equals 201.")
    assert response_post_user.status_code == 201, f'{response_post_user.json()}'

    log.debug("STEP 3. Update user name using PATCH request.")
    user_new_data = read_data('../assert/good_user_update_name.json')
    response_patch_user = user.patch_user(id_user=response_post_user.json()["id"], json=user_new_data)

    log.debug("STEP 4. Check response status code equals 200 and name is updated")
    assert response_patch_user.status_code == 200
    assert response_patch_user.json()['name'] == user_new_data['name']

    log.debug("STEP 5. Delete user using DELETE request.")
    response_delete_user = user.delete_user(id_user=response_patch_user.json()["id"])

    log.debug("STEP 6. Check response status code equals 204.")
    assert response_delete_user.status_code == 204
