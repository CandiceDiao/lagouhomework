import pytest
import yaml

@pytest.mark.parametrize(("a","b"), yaml.safe_load(open("./data_cal")))
class TestCal:
    def test_add(self,creatCal,a,b):
        assert a + b == creatCal.add(a,b)

    def test_sub(self,creatCal,a,b):
        assert a - b == creatCal.sub(a,b)

    def test_mul(self,creatCal,a,b):
        assert a * b ==creatCal.mul(a,b)

    def test_div(self,creatCal,a,b):
        try:
            a / b
        except ZeroDivisionError:
            assert False
        else:
            assert a / b == creatCal.div(a, b)


