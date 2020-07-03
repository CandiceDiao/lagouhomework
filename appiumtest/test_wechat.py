import pytest
import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""企业微信添加联系人
1、编写添加联系人测试用例
2、编写删除联系人测试用例
"""
class TestWechat:
    def setup(self):
        des_caps={
            'platformName':'android',
            'platformVersion':'6.0',
            'appPackage':'com.tencent.wework',
            'appActivity':'.launch.WwMainActivity',
            'noReset':True,
            'deviceName':'127.0.0.1:7555',
            'chromerdriverExecutable':'D:/mobiledriver'
        }
        self.driver=webdriver.Remote("http://localhost:4723/wd/hub",des_caps)
        # self.driver.implicitly_wait(10)
        contact_local = (
        By.XPATH, '//*[@class="android.widget.LinearLayout"]/*[@class="android.view.ViewGroup"]//*[@text="通讯录"]')
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(contact_local))
        self.driver.find_element(*contact_local).click()

    def teardown(self):
        self.driver.quit()

    # @pytest.mark.skip
    @pytest.mark.parametrize(('data'),yaml.safe_load(open("./wechat.yml")))
    def test_add_member(self,data):
        add_locator = (By.XPATH,'//*[@text="添加成员"]')
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(add_locator))
        self.driver.find_element(*add_locator).click()
        manualAdd_local=(By.XPATH,'//*[@text="手动输入添加"]')
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(manualAdd_local))
        self.driver.find_element(*manualAdd_local).click()

        name_local=(By.XPATH, '//*[contains(@text,"姓名")]/..//*[@class="android.widget.EditText"]')
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(name_local))
        self.driver.find_element(*name_local).send_keys(f'{data["name"]}')
        self.driver.find_element(By.XPATH, '//*[contains(@text,"性别")]/../ *[@class ="android.widget.RelativeLayout"]').click()
        gender_local=(By.XPATH, '//*[contains(@text,"女")]')
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(gender_local))
        self.driver.find_element(*gender_local).click()
        self.driver.find_element(By.XPATH,
                                 '// *[contains(@text,"手机")] /..// *[@class ="android.widget.EditText"]').send_keys(f'{data["phone"]}')
        self.driver.find_element(By.XPATH, '//*[@text = "保存"]').click()

        # #Toast控件：添加成功
        toast_local=(By.XPATH,'//*[@class="android.widget.Toast"]')
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(toast_local))
        toast_text = self.driver.find_element(*toast_local).text
        assert toast_text =='添加成功'

    def test_delete_member(self):
        contact_locator = (By.XPATH, '//*[@text = "Matcha"] /../../../../..// android.widget.RelativeLayout[last()]')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(contact_locator))
        self.driver.find_element(*contact_locator).click()
        manage_local=(By.XPATH,'//*[@text="管理通讯录"]')
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(manage_local))

        element_before = len(self.driver.find_elements(By.XPATH,
                                                       '//*[@class="android.widget.ListView"]/*[@class="android.widget.RelativeLayout"]'))
        self.driver.find_element(By.XPATH,
                                 '//android.widget.ListView/android.widget.RelativeLayout[last()-1]/android.widget.RelativeLayout/android.widget.RelativeLayout[last()]').click()
        del_local=(By.XPATH,'//*[@text="删除成员"]')
        WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable(del_local))
        self.driver.find_element(*del_local).click()
        ok_local = (By.XPATH, '//*[@text="确定"]')
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(ok_local))
        self.driver.find_element(*ok_local).click()

        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(manage_local))
        element_after=len(self.driver.find_elements(By.XPATH,'//*[@class="android.widget.ListView"]/*[@class="android.widget.RelativeLayout"]'))
        assert element_before-1==element_after









