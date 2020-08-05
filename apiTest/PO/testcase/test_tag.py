### 作业 利用封装思想，实现 tag 的增删改查
import random
import pytest
from apiTest.PO.api.tag import Tag
from apiTest.PO.api.wework import WeWork

class TestTag:
    # ####使用fixture 获取token
    @pytest.fixture(scope="session")
    def token(self,get_token):
        yield WeWork().get_token

    def setup(self):
        self.tag = Tag()

    def create_muti_data(self):
        data = [(x+1,"tag%0d"% x) for x in range(10)]
        return data

    def search_tag(self,res,tagname):
        for i in range(len(res['taglist'])):
            if res['taglist'][i]['tagname'] == tagname:
                return res['taglist'][i]['tagid']
                break;
        return None

    @pytest.mark.parametrize("tagid,tagname", create_muti_data("xxx"))
    # 组合
    def test_all(self, tagid, tagname,get_token):
        try:
            # 创建一个tag, 对结果断言
            assert "created" == self.tag.test_addTag(tagid,tagname, get_token)['errmsg']
        except AssertionError as e:
            if "UserTag Name Already Exist" in e.__str__():
                res=self.tag.test_getTag(get_token)
                del_tagid = self.search_tag(res, tagname)
                self.tag.test_delTag(del_tagid, get_token)
                res = self.tag.test_getTag(get_token)
                del_tagid = self.search_tag(res, tagname)
            if "invalid tagid" in e.__str__():
                self.tag.test_delTag(tagid, get_token)
            assert "created" == self.tag.test_addTag(tagid,tagname, get_token)['errmsg']
            res = self.tag.test_getTag(get_token)
        # 查询tag信息，对结果断言
        res_get =self.tag.test_getTag(get_token)
        assert tagid == self.search_tag(res_get, tagname)
        # 更新一个tag
        tagname="updataTag"+str(random.randint(0,100))
        assert "updated" == self.tag.test_updateTag(tagid, tagname,get_token)['errmsg']
        # 查询tag信息，对结果断言
        res_get = self.tag.test_getTag(get_token)
        assert tagid == self.search_tag(res_get, tagname)
        # 删除
        assert "deleted" == self.tag.test_delTag(tagid,get_token)['errmsg']
        # 查询tag信息，对结果断言
        res_get = self.tag.test_getTag(get_token)
        assert None == self.search_tag(res_get, tagname)
