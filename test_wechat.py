"""
分别使用浏览器复用和cookie登录企业微信。
将所有的死等都封装成显式等待
"""
import json
from time import sleep
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWechat:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")

    def teardown(self):
        self.driver.quit()

    # @pytest.mark.skip
    def test_get_cookie(self):
        # sleep(15)
        while True:
            # 等待直到出现“首页”并且可以点击，证明扫码成功
            res=WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable((By.ID, 'menu_index')))
            if res is not None:
                break
        cookies=self.driver.get_cookies()
        with open("cookies.json","w") as f:
            f.write(json.dumps(cookies))

    def test_login_bycookie(self):
        with open ("cookies.json") as f:
            cookies=json.load(f)
        for i in range(0,len(cookies)):
            self.driver.add_cookie(cookies[i])
        # 刷新
        self.driver.refresh()
        while True:
            # 等待直到出现“首页”并且可以点击，证明扫码成功
            res=WebDriverWait(self.driver, 15).until(expected_conditions.element_to_be_clickable((By.ID, 'menu_index')))
            if res is not None:
                break
        # sleep(5)
        # 显示等待按钮“导入通讯录”可以被点击
        # WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,".index_service a:nth-child(2) span:nth-child(2)")))
        self.driver.find_element(By.CSS_SELECTOR,".index_service a:nth-child(2) span:nth-child(2)").click()
        # sleep(5)
        # 显示等待
        WebDriverWait(self.driver,5).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"#js_upload_file_input")))
        self.driver.find_element(By.CSS_SELECTOR,"#js_upload_file_input").send_keys('C:/Users/diaod/Desktop/【测试工程师】学习计划.xlsx')
        # sleep(5)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located((By.ID,"upload_file_name")))
        assert_ele=self.driver.find_element(By.ID,"upload_file_name").text
        assert assert_ele=="【测试工程师】学习计划.xlsx"