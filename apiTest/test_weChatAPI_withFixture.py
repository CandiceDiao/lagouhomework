# 作业
# 实现通讯录的增删改查
# 使用 session 减少字段的重复项
import random
import re

import pytest
import requests
from hamcrest import *
class TestWechatAccess:
    ##实例化会话对象
    s = requests.Session()
    def setup(self):
        params={
            "corpid":"ww44051ca7a74ae8e3",
            "corpsecret":"uhSqBpzjxIvpbfPaXuPH574dfKwPUcLzlnqOGEklghc"
        }
        res = self.s.get(url="https://qyapi.weixin.qq.com/cgi-bin/gettoken",params=params)
        print(res.json())
        ###将token放入会话对象中
        self. s.params.update({"access_token": res.json()['access_token']})

    ####使用fixture 获取token
    @pytest.fixture(scope="session")
    def token(self):
        params = {
            "corpid": "ww44051ca7a74ae8e3",
            "corpsecret": "uhSqBpzjxIvpbfPaXuPH574dfKwPUcLzlnqOGEklghc"
        }
        res = requests.get(url="https://qyapi.weixin.qq.com/cgi-bin/gettoken", params=params)
        try:
            # 使用yield进行返回，而不是return
            yield res.json()['access_token']
        except Exception as e:
            raise ValueError("requests token error")
    # # 如何使用fixture生成器
    # #  读取成员
    # def test_getMember(self,token,userid="Candice"):
    #     params = {
    #         "access_token":token,
    #         "userid": userid
    #     }
    #     res = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/get",params=params)
    #     return res.json()

    # 添加成员
    def test_addMember(self,userid,name,mobile,department=None):
        # 参数最好不要定义为数组类型->department=[1]
        if department is None:
            department=[1]
        data = {
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": department
        }
        # res = requests.post(url=f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.test_get_token()}',
        #                     json=data)
        res = self.s.post(url=f'https://qyapi.weixin.qq.com/cgi-bin/user/create',json=data)
        # assert(self.test_getMember()['name']=="张三")
        return res.json()
        print(res.json())

    # #  读取成员
    # def test_getMember(self,userid):
    #     params = {
    #         "userid": userid
    #     }
    #     res = self.s.get("https://qyapi.weixin.qq.com/cgi-bin/user/get",params=params)
    #     return res.json()

    # 修改成员
    def test_updateMember(self,userid,name):
        data={
            "userid":userid,
            "name":name
        }
        res=self.s.post(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/update",json=data)
        return res.json()

    # 删除成员
    def test_deleteMember(self,userid):
        params={
            "userid":userid
        }
        res = self.s.get(url="https://qyapi.weixin.qq.com/cgi-bin/user/delete",params=params)
        return res.json()

    #应该使用数据驱动读取数据
    # 并发执行测试数据时：random.randint生成数据采用的是时间种子；所以可能存在相同数据
    def test_create_data(self):
        # 此处使用列表生成器;生成三个数组
        # 列表生成器的缺点是占内存
        data = [(str(random.randint(0,9999999)),
                "zhangsan",
                str(random.randint(18300000000,18309999999))) for x in range(3)]
        return data

    # 并发执行测试数据时：random.randint生成数据采用的是时间种子；所以可能存在相同数据
    def create_muti_data(self):
        #138%08d=138后面用0补齐：138%0 补齐8位置 138%08d
        data=[("wu12345wu"+str(x),"zhangsan1","138%08d" %x) for x in range(20)]
        return data

    @pytest.mark.parametrize("userid,name,mobile",create_muti_data("xxx"))
     # 组合
    def test_all(self,userid,name,mobile):
        try:
            # 创建一个成员，对结果断言
            assert "created" == self.test_addMember("cc1", "cc", "18301111111")['errmsg']
        except AssertionError as e:
            ### e.__str__() 打印异常信息
            if "userid existed" in e.__str__():
                self.test_deleteMember(userid)
            elif "mobile existed" in e.__str__():
                # {'errcode':60104,'errmsg':'mobile existed:zhangsan'}
                #使用正则表达找出 :zhangsan' 以：开头 '结尾 中间的内容-》zhangsan
                dele_userid=re.findall(":(.*)'$",e.__str__())
                self.test_deleteMember(dele_userid)
            assert "created" == self.test_addMember(userid, name, mobile)['errmsg']
        #查询成员信息，对结果断言
        assert name==self.test_getMember(userid)['name']
        #更新一个成员
        assert "updated" ==self.test_updateMember(userid,"wangwu")['errmsg']
        #查询成员信息，对结果断言
        assert "wangwu" == self.test_getMember(userid)['name']
        #删除
        assert "deleted" == self.test_deleteMember(userid)['errmsg']
        #查询成员信息，对结果断言
        assert 60111 == self.test_getMember(userid)['errcode']




