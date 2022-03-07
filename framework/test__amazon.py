import pytest
from selenium import webdriver


class Test_amazon():
    @pytest.fixture()

    def test_setup(self):
        global driver

        driver = webdriver.Chrome(executable_path="C:\\webdriver\\chromedriver.exe")
        driver.get("https://www.amazon.in/")
        driver.implicitly_wait(10)
        driver.maximize_window()
        print("run before every method")
        #driver.get_screenshot_as_file("C:\\Users\\mayur.pardeshi\\PycharmProjects\\pythonSeleniumProject1\\screenshot\\homepage.jpg")
        yield
        driver.close()
        print("test completed")

    def test_login(self, test_setup):
        driver.find_element_by_xpath("//span[text()='Hello, Sign in']").click()
        driver.find_element_by_xpath("//input[@name='email']").send_keys(8669059022)
        driver.find_element_by_xpath("//input[@id='continue']").click()
        t1 = driver.title
        assert t1 == "Amazon Sign In","test case is passed"
        print("run method a")
