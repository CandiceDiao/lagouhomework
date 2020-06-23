from webtest.PO.page.main_page import MainPage

class TestUploadMemeber():

    def setup(self):
        self.main = MainPage()

    def test_upload_member(self):
        assert "标准表汇总.xlsx" == self.main.goto_upload_contact().uploadFile('C:/Users/WBPC0154/Desktop/标准表汇总.xlsx')

    def goto_main_page(self):
        # return MainPage(self.driver)
        pass
