"""首页页面"""
from Base.base import Base
from Page.ElementPage import ElementPage


class IndexPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def go_to_sign_page(self):
        """点击'我'按钮,去到注册页面"""
        self.click_btn(ElementPage.my_btn)



