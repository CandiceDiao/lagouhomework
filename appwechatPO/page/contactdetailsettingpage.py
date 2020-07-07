from appium.webdriver.common.mobileby import MobileBy

from appwechatPO.page.basepage import BasePage
from appwechatPO.page.editmemberpage import EditMemberPage

#个人信息设置页面
class ContactDetailSettingPage(BasePage):
    _edit_member = '//*[@text="编辑成员"]'
    def click_edit_member(self):
        self.find(MobileBy.XPATH, self._edit_member).click()
        return EditMemberPage(self.driver)
