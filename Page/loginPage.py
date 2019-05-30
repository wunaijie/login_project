from Base.base import Base
from Page.ElementPage import ElementPage


class LoginPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def login(self, name, password):
        """
        登录
        :param name: 用户名
        :param password: 密码
        :return:
        """
        """输入用户名"""
        self.send_content_to_box(ElementPage.count_box, name)
        """输入密码"""
        self.send_content_to_box(ElementPage.password_box, password)
        """点击登录"""
        self.click_btn(ElementPage.login_btn)

    def close_login_page(self):
        """关闭登录页面"""
        self.click_btn(ElementPage.close_login_page_btn)

    def if_login_btn(self):
        """判断登录按钮是否存在"""
        self.get_element(ElementPage.login_btn)
