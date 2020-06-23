"""
登录页面
"""
from webtest.PO.page.register_page import RegisterPage


class LoginPage:

    def login(self):
        pass

    def goto_register(self):
        return RegisterPage()