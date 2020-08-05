import re

import pytest

from apiTest.PO.api.access import Access
from apiTest.PO.api.wework import WeWork


class TestAccess:

    # ####使用fixture 获取token
    @pytest.fixture(scope="session")
    def token(self,get_token):
        yield WeWork().get_token

    def setup(self):
        self.access = Access()

    def create_muti_data(self):
        # 138%08d=138后面用0补齐：138%0 补齐8位置 138%08d
        data = [("wu12345wu" + str(x), "zhangsan1", "138%08d" % x) for x in range(10)]
        return data

    @pytest.mark.parametrize("userid,name,mobile", create_muti_data("xxx"))
    # 组合
    def test_all(self, userid, name, mobile,get_token):
        try:
            # 创建一个成员, 对结果断言
            assert "created" == self.access.test_addMember(userid, name, mobile, get_token)['errmsg']
        except AssertionError as e:
            print("******")
            if "userid existed" in e.__str__():
                self.access.test_deleteMember(userid, get_token)
            if "mobile existed" in e.__str__():
                delete_userid = re.findall(":(.*)'$", e.__str__())
                self.access.test_deleteMember(delete_userid, get_token)
            assert "created" == self.access.test_addMember(userid, name, mobile, get_token)['errmsg']
        # 查询成员信息，对结果断言
        assert name == self.access.test_getMember(userid,get_token)['name']
        # 更新一个成员
        assert "updated" == self.access.test_updateMember(userid, "wangwu",get_token)['errmsg']
        # 查询成员信息，对结果断言
        assert "wangwu" == self.access.test_getMember(userid,get_token)['name']
        # 删除
        assert "deleted" == self.access.test_deleteMember(userid,get_token)['errmsg']
        # 查询成员信息，对结果断言
        assert 60111 == self.access.test_getMember(userid,get_token)['errcode']

