import pytest
import requests

from pages.db_page import DB_Page

db_page = DB_Page()

def test_ui():
    db_page.open()

# def test_get():
#     # requests.get(DB_Page.base_url + DB_Page.db, headers=DB_Page.headers)
#     response = db_page.get_db_structure()
#     print(response.text)
