import requests
import json
import pytest
from selenium.webdriver.common.by import By
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
    JSONdata = (By.CSS_SELECTOR, 'pre')

    def open(self):
        self.browser.get(self.base_url + self.db_ui)
    def get_db_structure(self):
        response = requests.get(self.base_url + self.db_endpoint, headers=self.headers)
        return response.json()

    def findJSON(self):
        data = self.browser.find_element(*self.JSONdata)
        json_data_as_text = data.text
        parsed_data = json.loads(json_data_as_text)
        return parsed_data

    def click_db_info(self):
        db_info_link = self.browser.find_element(*self.DB_INFO_LINK)
        db_info_link.click()

