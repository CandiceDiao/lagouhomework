# 通讯率录页面
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from appwechatPO.page.basepage import BasePage
from appwechatPO.page.contactdetailbriefInfo import ContactDetailBriefInfo
from appwechatPO.page.memberinvitepage import MemberInvitePage


class AddressListPage(BasePage):
    _addmember_text='添加成员'
    # def __init__(self,driver):
    #     self.driver = driver

    # 点击添加成员
    def click_addmember(self):
        self.find_by_scroll(self._addmember_text).click()
        return MemberInvitePage(self.driver)

    def click_member(self,name):
        self.find_by_scroll(name).click()
        return  ContactDetailBriefInfo(self.driver)
