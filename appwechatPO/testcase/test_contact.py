import pytest
import yaml

from appwechatPO.page.app import App

with open("../data/wechat.yml", encoding="utf-8") as f:
    datas = yaml.safe_load(f)
    addlist = datas['add']
    dellist = datas['del']

class TestWeWork:

    def setup_class(self):
        self.app = App()
        self.main=self.app.start().main()

    def teatdown_class(self):
        self.app.close()


    @pytest.mark.parametrize(('username,gender,phone'), addlist)
    def test_addcontact(self,username,gender,phone):
        toast = self.main.goto_addresslist().click_addmember().\
            addmember_menual().edit_username(username).\
            edit_gender(gender).edit_phonenum(phone)\
            .click_save().get_result()
        assert '添加成功' == toast
        # 回到上一个页面
        self.main.back()


    @pytest.mark.parametrize(('username'), dellist)
    def test_delcontact(self, username):
        self.main.goto_addresslist().click_member(username).\
            click_edit_member_info().click_edit_member().\
            click_delete_member().find_element_until_not(15,username)
