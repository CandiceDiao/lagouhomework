from appium.webdriver.common.mobileby import MobileBy

from appwechatPO.page.basepage import BasePage

#个人信息页面
from appwechatPO.page.contactdetailsettingpage import ContactDetailSettingPage

class ContactDetailBriefInfo(BasePage):
     _member_info='//*[@text="个人信息"]/../../../../../*[@class="android.widget.LinearLayout"][2]'


     def click_edit_member_info(self):
         self.find(MobileBy.XPATH,self._member_info).click()
         return ContactDetailSettingPage(self.driver)






