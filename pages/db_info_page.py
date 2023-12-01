import requests
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from hamcrest import *

from pages.db_page import DB_Page
class DB_info_Page:

    db_page = DB_Page()
    def verify_db_name(self):

        json_page = self.db_page.findJSON()
        db_structure = self.db_page.get_db_structure()

        assert_that(json_page["db_name"], equal_to(db_structure["db_info"]["db_name"]))

    def verify_db_creator(self):

        json_page = self.db_page.findJSON()
        db_structure = self.db_page.get_db_structure()

        assert_that(json_page["author"], equal_to(db_structure["db_info"]["author"]))