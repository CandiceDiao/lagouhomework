from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appwechatPO.page.addresslistpage import AddressListPage

# 主页面
from appwechatPO.page.basepage import BasePage


class MainPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    _contact='//*[@class="android.widget.LinearLayout"]/*[@class="android.view.ViewGroup"]//*[@text="通讯录"]'
    # 进入到通讯录方法
    def goto_addresslist(self):
        contact_local = (By.XPATH,self._contact)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(contact_local))
        self.driver.find_element(*contact_local).click()
        return AddressListPage(self.driver)

