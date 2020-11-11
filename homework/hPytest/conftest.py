import pytest
import yaml

from homework.hPytest.cal import calculate


@pytest.fixture()
def creatCal():
    cal = calculate()
    print("开始计算")
    yield cal
    print("计算结束")

# 注册一个命令行参数env,env默认值是test,表示测试环境，另外还有两个值 （dev,st）不同的环境读取不同的数据。

def pytest_addoption(parser):
    mygroup=parser.getgroup("CandiceAddRunOption")
    mygroup.addoption("--env",  #注册一个命令行选项
                      default='test',
                      dest='env',
                      help='set your run env')


@pytest.fixture(scope='session')
def cmdoption(request):
    myenv=request.config.getoption("--env",default='test')
    with open("data_env") as f:
        datas = yaml.safe_load(f)
    if myenv=='test':
        print('这是测试数据')
        datas=datas['test']
        print(type(datas))
    elif myenv=='dev':
        print('这是开发数据')
        datas = datas['dev']
    return datas

