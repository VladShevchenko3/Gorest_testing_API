import requests


class Api:

    def __init__(self, base_url, base_headers):
        self.base_url = base_url
        self.base_headers = base_headers

    def do_request(self, method, endpoint=None, headers=None, json=None, params=None):
        if headers is not None:
            self.base_headers.update(headers)
        return requests.request(method=method, url=self.base_url + str(endpoint or ""), json=json,
                                headers=self.base_headers, params=params)
