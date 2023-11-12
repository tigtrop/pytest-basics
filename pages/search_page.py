from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SearchPage:

    SEARCH_INPUT = (By.ID, 'searchbox_input')

    URL = 'https://duckduckgo.com/'
    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)