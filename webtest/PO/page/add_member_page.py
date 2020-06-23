from webtest.PO.page.base_page import BasePage
from webtest.PO.page.contact_page import Contact
from selenium.webdriver.common.by import By

class AddMember(BasePage):
    # 不要暴露太多页面元素；定义为私有变量
    _username = "username1"
    # def __init__(self):
    #     # debug模式 就可以跳过扫码登录环节
    #     option = Options()
    #     option.debugger_address = "localhost:9222"
    #     self.driver = webdriver.Chrome(options=option)

    def add_member(self):
        """
        添加成员
        :return:
        """
        # self.find_element()-》替换成 封装在BasePage 中的 find方法
        self.find(By.ID,"username").send_keys(self._username)
        self.find(By.ID, "memberAdd_acctid").send_keys("acctid1")
        self.find(By.ID, "memberAdd_phone").send_keys("18301271111")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        return Contact(self.driver)

    # 同样的行为，不同的结果，需要创建不同的方法
    def add_member_fail(self):
        """
        添加成员
        :return:
        """
        self.find(By.ID,"username").send_keys("username2")
        self.find(By.ID, "memberAdd_acctid").send_keys("Candice")
        self.find(By.ID, "memberAdd_phone").send_keys("18301271111")
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        self.find(By.CSS_SELECTOR, ".js_btn_cancel").click()
        return Contact(self.driver)