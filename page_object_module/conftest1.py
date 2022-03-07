from utils import utils as utils
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"  # in that we store our default browser is chrome
    )

@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\webdriver\\chromedriver.exe")#
        driver.get(utils.URL)
        driver.implicitly_wait(10)
        driver.maximize_window()
    elif browser_name == "firefox":   # elif means else if
        # we are using this to run our script in command propmt using firefox browser name and similar use to any other browser

        driver = webdriver.Chrome(executable_path="C:\\webdriver\\geckodriver.exe")
        driver.get(utils.URL)
        driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.close()
    print("test completed")

