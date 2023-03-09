from Api import Api


class User:
    base_url = 'https://gorest.co.in/public/v2/users'
    bearer = 'a28db959a3da8d6d9a137120dd6c585e2cce6254441b4017fc3dd915300a38e3'
    base_headers = {'Authorization': f'Bearer {bearer}', "accept": "application/json",
                    "Content-Type": "application/json"}

    def __init__(self):
        self.api = Api(self.base_url, self.base_headers)

    def get_user(self, params):
        return self.api.do_request(method="GET", params=params)

    def post_user(self, json):
        return self.api.do_request(method="POST", json=json)

    def delete_user(self, id_user):
        return self.api.do_request(method="DELETE", endpoint=f'/{id_user}')

    def patch_user(self, id_user, json):
        return self.api.do_request(method="PATCH", endpoint=f'/{id_user}', json=json)
