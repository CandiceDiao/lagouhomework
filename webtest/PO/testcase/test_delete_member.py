from webtest.PO.page.main_page import MainPage

class TestDeleteMemeber:

    def setup(self):
        self.main = MainPage()

    def test_delete_member(self):
        # 添加一个成员
        self.main.goto_add_member().add_member()

        assert "username1" not in self.main.goto_contact().delete_member().get_member()
