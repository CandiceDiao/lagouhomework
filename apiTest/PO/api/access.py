from apiTest.PO.api.base_api import BaseApi


class Access(BaseApi):

    # 添加成员
    def test_addMember(self,userid,name,mobile,token,department=None):
        if department is None:
            department=[1]
        # 注意 data中传入 json 数据
        data={
            "method":"post",
            "url":f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}',
            "json":{
                "userid": userid,
                "name": name,
                "mobile": mobile,
                "department": department
            }

        }
        res = self.send_api(data)
        return res

    # 读取成员
    def test_getMember(self,userid,token):
        data={
            "method":"get",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/user/get",
            "params":{
                "access_token": token,
                "userid": userid
            }
        }
        res = self.send_api(data)
        return res

    # 修改成员
    def test_updateMember(self,userid,name,token):
        data={
            "method":"post",
            "url":f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}",
            "json":{
                "userid": userid,
                "name": name
            }
        }
        res=self.send_api(data)
        return res

    # 删除成员
    def test_deleteMember(self,userid,token):
        # 注意 get 方法中 data 需要参数 "params"
        data={
            "method":"get",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/user/delete",
            "params":{
                "access_token": token,
                "userid": userid
            }
        }
        res = self.send_api(data)
        return res
    
