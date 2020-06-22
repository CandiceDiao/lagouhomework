import pytest

from homework.pytest.cal import calculate

@pytest.fixture()
def creatCal():
    cal = calculate()
    print("开始计算")
    yield cal
    print("计算结束")
