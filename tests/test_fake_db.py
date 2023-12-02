import pytest
import requests

from pages.db_page import DB_Page
from pages.db_info_page import DB_info_Page

db_page = DB_Page()
db_info_page = DB_info_Page()

def test_db_info():
    db_page.open()

    db_page.verify_db_name()

    db_page.click_db_info()

    db_info_page.verify_db_name()
    db_info_page.verify_db_creator()

def test_app_ids_badge():
    db_page.open()

    db_page.verifyElementCount(db_page.APP_IDS_LINK)

def test_ad_zones_badge():
    db_page.open()

    db_page.verifyElementCount(db_page.AD_ZONES_LINK)

def test_ad_zones_badge():
    db_page.open()

    db_page.verifyElementCount(db_page.NETWORKS_LINK)




# def test_get():
#     # requests.get(DB_Page.base_url + DB_Page.db, headers=DB_Page.headers)
#     response = db_page.get_db_structure()
#     print(response.text)
