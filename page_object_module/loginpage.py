

class Loginpage():

    def __init__(self, driver):

        self.driver = driver
        self.username = "//input[@name='email']"
        self.continue_button = "//input[@id='continue']"

    def username_textbox(self, username):
        self.driver.find_element_by_xpath(self.username).send_keys(username)

    def click_continue_button(self):
        self.driver.find_element_by_xpath(self.continue_button).click()


