"""注册页面"""
from Base.base import Base
from Page.ElementPage import ElementPage


class SignPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def go_to_login_page(self):
        """点击已有账号,去登录"""
        self.click_btn(ElementPage.go_to_login_page_btn)
