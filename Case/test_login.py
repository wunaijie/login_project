from selenium.common.exceptions import TimeoutException
from Base.getDriver import get_phone_driver
from Page.Page import Page
from Base.get_data import GetFileData
import sys
import os
import pytest

sys.path.append(os.getcwd())


def get_login_data():
    """定义一个读取数据的方法"""

    success_data_list = []  # 预期成功的数据列表
    fail_data_list = []  # 预期失败的数据列表
    login_data = GetFileData().get_file_data("login_data.yml")
    for i in login_data:
        if login_data.get(i).get("toast"):
            fail_data_list.append((i, login_data.get(i).get("account"),
                                   login_data.get(i).get("passwd"),
                                   login_data.get(i).get("toast"),
                                   login_data.get(i).get("expect_data")))
        else:
            success_data_list.append((i, login_data.get(i).get("account"), login_data.get(i).get("passwd")
                                      , login_data.get(i).get("expect_data")))
    return {"success": success_data_list, "fail": fail_data_list}


class TestLLogin(object):
    def setup_class(self):
        """初始化对象"""
        self.driver = get_phone_driver('com.yunmall.lc', 'com.yunmall.ymctoc.ui.activity.MainActivity')
        self.page_obj = Page(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(autouse=True)
    def into_login_page(self):
        """点击首页'我',跳转至注册页面"""
        self.page_obj.get_index_page().go_to_sign_page()

        """点击"已账号",跳转至登录页面"""
        self.page_obj.get_sign_page().go_to_login_page()

    @pytest.mark.parametrize("login_num,name,password,exp", get_login_data().get("success"))
    def test_success_login(self, login_num, name, password, exp):
        """打印测试数据顺序"""
        print("这是用例测试:", login_num)

        """点击首页'我',跳转至注册页面"""
        self.page_obj.get_index_page().go_to_sign_page()

        """点击"已账号",跳转至登录页面"""
        self.page_obj.get_sign_page().go_to_login_page()

        """输入信息,点击登录,跳转至个人页面"""
        self.page_obj.get_login_page().login(name, password)

        """进行断言,点击设置,跳转至设置页面"""
        try:
            """断言成功"""
            res = self.page_obj.get_person_page().get_login_success_result()
            try:
                assert res in exp
            except AssertionError:
                """在个人中心,但没有'exp'"""
                """截图"""
                self.page_obj.get_person_page().screen_shot()
                assert False
            finally:
                """点击设置"""
                self.page_obj.get_person_page().go_to_setting_page()
                """执行退出操作`"""
                self.page_obj.get_setting_page().scroll_screen_in_setting(1)
                self.page_obj.get_setting_page().click_login_out_btn(1)
        except TimeoutException:
            """断言失败"""
            """还停留在登录页面"""
            self.page_obj.get_person_page().screen_shot()  # 截图
            """需要执行退出登录页面,以便于进行下面的测试"""
            self.page_obj.get_login_page().close_login_page()

    @pytest.mark.parametrize("login_num,name,password,toast,exp", get_login_data().get("fail"))
    def test_fail_login(self, login_num, name, password, toast, exp):
        print("这是测试用例", login_num)

        """输入信息,点击登录,跳转至个人页面"""
        self.page_obj.get_login_page().login(name, password)

        """进行断言"""

        try:
            """能获取toast信息"""
            message = self.page_obj.get_login_page().get_toast(toast)
            try:
                assert message == exp
            except AssertionError:
                """截图"""
                self.page_obj.get_login_page().screen_shot()
                assert False
            finally:
                try:
                    """判断登录按钮在不在"""
                    assert self.page_obj.get_login_page().if_login_btn()
                    """在,就关闭登录页面"""
                    self.page_obj.get_login_page().close_login_page()
                except AssertionError:
                    """不在,就可能在个人页面"""
                    """截图"""
                    self.page_obj.get_login_page().screen_shot()
                    """点击设置"""
                    self.page_obj.get_person_page().go_to_setting_page()
                    """执行退出操作`"""
                    self.page_obj.get_setting_page().click_login_out_btn(1)
                    assert False
        except TimeoutException:
            """不能获取到toast消息"""
            try:
                """对登录按钮进行判断"""
                self.page_obj.get_login_page().if_login_btn()  # 登录按钮在,表示在登录页面
                self.page_obj.get_login_page().close_login_page()  # 关闭登录页面
            except TimeoutException:
                self.page_obj.get_person_page().go_to_setting_page()  # 点击设置
                self.page_obj.get_setting_page().click_login_out_btn()  # 执行退出操作
                assert False

