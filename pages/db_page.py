import requests
import pytest

class DB_Page:

    base_url = 'https://my-json-server.typicode.com/'
    db = 'IlyaKnysh/fake_db'
    headers = {'accept-encoding': 'gzip, deflate', 'Connection': 'keep-alive', 'cache-control': 'no-cache'}

    def get_response(self):
        response = requests.get(self.base_url + self.db, headers=self.headers)
        return response

