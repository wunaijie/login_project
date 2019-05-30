"""个人信息页面"""
from Base.base import Base
from Page.ElementPage import ElementPage


class PersonPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def go_to_setting_page(self):
        self.click_btn(ElementPage.setting_btn)

    def get_login_success_result(self):
        return self.get_element(ElementPage.my_coupons).text
