from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

"""
用来存放一些最基本的操作
1.实例化driver对象
2.查找元素find方法
3.appium 底层操作
"""

class BasePage:
    driver:WebDriver
    def __init__(self,driver:WebDriver = None):
        self.driver=driver

    #查找元素
    def find(self,by,locator=None):
        element = self.driver.find_elements(*by) if isinstance(by, tuple) else self.driver.find_element(by, locator)
        self._error_cont = 0
        return element


    def find_by_scroll(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector().scrollable(true)\
            .instance(0)).scrollIntoView(new UiSelector().\
            text("{text}").instance(0));')

    def get_toast(self):
        return self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text

    def back(self,number=1):
        for i in range(number):
            self.driver.back()

    def find_element_until_not(self,time,username):
        WebDriverWait(self.driver, 15).until_not(lambda x:x.find_element(MobileBy.XPATH,f"//*[@text='{username}']"))