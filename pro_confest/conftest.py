import pytest


@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver

    driver = webdriver.Chrome(executable_path="C:\\Users\\mayur.pardeshi\\PycharmProjects\\pythonSeleniumProject1""\\pro_drivers\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver
    yield
    driver.close()
    driver.quit()
    print("test completed")
