import pytest
import yaml



def test_option(cmdoption):
    print(f"{cmdoption}")

@pytest.mark.parametrize(("a","b"), yaml.safe_load(open("./data_cal")))
class TestCal:

    @pytest.mark.run(order=3)
    @pytest.mark.dependency(name='mul')
    def check_mul(self,creatCal,a,b):
        assert a * b ==creatCal.mul(a,b)

    @pytest.mark.run(order=1)
    @pytest.mark.dependency(name='add')
    def test_add(self,creatCal,a,b):
        assert a + b == creatCal.add(a,b)

    @pytest.mark.run(order=2)
    @pytest.mark.dependency(depends=["add"])
    def test_sub(self,creatCal,a,b):
        assert a - b == creatCal.sub(a,b)

    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depends=["mul"])
    def check_div(self,creatCal,a,b):
        try:
            a / b
        except ZeroDivisionError:
            assert False
        else:
            assert a / b == creatCal.div(a, b)




