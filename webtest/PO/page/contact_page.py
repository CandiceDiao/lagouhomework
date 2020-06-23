from time import sleep

from selenium.webdriver.common.by import By
from webtest.PO.page.base_page import BasePage

class Contact(BasePage):

    # def __init__(self):
    #     # debug模式 就可以跳过扫码登录环节
    #     option = Options()
    #     option.debugger_address = "localhost:9222"
    #     self.driver = webdriver.Chrome(options=option)

    def get_member(self):
        # 注意使用find_elements：返回值为list of WebElement
        elements=self.finds(By.CSS_SELECTOR,".member_colRight_memberTable_tr td:nth-child(2)")

        # 碰到如下结构；可以使用列表推导式
        # member_list=[]
        # for element in elements:
        #     member_list.append(element.get_attribute("title"))
        member_list=[element.get_attribute("title") for element in elements ]
        return member_list

    def delete_member(self):
        self.find(By.CSS_SELECTOR,".js_list tr:nth-last-child(1) input").click()
        self.find(By.CSS_SELECTOR, 'div.js_has_member  div:nth-child(1) a.js_delete').click()
        self.find(By.CSS_SELECTOR, '.ww_dialog .ww_btn_Blue').click()
        sleep(5)
        return Contact(self.driver)

