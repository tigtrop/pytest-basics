from hamcrest import *
from pages.db_page import DB_Page
class Networks_page(DB_Page):
    def verifySchema(self):
        json_page = self.findJSON()

        for elem in json_page:
            assert_that(list(elem.keys()), equal_to(['name', 'types']))