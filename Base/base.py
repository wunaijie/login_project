import os
import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, location, timeout=30, poll_frequency=1):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*location))

    def get_elements(self, location, timeout=30, poll_frequency=1):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*location))

    def send_content_to_box(self, location, text):
        # 输入操作
        self.get_element(location).clear()
        self.get_element(location).send_keys(text)

    def click_btn(self, location):
        # 点击操作
        self.get_element(location).click()

    def swipe_screen(self, con):
        """
        滑动屏幕
        :param con: 1:向上,2:向下,3:向左,4:向右  ****难点****
        """
        screen_size = self.driver.get_window_size()
        width = screen_size.get("width")
        height = screen_size.get("height")
        if con == 1:
            time.sleep(2)
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2)
        if con == 2:
            time.sleep(2)
            self.driver.swipe(width * 0.5, height * 0.2, width * 0.5, height * 0.8)
        if con == 3:
            time.sleep(2)
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5)
        if con == 4:
            time.sleep(2)
            self.driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5)

    def screen_shot(self, name="截图"):
        """截图"""
        scree_shot_name = "./image" + os.sep + "{}.png".format(int(time.time()))  # ****难点****
        self.driver.get_screenshot_as_file(scree_shot_name)
        with open(scree_shot_name, "rb") as f:
            """将截图加到报告中"""
            allure.attach(name, f.read(), allure.attach_type.PNG)

    def get_toast(self, toast):
        """
        获取toast消息
        :param toast:toast消息的部分内容
        :return: toast消息的全部内容
        """
        location = (By.XPATH, "//*[contains(@text,'{}')]".format(toast))
        return self.get_element(location, timeout=5, poll_frequency=1).text
