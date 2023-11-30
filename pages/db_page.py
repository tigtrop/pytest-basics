import requests
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class DB_Page:

    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    base_url = 'https://my-json-server.typicode.com/'
    db_endpoint = 'IlyaKnysh/fake_db/db?'
    db_ui = 'IlyaKnysh/fake_db'
    headers = {'accept-encoding': 'gzip, deflate', 'Connection': 'keep-alive', 'cache-control': 'no-cache'}

    DB_TITLE = (By.CSS_SELECTOR, 'h3 a[href="https://github.com/IlyaKnysh/fake_db"]')
    DB_CREATOR = (By.CSS_SELECTOR, 'h5 a')
    DB_INFO_LINK = (By.CSS_SELECTOR, 'a[href="/IlyaKnysh/fake_db/db_info"]')
    APP_IDS_LINK = (By.CSS_SELECTOR, 'a[href="/IlyaKnysh/fake_db/app_ids"]')
    AD_ZONES_LINK = (By.CSS_SELECTOR, 'a[href="/IlyaKnysh/fake_db/ad_zones"]')
    NETWORKS_LINK = (By.CSS_SELECTOR, 'a[href="/IlyaKnysh/fake_db/networks"]')

    def open(self):
        self.browser.get(self.base_url + self.db_ui)
    def get_db_structure(self):
        response = requests.get(self.base_url + self.db_endpoint, headers=self.headers)
        return response

