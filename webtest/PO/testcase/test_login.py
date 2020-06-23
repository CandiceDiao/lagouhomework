from webtest.PO.page.index_Page import IndexPage


class TestLogin:

    def test_login(self):
        main = IndexPage()
        # 1.进入首页 2.跳转登录页面 3.登录
        main.goto_login().login()

