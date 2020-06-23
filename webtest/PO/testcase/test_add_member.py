from webtest.PO.page.main_page import MainPage


class TestAddMember:

    def setup(self):
        # 第一次实例化不能传入self.driver
        self.main = MainPage()

    def teardown(self):
        self.main.quit()

    def test_add_member(self):
        # 1.点击添加成员；跳转到添加成员页面 2.填写成员信息 3.点击保存
        # assert "username1"in
        assert "username1" in self.main.goto_add_member().add_member().get_member()

    def test_add_memeber_fail(self):
        assert "username2" not in self.main.goto_add_member().add_member_fail().get_member()
