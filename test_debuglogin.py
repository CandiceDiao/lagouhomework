from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestDebugLogin:

    def test_debuglogin(self):
        option = Options()
        # chrome --remote-debugging-port=9222
        # 需要和启动命令端口号一致
        # 指定了一个调试地址
        option.debugger_address = "localhost:9222"
        # 把调试地址作为参数传递进去
        self.driver = webdriver.Chrome(options=option)
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
