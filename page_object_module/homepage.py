


class Homepage():

    def __init__(self,driver):
        self.driver = driver

        self.sign_in = "//span[text()='Hello, Sign in']"

    def click_sign_in(self):
        self.driver.find_element_by_xpath(self.sign_in).click()









