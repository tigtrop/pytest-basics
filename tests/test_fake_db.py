import pytest
import requests

from pages.db_page import DB_Page
from pages.db_info_page import DB_info_Page

db_page = DB_Page()
db_info_page = DB_info_Page()

@pytest.fixture
def setup_test():
    db_page.open()
    yield
def test_db_info(setup_test):
    db_page.verify_db_name()

    db_page.click_db_info()

    db_info_page.verify_db_name()
    db_info_page.verify_db_creator()

def test_app_ids_badge(setup_test):
    db_page.verifyElementCount(db_page.APP_IDS_LINK)

def test_ad_zones_badge(setup_test):
    db_page.verifyElementCount(db_page.AD_ZONES_LINK)

def test_network_link_badge(setup_test):
    db_page.verifyElementCount(db_page.NETWORKS_LINK)

def test_ad_zones_type(setup_test):
    db_page.verifyElementType(db_page.AD_ZONES_LINK)

def test_db_info_type(setup_test):
    db_page.verifyElementType(db_page.DB_INFO_LINK)



# def test_get():
#     # requests.get(DB_Page.base_url + DB_Page.db, headers=DB_Page.headers)
#     response = db_page.get_db_structure()
#     print(response.text)
