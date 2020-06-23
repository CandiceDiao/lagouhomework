from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

# BasePage定义：它是一个其他page的公共方法封装，他是一个底层使用的框架
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _base_url=""
    def __init__(self,driver_basepage:WebDriver=None):
        if driver_basepage==None:
            # debug模式 就可以跳过扫码登录环节
            option = Options()
            option.debugger_address = "localhost:9222"
            self.driver = webdriver.Chrome(options=option)
            # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        else:
            self.driver=driver_basepage

        # _base_url应该放在业务层面，而不是底层框架
        if self._base_url !="":
            self.driver.get(self._base_url)
        self.driver.implicitly_wait(3)

    def find(self,by,value):
        return self.driver.find_element(by=by,value=value)

    def finds(self,by,value):
        return self.driver.find_elements(by=by,value=value)

    def quit(self):
        return self.driver.quit()

    def wait_element_located(self,time,by,value):
        WebDriverWait(self.driver,time).until(
            expected_conditions.presence_of_element_located((by,value)))