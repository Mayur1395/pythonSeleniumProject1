import pytest


class Test1():
    @pytest.fixture()      # this fixture we can use for pre condition and in methods we pass the argument in this method name
    def test_setup(self):
        print("run before every method")

    def test_method1(self,test_setup):
        a = 5
        b = 6
        assert a+1 == b, "if not matched test case is failed"

    def test_method2(self,test_setup):
        name = "mayur"
        assert name == "ashwin", "if not matched test case is failed"




