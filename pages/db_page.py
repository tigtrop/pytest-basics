import requests
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



class DB_Page:

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    base_url = 'https://my-json-server.typicode.com/'
    db_endpoint = 'IlyaKnysh/fake_db/db?'
    db_ui = 'IlyaKnysh/fake_db'
    headers = {'accept-encoding': 'gzip, deflate', 'Connection': 'keep-alive', 'cache-control': 'no-cache'}

    # def __init__(self, self.driver):
    #     self.browser = browser

    def open(self):
        self.driver.get(self.base_url + self.db_ui)
    def get_db_structure(self):
        response = requests.get(self.base_url + self.db_endpoint, headers=self.headers)
        return response

