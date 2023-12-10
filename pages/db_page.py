import requests
import json
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from hamcrest import *

class DB_Page:

    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    base_url = 'https://my-json-server.typicode.com/'
    db_endpoint = 'IlyaKnysh/fake_db/db?'
    db_ui = 'IlyaKnysh/fake_db'
    headers = {'accept-encoding': 'gzip, deflate', 'Connection': 'keep-alive', 'cache-control': 'no-cache'}

    DB_TITLE = (By.CSS_SELECTOR, 'h3 a[href="https://github.com/IlyaKnysh/fake_db"]')
    DB_CREATOR = (By.CSS_SELECTOR, 'h5 a')
    DB_INFO_LINK = (By.CSS_SELECTOR, 'a[href="/IlyaKnysh/fake_db/db_info"]')
    DB_INFO_BADGE = (By.CSS_SELECTOR, DB_INFO_LINK[1] + '+sup')
    APP_IDS_LINK = (By.CSS_SELECTOR, 'a[href="/IlyaKnysh/fake_db/app_ids"]')
    APP_IDS_BADGE = (By.CSS_SELECTOR, APP_IDS_LINK[1] + '+sup')
    AD_ZONES_LINK = (By.CSS_SELECTOR, 'a[href="/IlyaKnysh/fake_db/ad_zones"]')
    AD_ZONES_BADGE = (By.CSS_SELECTOR, AD_ZONES_LINK[1] + '+sup')
    NETWORKS_LINK = (By.CSS_SELECTOR, 'a[href="/IlyaKnysh/fake_db/networks"]')
    NETWORKS_BADGE = (By.CSS_SELECTOR, NETWORKS_LINK[1] + '+sup')
    JSONdata = (By.CSS_SELECTOR, 'pre')

    def open(self):
        self.browser.get(self.base_url + self.db_ui)

    def refresh(self):
        self.browser.refresh()
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

    def click_app_ids(self):
        app_ids_link = self.browser.find_element(*self.APP_IDS_LINK)
        app_ids_link.click()

    def click_ad_zones(self):
        ad_zones_link = self.browser.find_element(*self.AD_ZONES_LINK)
        ad_zones_link.click()

    def click_networks(self):
        networks_link = self.browser.find_element(*self.NETWORKS_LINK)
        networks_link.click()

    def verify_db_name(self):
        db_structure = self.get_db_structure()
        db_name = self.browser.find_element(*self.DB_TITLE).text

        assert_that(db_name, equal_to(db_structure["db_info"]["db_name"]))

    def verifyElementCount(self, linkSelector):
        link = self.browser.find_element(*linkSelector)
        badge = self.browser.find_element(By.CSS_SELECTOR,linkSelector[1] + '+ sup')
        badgeNumber = badge.text

        link.click()

        json_page = self.findJSON()

        assert_that(int(badgeNumber), equal_to(len(json_page)))

    def verifyElementType(self, linkSelector):
        link = self.browser.find_element(*linkSelector)
        badge = self.browser.find_element(By.CSS_SELECTOR, linkSelector[1] + '+ sup')
        badgeType = type(badge.text)
        badgeText = badge.text
        link.click()

        json_page = self.findJSON()
        if type(dict()) == type(json_page):
            assert_that(badgeText, equal_to('object'))
        else:
            assert_that(int(badgeText), equal_to(len(json_page)))

    def checkBadgeValue(self, badgeSelector):
        badge = self.browser.find_element(*badgeSelector)
        return badge.text



