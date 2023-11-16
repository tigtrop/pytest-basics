import pytest
import selenium.webdriver
import time

from pages.form_page import FormPage

def test_form_check(browser):
    form_page = FormPage(browser)

    customer_name = "Kendro"

    form_page.open()

    form_page.enterCustomerName(customer_name)
    time.sleep(10)
