
# 添加成员页面
# from appwechatPO.page.contactaddpage import ContactAddPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appwechatPO.page.basepage import BasePage


class MemberInvitePage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    _import_text='//*[@text="手动输入添加"]'
    def addmember_menual(self):
        # 局部导入
        self.find(By.XPATH,self._import_text).click()
        from appwechatPO.page.contactaddpage import ContactAddPage
        return ContactAddPage(self.driver)

    def get_result(self):
        # toast_local = (By.XPATH, '//*[@class="android.widget.Toast"]')
        # WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(toast_local))
        toast_text = self.get_toast()
        return toast_text