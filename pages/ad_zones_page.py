import requests
from hamcrest import *
from pages.db_page import DB_Page
from functools import wraps
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def check_status_code(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)

        assert_that(response.status_code, any_of(equal_to(201), equal_to(200)))

        return response

    return wrapper
class Ad_zones_page(DB_Page):

    ad_zones_endpoint = 'IlyaKnysh/fake_db/ad_zones?'
    headers = {'Content-Type' : 'application/json', 'accept-encoding': 'gzip, deflate', 'Connection': 'keep-alive', 'cache-control': 'no-cache'}
    def verifySchema(self):
        json_page = self.findJSON()

        for elem in json_page:
            assert_that(list(elem.keys()), equal_to(['id', 'zone', 'type']))

    @check_status_code
    def post_new_zone(self):
        obj = {
                "id": 11111,
                "zone": "intersitial",
                "type": "interstitial_rewarded_video"
                }
        logger.info(f"Sending POST request to {self.base_url + self.ad_zones_endpoint} with JSON: {obj}")
        response = requests.post(self.base_url + self.ad_zones_endpoint, headers=self.headers, json=obj)
        logger.info(f"Received response: {response.text}")

        return response

