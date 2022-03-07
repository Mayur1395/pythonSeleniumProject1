
class homepage:

    def __init__(self,driver):
        self.driver = driver

        self.click_login = "//a[text()='Log in']"

    def test_click_login_button(self):
        self.driver.find_element_by_xpath(self.click_login).click()




