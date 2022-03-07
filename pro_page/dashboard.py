class dashboard:

    def __init__(self, driver):
        self.driver = driver

        self.text_profile = "//a[text()='Howdy, '] "

    def test_text_profile_button(self):
        s1 = self.driver.find_element_by_xpath(self.text_profile).text

        assert "Howdy, opensourcecms" == s1
