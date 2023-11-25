from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
from hamcrest import *

class FormPage:

    CustomerNameField = (By.CSS_SELECTOR, 'input[name="custname"]')
    PhoneField = (By.CSS_SELECTOR, 'input[name="custtel"]')
    EmailField = (By.CSS_SELECTOR, 'input[name="custemail"]')
    SmallPizzaRadioButton = (By.CSS_SELECTOR, 'input[value="small"]')
    MediumPizzaRadioButton = (By.CSS_SELECTOR, 'input[value="medium"]')
    LargePizzaRadioButton = (By.CSS_SELECTOR, 'input[value="large"]')
    AddBaconCheckbox = (By.CSS_SELECTOR, 'input[value="bacon"]')
    AddExtraCheeseCheckbox = (By.CSS_SELECTOR, 'input[value="cheese"]')
    AddOnionCheckbox = (By.CSS_SELECTOR, 'input[value="onion"]')
    AddMushroomCheckbox = (By.CSS_SELECTOR, 'input[value="mushroom"]')
    DeliveryTimePicker = (By.CSS_SELECTOR, 'input[name="delivery"]')
    CommentField = (By.CSS_SELECTOR, 'textarea[name="comments"]')
    SubmitButton = (By.CSS_SELECTOR, 'button')
    JSONdata = (By.CSS_SELECTOR, 'pre')


    URL = 'https://httpbin.org/forms/post'
    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get(self.URL)

    def enterCustomerName(self, customerName):
        customerNameField = self.browser.find_element(*self.CustomerNameField)
        customerNameField.send_keys(customerName)

    def enterPhoneNumber(self, phoneNumber):
        phoneNumberField = self.browser.find_element(*self.PhoneField)
        phoneNumberField.send_keys(phoneNumber)

    def enterEmail(self, email):
        emailField = self.browser.find_element(*self.EmailField)
        emailField.send_keys(email)

    def selectSmallPizza(self):
        smallPizzaRadio = self.browser.find_element(*self.SmallPizzaRadioButton)
        smallPizzaRadio.click()

    def selectMediumPizza(self):
        mediumPizzaRadio = self.browser.find_element(*self.MediumPizzaRadioButton)
        mediumPizzaRadio.click()

    def selectLargePizza(self):
        largePizzaRadio = self.browser.find_element(*self.LargePizzaRadioButton)
        largePizzaRadio.click()

    def addBacon(self):
        addBacon = self.browser.find_element(*self.AddBaconCheckbox)
        addBacon.click()

    def addCheese(self):
        addCheese = self.browser.find_element(*self.AddExtraCheeseCheckbox)
        addCheese.click()

    def addOnion(self):
        addOnion = self.browser.find_element(*self.AddOnionCheckbox)
        addOnion.click()

    def addMushrooms(self):
        addMushrooms = self.browser.find_element(*self.AddMushroomCheckbox)
        addMushrooms.click()

    def enterDeliveryTime(self, deliveryTime):
        deliveryTimeField = self.browser.find_element(*self.DeliveryTimePicker)
        deliveryTimeField.send_keys(deliveryTime)

    def enterComment(self, comment):
        commentField = self.browser.find_element(*self.CommentField)
        commentField.send_keys(comment)

    def clickSublit(self):
        submitButton = self.browser.find_element(*self.SubmitButton)
        submitButton.click()

    def findJSON(self):
        data = self.browser.find_element(*self.JSONdata)
        json_data_as_text = data.text
        parsed_data = json.loads(json_data_as_text)
        return parsed_data

################################################

    def choosePizzaSize(self, size):
        if size == "Small":
            self.selectSmallPizza()
        elif size == "Medium":
            self.selectMediumPizza()
        elif size == "Large":
            self.selectLargePizza()
        else:
            raise Exception("The pizza size is not supported")

    def addToppings(self, addBacon, addCheese, addOnion, addMushroom):
        if addBacon == "bacon":
            self.addBacon()
        if addCheese == "cheese":
            self.addCheese()
        if addOnion == "onion":
            self.addOnion()
        if addMushroom == "mushrooms":
            self.addMushrooms()

#######################################

    def verifyName(self, name):
        assert_that(self.findJSON()["form"]["custname"], equal_to(name))

    def verifyPhone(self, phoneNumber):
        assert_that(self.findJSON()["form"]["custtel"], equal_to(phoneNumber))
    def verifyEmail(self, email):
        assert_that(self.findJSON()["form"]["custemail"], equal_to(email))
    def verifySize(self, size):
        assert_that(self.findJSON()["form"]["size"], equal_to(size.lower()))
    def verifyToppings(self, *arguments):
        tops = []
        for elem in arguments:
            if elem != "No":
                tops.append(elem)

        if len(tops) == 1:
            tops = tops[0]
        assert_that(self.findJSON()["form"]["topping"], equal_to(tops))
    def verifyTime(self, time):
        assert_that(self.findJSON()["form"]["delivery"], equal_to(time))
    def verifyComment(self, text):
        assert_that(self.findJSON()["form"]["comments"], equal_to(text))
    
