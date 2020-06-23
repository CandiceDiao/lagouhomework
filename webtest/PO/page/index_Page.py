'''
企业微信首页
'''
from webtest.PO.page.login_page import LoginPage
from webtest.PO.page.register_page import RegisterPage


class IndexPage:

    def goto_login(self):
        """
        跳转到登录页面
        :return: LoginPage的一个实例化
        """
        return LoginPage()

    def goto_register(self):
        """
         跳转到注册页面
         :return: RegisterPage
         """
        return RegisterPage()
