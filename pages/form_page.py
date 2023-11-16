from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class FormPage:

    CustomerNameField = (By.CSS_SELECTOR, 'input[name="custname"]')
    TelephoneField = (By.CSS_SELECTOR, 'input[name="custtel"]')
    EmailField = (By.CSS_SELECTOR, 'input[name="custemail"]')
    SmallPizzaRadioButton = (By.CSS_SELECTOR, 'input[value="small"]')
    MediumPizzaRadioButton = (By.CSS_SELECTOR, 'input[value="medium"]')
    LargePizzaRadioButton = (By.CSS_SELECTOR, 'input[value="large"]')
    PizzaBaconCheckbox = (By.CSS_SELECTOR, 'input[value="bacon"]')
    PizzaExtraCheeseCheckbox = (By.CSS_SELECTOR, 'input[value="cheese"]')
    PizzaOnionCheckbox = (By.CSS_SELECTOR, 'input[value="onion"]')
    PizzaMushroomCheckbox = (By.CSS_SELECTOR, 'input[value="mushroom"]')
    DeliveryTimePicker = (By.CSS_SELECTOR, 'input[name="delivery"]')
    CommentField = (By.CSS_SELECTOR, 'input[name="comments"]')
    SubmitButton = (By.CSS_SELECTOR, 'button')


    URL = 'https://httpbin.org/forms/post'
    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get(self.URL)

    def enterCustomerName(self, customerName):
        customerNameField = self.browser.find_element(*self.CustomerNameField)
        customerNameField.send_keys(customerName)
