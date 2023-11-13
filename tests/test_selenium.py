import pytest
import selenium.webdriver

from pages.search_page import SearchPage

def test_basic_search(browser):
    search_page = SearchPage(browser)

    PHRASE = 'google'

    search_page.open()

    search_page.search(PHRASE)