from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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
        if addBacon == "Yes":
            self.addBacon()
        if addCheese == "Yes":
            self.addCheese()
        if addOnion == "Yes":
            self.addOnion()
        if addMushroom == "Yes":
            self.addMushrooms()

