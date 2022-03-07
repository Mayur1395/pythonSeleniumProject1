import pytest
from selenium import webdriver


from pro_page.homepage import homepage
from pro_page.loginpage import loginpage
from pro_page.dashboard import dashboard
from pro_utils import utils as utils

@pytest.mark.usefixtures("test_setup")
class Testdemo:
    @pytest.fixture(scope="class")
    def test_setup(self):
        from selenium import webdriver
        global driver

        driver = webdriver.Chrome(
            executable_path="C:\\Users\\mayur.pardeshi\\PycharmProjects\\pythonSeleniumProject1""\\pro_drivers\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)

        yield
        driver.close()
        driver.quit()
        print("test completed")

    def test_homepage(self):

        driver.get(utils.URL)
        h1 = homepage(driver)
        h1.test_click_login_button()

    def test_loginpage(self):

        l1 = loginpage(driver)
        l1.test_enter_username(utils.USERNAME)
        l1.test_enter_password(utils.PASSWORD)
        l1.test_click_login_button()

    def test_dashboard(self):


        d1 = dashboard(driver)
        d1.test_text_profile_button()
