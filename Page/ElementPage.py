# 元素页面
from selenium.webdriver.common.by import By


class ElementPage(object):
    """点击我按钮"""
    my_btn = (By.XPATH, "//*[contains(@text,'我')]")
    """去登录按钮"""
    go_to_login_page_btn = (By.XPATH, "//*[contains(@text,'已有')]")
    """输入账号框"""
    count_box = (By.XPATH, "//*[contains(@text,'昵称')]")
    """输入密码框"""
    password_box = (By.ID, "com.yunmall.lc:id/logon_password_textview")
    """点击登录按钮"""
    login_btn = (By.ID, "com.yunmall.lc:id/logon_button")
    """设置按钮"""
    setting_btn = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")
    """我的优惠券"""
    my_coupons = (By.ID, "com.yunmall.lc:id/txt_my_coupons")
    """退出账号按钮"""
    logout_btn = (By.ID, "com.yunmall.lc:id/setting_logout")
    """确认退出"""
    confirm_logout_btn = (By.ID, "com.yunmall.lc:id/ymdialog_right_button")
    """取消退出"""
    dis_logout_btn = (By.ID, "com.yunmall.lc:id/ymdialog_left_button")
    """退出登录页面按钮"""
    close_login_page_btn = (By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image")
