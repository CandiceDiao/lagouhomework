
# 添加成员页面
# from appwechatPO.page.memberinvitepage import MemberInvitePage
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from appwechatPO.page.basepage import BasePage


class ContactAddPage(BasePage):
    _username_element = ("//*[contains(@text, '姓名')]/../android.widget.EditText")
    _gender_element = ("//*[@text='性别']/..//*[@text='男']")
    _female_element = ( "//*[@text='女']")
    _male_element = ("//*[@text='男']")
    _phonenum_element = ("//*[contains(@text, '手机')]/..//*[@text='手机号']")

    _save_element = ("//*[@text='保存']")

    # 编辑姓名
    def edit_username(self,username):
        self.find(MobileBy.XPATH,self._username_element).send_keys(username)
        return self

    # 编辑性别
    def edit_gender(self,gender):
        self.find(MobileBy.XPATH,self._gender_element).click()
        if gender=='男':
            self.find(MobileBy.XPATH,self._male_element).click()
        else:
            self.find(MobileBy.XPATH,self._female_element).click()
        return self

    # 编辑手机号
    def edit_phonenum(self,phone):
        self.find(MobileBy.XPATH,self._phonenum_element).send_keys(phone)
        return self

    def click_save(self):
        self.find(MobileBy.XPATH,self._save_element).click()
        from appwechatPO.page.memberinvitepage import MemberInvitePage
        return MemberInvitePage()



