from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from webtest.PO.page.base_page import BasePage


class UploadPage(BasePage):

    def uploadFile(self,filepath):
        # WebDriverWait(self.driver, 5).until(
        #     expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#js_upload_file_input")))
        self.wait_element_located(5,By.CSS_SELECTOR, "#js_upload_file_input")
        self.find(By.CSS_SELECTOR, "#js_upload_file_input").send_keys(filepath)
        # WebDriverWait(self.driver, 5).until(
        #     expected_conditions.presence_of_element_located((By.ID, "upload_file_name")))
        self.wait_element_located(5, By.ID, "upload_file_name")
        assert_ele = self.find(By.ID, "upload_file_name").text
        return assert_ele


    # def goto_main_page(self):
    #     return MainPage(self.driver)
