import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1.0):
        by = feature[0]
        value = feature[1]

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    def find_elements(self, feature, timeout=10, poll=1.0):
        by = feature[0]
        value = feature[1]

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, text):
        self.find_element(feature).send_keys(text)

    def get_text(self, feature):
        return self.find_element(feature).text


    def is_toast_exist(self,message):
        message_xpath = By.XPATH,"//*[contains(@text,'%s')]" % message
        try:
            self.find_element(message_xpath, 5, 0.1)
            return True
        except TimeoutException:
            return False

    def get_toast_text(self, message):
        if self.is_toast_exist(message):
            message_xpath = By.XPATH, "//*[contains(@text,'%s')]" % message
            return self.find_element(message_xpath, 5, 0.1).text
        else:
            raise Exception("toast未出现，请检查参数是否正确或toast有没有出现在屏幕上")

    #滑动一次页面
    def scroll_one_time(self,direction="up"):
        width = self.driver.get_window_size()["width"]
        height = self.driver.get_window_size()["height"]
        # 中心点
        center_x = width / 2
        center_y = height / 2

        # X轴的四分之一处
        left_x = width / 4 * 1
        # Y轴在二分之一处
        left_y = center_y
        # X轴在四分之三处
        right_x = width / 4 * 3
        # Y轴在二分之一处
        right_y = center_y

        # X轴在二分之一处
        top_x = center_x
        # Y轴在四分之一处
        top_y = height / 4 * 1
        # X轴在二分之一处
        bottom_x = center_x
        # Y轴在四分之三处
        bottom_y = height / 4 * 3

        if direction == "up":
            # 往上滑，从Y轴的四分之三处滑到四分之一处，横轴一直在二分之一处
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y, 3000)
        elif direction == "down":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y, 3000)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y, 3000)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y, 3000)
        else:
            raise Exception("请输入：up/down/left/right")

    # 边滑边找元素
    def find_element_scroll(self,feature, direction="up"):
        """
        边滑边找 某个元素的特征
        :param feature: 元素的特征
        :param direction: 方向
            "up"：从下往上
            "down"：从上往下
            "right"：从左往右
            "left"：从右往左
        :return:
        """
        page_source = ""
        while True:
            try:
                return self.find_element(feature)
            except Exception:
                self.scroll_one_time(direction)
                if self.driver.page_source == page_source:
                    print("到底了")
                    break
                page_source = self.driver.page_source


    def is_keyword_in_page_source(self,keyword,timeout=10,poll=0.1):
        """
        如果不能成为会员，有输入邀请码的字符串，返回True
        :return:
        """
        end_time = time.time()+timeout
        while True:
            if end_time < time.time():
                return False
            if keyword in self.driver.page_source:
                return True

            time.sleep(poll)

    def is_feature_exist(self,feature):
        try:
            self.find_element(feature)
            return True
        except TimeoutException:
            return False

    def press_back(self):
        self.driver.press_keycode(4)

    def press_enter(self):
        self.driver.press_keycode(66)