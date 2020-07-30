#### 阶段十 企业微信-接口测试实战
# 实现通讯录的增删改查

import requests
class TestWechatAccess:

    # token 相当于身份证
    def test_get_token(self):

        # 精简url方法一: 使用f{变量}
        # corpid='ww44051ca7a74ae8e3'
        # corpsecret='uhSqBpzjxIvpbfPaXuPH574dfKwPUcLzlnqOGEklghc'
        # res=requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}")

        # 精简url方法二: 将？后面的变量放入params中;注意params中不能带？
        # 主要传递参数是不能加上引号； corpid/corpsecret
        params={
            "corpid":"ww44051ca7a74ae8e3",
            "corpsecret":"uhSqBpzjxIvpbfPaXuPH574dfKwPUcLzlnqOGEklghc"
        }
        res = requests.get(url="https://qyapi.weixin.qq.com/cgi-bin/gettoken",params=params)

        # 返回值res是 response 类型-》'requests.models.Response'
        print(type(res))
        print(res.json()['access_token'])
        # 直接return 由上层调用改方法的地方做异常处理
        return res.json()['access_token']

    # 添加成员
    def test_addMember(self):
        data = {
                "userid": "zhangsan",
                "name": "张三",
                "mobile": "13800000009",
                "department": [1]
        }
        # 上方data为python类型，如果通过请求传输，必须要转化为json!!!
        # 因为在接口文档：开发必读中表明 所有的接口需使用HTTPS协议、JSON数据格式、UTF8编码。
        # 可以使用json.loads（）进行转换；或者 直接使用json=data

        res = requests.post(url=f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.test_get_token()}',json=data)
        print(res.json())

    # 读取成员
    def test_getMember(self):
        params={
            "access_token":self.test_get_token(),
            "userid":"zhangsan1"
        }
        res = requests.get("https://qyapi.weixin.qq.com/cgi-bin/user/get",params=params)
        print(res.json())

    # 修改成员
    def test_updateMember(self):
        data={
            "userid":"zhangsan",
            "name":"王五"
        }
        res=requests.post(url=f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.test_get_token()}",json=data)
        print(res.json())

    # 删除成员
    def test_deleteMember(self):
        params={
            "access_token":self.test_get_token(),
            "userid":"zhangsan"
        }
        res = requests.get(url="https://qyapi.weixin.qq.com/cgi-bin/user/delete",params=params)
        print(res.json())