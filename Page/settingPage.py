"""设置页面"""
from Base.base import Base
from Page.ElementPage import ElementPage


class SettingPage(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)

    def scroll_screen_in_setting(self, con=1):
        """滑动屏幕操作"""
        self.swipe_screen(con)

    def click_login_out_btn(self, conf=1):
        """
        点击退出按钮
        :param conf: 1(默认):确认退出,其他:取消退出
        """
        self.scroll_screen_in_setting(1)  # 滑动屏幕操作
        self.click_btn(ElementPage.logout_btn)
        if conf:
            self.click_btn(ElementPage.confirm_logout_btn)

        else:
            self.click_btn(ElementPage.dis_logout_btn)
