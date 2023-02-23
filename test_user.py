from read_with_json_file import read_data


def test_get_user_by_id(api_client, base_url):
    endpoint = '/users'
    response = api_client.get(url=base_url + endpoint, params={'page': 1, 'id': 577270})
    assert response.status_code == 200, response.json()


def test_post_user_auto_delete(post_user_auto_delete):
    user = read_data('assert/good_user.json')
    assert post_user_auto_delete.status_code == 201, post_user_auto_delete.json()
    assert post_user_auto_delete.json()['name'] == user['name'], post_user_auto_delete.json()
    assert post_user_auto_delete.json()['email'] == user['email'], post_user_auto_delete.json()
    assert post_user_auto_delete.json()['gender'] == user['gender'], post_user_auto_delete.json()
    assert post_user_auto_delete.json()['status'] == user['status'], post_user_auto_delete.json()


class TestCreateEditDeleteUser:

    def test_post_user(self, api_client, base_url, global_var):
        user = read_data('assert/good_user.json')
        endpoint = '/users'
        response = api_client.post(url=base_url + endpoint, json=user)
        global_var['client_id'] = response.json()['id']
        assert response.status_code == 201, f'{response.json()}'
        assert response.json()['name'] == user['name'], response.json()
        assert response.json()['email'] == user['email'], response.json()
        assert response.json()['gender'] == user['gender'], response.json()
        assert response.json()['status'] == user['status'], response.json()

    def test_post_existed_user(self, api_client, base_url):
        user = read_data('assert/good_user.json')
        endpoint = '/users'
        response = api_client.post(url=base_url + endpoint, json=user)
        assert response.status_code == 422
        assert response.json()[0]['message'] == 'has already been taken'

    def test_patch_user_name(self, api_client, base_url, global_var):
        user = read_data('assert/good_user_update_name.json')
        endpoint = '/users'
        url = f'{base_url}{endpoint}/{global_var["client_id"]}'
        response = api_client.patch(url=url, json=user)
        assert response.status_code == 200
        assert response.json()['name'] == user['name']

    def test_delete_user(self, api_client, base_url, global_var):
        endpoint = '/users'
        url = f'{base_url}{endpoint}/{global_var["client_id"]}'
        response = api_client.delete(url=url)
        assert response.status_code == 204


class TestCreateUser:

    def test_email_id_without_at_sign(self, api_client, base_url, global_var):
        user = read_data("assert/user_email_id_without_at_sign.json")
        endpoint = '/users'
        response = api_client.post(url=base_url + endpoint, json=user)
        assert response.status_code == 422, f'user data: {response.json()}'
        assert response.json()[0]['message'] == 'is invalid'

    def test_email_id_without_domain_name(self, api_client, base_url, global_var):
        user = read_data("assert/user_email_id_without_domain_name.json")
        endpoint = '/users'
        response = api_client.post(url=base_url + endpoint, json=user)
        assert response.status_code == 422, f'user data: {response.json()}'
        assert response.json()[0]['message'] == 'is invalid'

    def test_email_id_without_top_level_domain(self, api_client, base_url, global_var):
        user = read_data("assert/user_email_id_without_top_level_domain.json")
        endpoint = '/users'
        response = api_client.post(url=base_url + endpoint, json=user)
        assert response.status_code == 422, f'user data: {response.json()}'
        assert response.json()[0]['message'] == 'is invalid'

    def test_email_id_with_special_symbol(self, api_client, base_url, global_var):
        user = read_data("assert/user_email_id_with_special_symbol.json")
        endpoint = '/users'
        response = api_client.post(url=base_url + endpoint, json=user)
        assert response.status_code == 422, f'user data: {response.json()}'
        assert response.json()[0]['message'] == 'is invalid'

    def test_email_id_with_multiple_at_signs(self, api_client, base_url, global_var):
        user = read_data("assert/user_email_id_with_multiple_at_signs.json")
        endpoint = '/users'
        response = api_client.post(url=base_url + endpoint, json=user)
        assert response.status_code == 422, f'user data: {response.json()}'
        assert response.json()[0]['message'] == 'is invalid'

    def test_email_id_with_local_part(self, api_client, base_url, global_var):
        user = read_data("assert/user_email_id_with_local_part.json")
        endpoint = '/users'
        response = api_client.post(url=base_url + endpoint, json=user)
        assert response.status_code == 422, f'user data: {response.json()}'
        assert response.json()[0]['message'] == 'is invalid'

    def test_email_id_start_with_a_dot(self, api_client, base_url, global_var):
        user = read_data("assert/user_email_id_start_with_a_dot.json")
        endpoint = '/users'
        response = api_client.post(url=base_url + endpoint, json=user)
        assert response.status_code == 422, f'user data: {response.json()}'
        assert response.json()[0]['message'] == 'is invalid'

    def test_email_id_local_part_ends_with_a_dot(self, api_client, base_url, global_var):
        user = read_data("assert/user_email_id_local_part_ends_with_a_dot.json")
        endpoint = '/users'
        response = api_client.post(url=base_url + endpoint, json=user)
        assert response.status_code == 422, f'user data: {response.json()}'
        assert response.json()[0]['message'] == 'is invalid'

    def test_email_id_with_multiple_dots(self, api_client, base_url, global_var):
        user = read_data("assert/user_email_id_with_multiple_dots.json")
        endpoint = '/users'
        response = api_client.post(url=base_url + endpoint, json=user)
        assert response.status_code == 422, f'user data: {response.json()}'
        assert response.json()[0]['message'] == 'is invalid'

    def test_email_id_local_part_with_a_pass(self, api_client, base_url, global_var):
        user = read_data("assert/user_email_id_local_part_with_a_pass.json")
        endpoint = '/users'
        response = api_client.post(url=base_url + endpoint, json=user)
        assert response.status_code == 422, f'user data: {response.json()}'
        assert response.json()[0]['message'] == 'is invalid'

    def test_email_id_domain_part_with_a_pass(self, api_client, base_url, global_var):
        user = read_data("assert/user_email_id_domain_part_with_a_pass.json")
        endpoint = '/users'
        response = api_client.post(url=base_url + endpoint, json=user)
        assert response.status_code == 422, f'user data: {response.json()}'
        assert response.json()[0]['message'] == 'is invalid'

    def test_without_email_field(self, api_client, base_url, global_var):
        user = read_data("assert/user_without_email_field.json")
        endpoint = '/users'
        response = api_client.post(url=base_url + endpoint, json=user)
        assert response.status_code == 422, f'user data: {response.json()}'
        assert response.json()[0]['message'] == 'is invalid'
