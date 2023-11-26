import pytest
import csv

from pages.form_page import FormPage

def read_csv():
    with open('../test_data.csv') as csvfile:
        csvreader = csv.reader(csvfile)

        rows = []
        for row in csvreader:
            rows.append(row)
        return rows

@pytest.mark.parametrize('customer_name, phone, email, size, addBacon, addCheese, addOnion, addMushroom, deliveryTime, comment',
                         read_csv())
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

    form_page.verifyName(customer_name)

    form_page.verifyPhone(phone)

    form_page.verifyEmail(email)

    form_page.verifySize(size)

    form_page.verifyToppings(addBacon, addCheese, addOnion, addMushroom)

    form_page.verifyComment(comment)

    form_page.verifyTime(deliveryTime)