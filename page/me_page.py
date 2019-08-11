import time
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):
    #昵称
    nick_name = By.ID,"com.yunmall.lc:id/tv_user_nikename"
    # 设置按钮
    setting_buton = By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"
    # 加入超级VIP
    be_vip_button = By.XPATH, "//*[@text='加入超级VIP']"

    #获取昵称
    def get_nick_name(self):
        return self.get_text(self.nick_name)

    #点击设置按钮
    def click_setting_button(self):
        self.click(self.setting_buton)

    #点击加入超级VIP
    def click_be_vip(self):
        self.find_element_scroll(self.be_vip_button).click()
        time.sleep(10)

