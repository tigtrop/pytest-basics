import pytest
from hamcrest import *
import requests

from pages.db_page import DB_Page
from pages.db_info_page import DB_info_Page
from pages.app_ids_page import App_Ids_Page
from pages.ad_zones_page import Ad_zones_page
from pages.networks_page import Networks_page

db_page = DB_Page()
db_info_page = DB_info_Page()
app_ids_page = App_Ids_Page()
ad_zones_page = Ad_zones_page()
networks_page = Networks_page()

@pytest.fixture
def setup_test():
    db_page.open()
    yield
def test_db_info(setup_test):
    db_page.verify_db_name()

    db_page.click_db_info()

    db_info_page.verify_db_name()
    db_info_page.verify_db_creator()

def test_app_ids_count(setup_test):
    db_page.verifyElementCount(db_page.APP_IDS_LINK)

def test_ad_zones_count(setup_test):
    db_page.verifyElementCount(db_page.AD_ZONES_LINK)

def test_network_link_count(setup_test):
    db_page.verifyElementCount(db_page.NETWORKS_LINK)

def test_db_info_badge(setup_test):
    db_page.verifyElementType(db_page.DB_INFO_LINK)

def test_app_ids_badge(setup_test):
    db_page.verifyElementType(db_page.APP_IDS_LINK)

def test_ad_zones_badge(setup_test):
    db_page.verifyElementType(db_page.AD_ZONES_LINK)

def test_network_badge(setup_test):
    db_page.verifyElementType(db_page.NETWORKS_LINK)

def test_app_ids_schema(setup_test):
    db_page.click_app_ids()
    app_ids_page.verifySchema()

def test_ad_zones_schema(setup_test):
    db_page.click_ad_zones()
    ad_zones_page.verifySchema()

def test_networks_schema(setup_test):
    db_page.click_networks()
    networks_page.verifySchema()

def test_add_new_zone(setup_test):
    badgeValueBefore  = int(db_page.checkBadgeValue(db_page.AD_ZONES_BADGE))

    ad_zones_page.post_new_zone()

    db_page.refresh()
    badgeValueAfter = int(db_page.checkBadgeValue(db_page.AD_ZONES_BADGE))
    assert_that(badgeValueBefore+1, equal_to(badgeValueAfter))

    db_page.verifyElementCount(db_page.AD_ZONES_LINK)




# def test_get():
#     # requests.get(DB_Page.base_url + DB_Page.db, headers=DB_Page.headers)
#     response = db_page.get_db_structure()
#     print(response.text)
