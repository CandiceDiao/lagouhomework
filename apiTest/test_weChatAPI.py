# 作业
# 实现通讯录的增删改查
# 使用 session 减少字段的重复项
import requests
from hamcrest import *
class TestWechatAccess:
    ###实例化会话对象
    s = requests.Session()
    def setup(self):
        params={
            "corpid":"ww44051ca7a74ae8e3",
            "corpsecret":"uhSqBpzjxIvpbfPaXuPH574dfKwPUcLzlnqOGEklghc"
        }
        res = self.s.get(url="https://qyapi.weixin.qq.com/cgi-bin/gettoken",params=params)
        ###将token放入会话对象中
        self. s.params.update({"access_token": res.json()['access_token']})

    # 添加成员
    def test_addMember(self):
        data = {
                "userid": "zhangsan",
                "name": "张三",
                "mobile": "13800000009",
                "department": [1]
        }
        # res = requests.post(url=f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.test_get_token()}',
        #                     json=data)
        res = self.s.post(url=f'https://qyapi.weixin.qq.com/cgi-bin/user/create',json=data)
        ###将userid放入会话对象中
        self.s.params.update({"userid":"zhangsan"})
        assert(self.test_getMember()['name']=="张三")
        print(res.json())

    #  读取成员
    def test_getMember(self):
        # params = {
        #     "access_token": self.test_get_token(),
        #     "userid": "zhangsan1"
        # }
        # res = self.s.get("https://qyapi.weixin.qq.com/cgi-bin/user/get",params=params)
        res = self.s.get("https://qyapi.weixin.qq.com/cgi-bin/user/get")
        return res.json()
        print(res.json())

    # 修改成员
    def test_updateMember(self):
        data={
            "userid":"zhangsan",
            "name":"王五"
        }
        res=self.s.post(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/update",json=data)
        assert (self.test_getMember()['name'] == "王五")
        print(res.json())

    # 删除成员
    def test_deleteMember(self):
        # params={
        #     "userid":"zhangsan"
        # }
        res = self.s.get(url="https://qyapi.weixin.qq.com/cgi-bin/user/delete")
        assert_that(self.test_getMember()['errmsg'], starts_with('userid not found'))
        print(res.json())


