
class Loginpage1():

    def __init__(self, driver):

        self.driver = driver
        self.password = "//input[@name='password']"
        self.sign_in = "//input[@id='signInSubmit']"

    def password_textbox(self, password):
        self.driver.find_element_by_xpath(self.password).send_keys(password)

    def click_sign_in_button(self):
        self.driver.find_element_by_xpath(self.sign_in).click()

