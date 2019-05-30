"""统一入口页面"""
from Page.ElementPage import ElementPage
from Page.indexPage import IndexPage
from Page.loginPage import LoginPage
from Page.personPage import PersonPage
from Page.settingPage import SettingPage
from Page.signPage import SignPage


class Page(object):
    def __init__(self, driver):
        self.driver = driver

    def get_index_page(self):
        """实例化首页类"""
        return IndexPage(self.driver)

    def get_sign_page(self):
        """实例化注册页面类"""
        return SignPage(self.driver)

    def get_login_page(self):
        """实例化登录页面类"""
        return LoginPage(self.driver)

    def get_person_page(self):
        """实例化个人信息页面类"""
        return PersonPage(self.driver)

    def get_setting_page(self):
        """实例化设置页面类"""
        return SettingPage(self.driver)

    def get_element_page(self):
        return ElementPage()
