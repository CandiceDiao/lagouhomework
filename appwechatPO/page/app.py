"""
app.py 主要用于 app的一些常用操作：
启动app,关闭app,重启app,进入主页
"""
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from appwechatPO.page.basepage import BasePage
from appwechatPO.page.main import MainPage


class App(BasePage):
    driver:WebDriver=None
    def start(self):
        _package="com.tencent.wework"
        _activity=".launch.WwMainActivity"
        if self.driver is None:
            caps={}
            caps['platformName'] = 'Android'
            caps['platformVersion'] = '6.0'
            caps['deviceName'] = '127.0.0.1:7555'
            caps['appPackage'] = _package
            caps['appActivity'] = _activity
            caps['noReset'] = 'true'
            # 开启权限
            caps['autoGrantPermissions']=True
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()
        return self

    def researt(self):
        pass

    def close(self):
        self.driver.quit()

    #进入到主页
    def main(self):
        return MainPage(self.driver)
