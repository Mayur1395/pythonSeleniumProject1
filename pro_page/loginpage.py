

class loginpage:

    def __init__(self,driver):
        self.driver = driver

        self.username_textbox = "//input[@id='user_login']"
        self.password_textbox = "//input[@id='user_pass']"
        self.click_button = "//input[@id='wp-submit']"

    def test_enter_username(self, username):
        self.driver.find_element_by_xpath(self.username_textbox).send_keys(username)

    def test_enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox).send_keys(password)

    def test_click_login_button(self):
        self.driver.find_element_by_xpath(self.click_button).click()







