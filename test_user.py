from read_with_json_file import read_data


def test_get_user_by_id(user):
    response = user.get_user(params={'page': 1, 'id': 892051})
    assert response.status_code == 200, response.json()


def test_post_user_auto_delete(post_user_auto_delete):
    user = read_data('assert/good_user.json')
    assert post_user_auto_delete.status_code == 201, post_user_auto_delete.json()
    assert post_user_auto_delete.json()['name'] == user['name'], post_user_auto_delete.json()
    assert post_user_auto_delete.json()['email'] == user['email'], post_user_auto_delete.json()
    assert post_user_auto_delete.json()['gender'] == user['gender'], post_user_auto_delete.json()
    assert post_user_auto_delete.json()['status'] == user['status'], post_user_auto_delete.json()


def test_post_existed_user(user):
    user_data = read_data('assert/good_user.json')
    response_post_user = user.post_user(user_data)
    assert response_post_user.status_code == 201, f'{response_post_user.json()}'
    response_post_existed_user = user.post_user(user_data)
    assert response_post_existed_user.status_code == 422
    assert response_post_existed_user.json()[0]['message'] == 'has already been taken'
    user.delete_user(id_user=response_post_user.json()["id"])
    assert response.status_code == 204


def test_patch_user_name(user):
    user_data = read_data('assert/good_user.json')
    response_post_user = user.post_user(user_data)
    assert response_post_user.status_code == 201, f'{response_post_user.json()}'
    user_new_data = read_data('assert/good_user_update_name.json')
    response_patch_user = user.patch_user(id_user=response_post_user.json()["id"], json=user_new_data)
    assert response_patch_user.status_code == 200
    assert response_patch_user.json()['name'] == user_new_data['name']
    user.delete_user(id_user=response_patch_user.json()["id"])
    assert response.status_code == 204


def test_delete_user(user):
    user_data = read_data('assert/good_user.json')
    response_post_user = user.post_user(user_data)
    assert response_post_user.status_code == 201, f'{response_post_user.json()}'
    response = user.delete_user(id_user=response_post_user.json()["id"])
    assert response.status_code == 204


def test_email_id_without_at_sign(user):
    user_data = read_data("assert/user_email_id_without_at_sign.json")
    response = user.post_user(json=user_data)
    assert response.status_code == 422, f'user data: {response.json()}'
    assert response.json()[0]['message'] == 'is invalid'


def test_email_id_without_domain_name(user):
    user_data = read_data("assert/user_email_id_without_domain_name.json")
    response = user.post_user(json=user_data)
    assert response.status_code == 422, f'user data: {response.json()}'
    assert response.json()[0]['message'] == 'is invalid'


def test_email_id_without_top_level_domain(user):
    user_data = read_data("assert/user_email_id_without_top_level_domain.json")
    response = user.post_user(json=user_data)
    assert response.status_code == 422, f'user data: {response.json()}'
    assert response.json()[0]['message'] == 'is invalid'


def test_email_id_with_special_symbol(user):
    user_data = read_data("assert/user_email_id_with_special_symbol.json")
    response = user.post_user(json=user_data)
    assert response.status_code == 422, f'user data: {response.json()}'
    assert response.json()[0]['message'] == 'is invalid'


def test_email_id_with_multiple_at_signs(user):
    user_data = read_data("assert/user_email_id_with_multiple_at_signs.json")
    response = user.post_user(json=user_data)
    assert response.status_code == 422, f'user data: {response.json()}'
    assert response.json()[0]['message'] == 'is invalid'


def test_email_id_with_local_part(user):
    user_data = read_data("assert/user_email_id_with_local_part.json")
    response = user.post_user(json=user_data)
    assert response.status_code == 422, f'user data: {response.json()}'
    assert response.json()[0]['message'] == 'is invalid'


def test_email_id_start_with_a_dot(user):
    user_data = read_data("assert/user_email_id_start_with_a_dot.json")
    response = user.post_user(json=user_data)
    assert response.status_code == 422, f'user data: {response.json()}'
    assert response.json()[0]['message'] == 'is invalid'


def test_email_id_local_part_ends_with_a_dot(user):
    user_data = read_data("assert/user_email_id_local_part_ends_with_a_dot.json")
    response = user.post_user(json=user_data)
    assert response.status_code == 422, f'user data: {response.json()}'
    assert response.json()[0]['message'] == 'is invalid'


def test_email_id_with_multiple_dots(user):
    user_data = read_data("assert/user_email_id_with_multiple_dots.json")
    response = user.post_user(json=user_data)
    assert response.status_code == 422, f'user data: {response.json()}'
    assert response.json()[0]['message'] == 'is invalid'


def test_email_id_local_part_with_a_pass(user):
    user_data = read_data("assert/user_email_id_local_part_with_a_pass.json")
    response = user.post_user(json=user_data)
    assert response.status_code == 422, f'user data: {response.json()}'
    assert response.json()[0]['message'] == 'is invalid'


def test_email_id_domain_part_with_a_pass(user):
    user_data = read_data("assert/user_email_id_domain_part_with_a_pass.json")
    response = user.post_user(json=user_data)
    assert response.status_code == 422, f'user data: {response.json()}'
    assert response.json()[0]['message'] == 'is invalid'


def test_without_email_field(user):
    user_data = read_data("assert/user_without_email_field.json")
    response = user.post_user(json=user_data)
    assert response.status_code == 422, f'user data: {response.json()}'
    assert response.json()[0]['message'] == 'is invalid'
