import requests
from hamcrest import *
from pages.db_page import DB_Page
class Ad_zones_page(DB_Page):

    ad_zones_endpoint = 'IlyaKnysh/fake_db/ad_zones?'
    headers = {'Content-Type' : 'application/json', 'accept-encoding': 'gzip, deflate', 'Connection': 'keep-alive', 'cache-control': 'no-cache'}
    def verifySchema(self):
        json_page = self.findJSON()

        for elem in json_page:
            assert_that(list(elem.keys()), equal_to(['id', 'zone', 'type']))

    def post_new_zone(self):
        obj = {
                "id": 11111,
                "zone": "intersitial",
                "type": "interstitial_rewarded_video"
                }

        response = requests.post(self.base_url + self.ad_zones_endpoint, headers=self.headers, json=obj)
        assert_that(response.status_code, equal_to(201))

