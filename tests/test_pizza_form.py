import pytest
import selenium.webdriver
import time
import json

from pages.form_page import FormPage
@pytest.mark.parametrize('customer_name, phone, email, size, addBacon, addCheese, addOnion, addMushroom, deliveryTime, comment',
                         [('David', '09933165847', 'mail@test.com', 'Small', 'Yes', 'No', 'No', 'No', '13:00', 'Faster please')])
def test_form_check(browser, customer_name, phone, email, size, addBacon, addOnion, addCheese, addMushroom, deliveryTime, comment):
    form_page = FormPage(browser)

    form_page.open()

    form_page.enterCustomerName(customer_name)

    form_page.enterPhoneNumber(phone)

    form_page.enterEmail(email)

    form_page.choosePizzaSize(size)

    form_page.addToppings(addBacon,addCheese,addOnion,addMushroom)

    form_page.enterDeliveryTime(deliveryTime)

    form_page.enterComment(comment)

    form_page.clickSublit()



    time.sleep(10)
