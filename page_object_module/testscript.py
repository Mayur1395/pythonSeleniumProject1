import pytest

from page_object_module.baseclass import Baseclass
from page_object_module.homepage import Homepage
from page_object_module.loginpage import Loginpage
from page_object_module.loginpage1 import Loginpage1
from utils import utils as utils

# @pytest.mark.usefixtures("test_setup")   this statement we execute in our baseclass and baseclass inheriting in this

class Test_amazon(Baseclass):

    def test_sign(self):

        driver = self.driver
        home = Homepage(driver)
        home.click_sign_in()

    def test_login(self):
        #log =self.getlogger()
        driver = self.driver
        login = Loginpage(driver)
        login.username_textbox(utils.USERNAME)
        login.click_continue_button()

    def test_login1(self):
        driver = self.driver
        login1 = Loginpage1(driver)
        login1.password_textbox(utils.PASSWORD)
        login1.click_sign_in_button()
