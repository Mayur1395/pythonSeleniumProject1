import pytest


class Test2:

    @pytest.fixture()
    def test_setup1(self):
        print("run before every method")
        yield                            # this keyword we can use after method run
        print("run after every method")

    def test_method1(self,test_setup1):
        s1 = "mayur"
        s2 = "mayur"
        assert s1 == s2, "if not matched test case is failed"

    def test_method2(self,test_setup1):
        a = 8
        b = 9
        assert a + b == 17, "if not matched test case is failed"
