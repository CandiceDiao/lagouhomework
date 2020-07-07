import time

from appium.webdriver.common.mobileby import MobileBy


from appwechatPO.page.basepage import BasePage


class EditMemberPage(BasePage):
    _delete_text='删除成员'
    def click_delete_member(self):
        self.find_by_scroll(self._delete_text).click()
        time.sleep(2)
        self.find(MobileBy.XPATH,'//*[@text="确定"]').click()
        from appwechatPO.page.addresslistpage import AddressListPage
        return AddressListPage(self.driver)

