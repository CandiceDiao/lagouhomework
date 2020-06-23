
from selenium.webdriver.common.by import By

from webtest.PO.page.add_member_page import AddMember
from webtest.PO.page.base_page import BasePage
from webtest.PO.page.contact_page import Contact
from webtest.PO.page.upload_page import UploadPage


class MainPage(BasePage):
    # def __init__(self):
    #     # debug模式 就可以跳过扫码登录环节
    #     option = Options()
    #     option.debugger_address = "localhost:9222"
    #     self.driver = webdriver.Chrome(options=option)
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    # 实例化MainPage时会将BasePage._base_url替换
    _base_url="https://work.weixin.qq.com/wework_admin/frame#index"
    def goto_add_member(self):
        #click
        self.find(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(1)").click()
        return AddMember(self.driver)

    def goto_contact(self):
        return Contact(self.driver)

    def goto_upload_contact(self):
        self.find(By.CSS_SELECTOR,".index_service a:nth-child(2) span:nth-child(2)").click()
        return UploadPage(self.driver)

