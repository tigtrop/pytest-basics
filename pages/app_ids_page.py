import requests
import json
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from hamcrest import *
from pages.db_page import DB_Page
class App_Ids_Page(DB_Page):
    def verifySchema(self):
        json_page = self.findJSON()

        for elem in json_page:
            assert_that(elem["id"])
