from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AboutAolaiPage(BaseAction):
    # 版本更新
    new_buttom = By.XPATH,"//*[@text='版本更新']"

    #点击版本更新
    def click_new_button(self):
        self.click(self.new_buttom)