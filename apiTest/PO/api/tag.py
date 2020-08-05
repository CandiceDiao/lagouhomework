from apiTest.PO.api.base_api import BaseApi


class Tag(BaseApi):

    # 创建标签
    def test_addTag(self,tagid,tagname,token):
        data={
            "method":"post",
            "url":f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={token}",
            "json":{
            "tagname":tagname,
            "tagid":tagid
            }
        }
        res=self.send_api(data)
        return res


    # 更新标签名字
    def test_updateTag(self,tagid,tagname,token):
        data={
            "method":"post",
            "url":f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={token}",
            "json":{
            "tagname": tagname,
            "tagid": tagid
            }
        }
        res=self.send_api(data)
        return res

    # 删除标签
    def test_delTag(self,tagid,token):
        data={
            "method":"get",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/tag/delete",
            "params":{
                "access_token": token,
                "tagid": tagid
            }
        }
        res=self.send_api(data)
        return res

    # 获取标签列表
    def test_getTag(self,token):
        data={
            "method":"get",
            "url":"https://qyapi.weixin.qq.com/cgi-bin/tag/list",
            "params":{
                "access_token": token
            }
        }
        res=self.send_api(data)
        return res
