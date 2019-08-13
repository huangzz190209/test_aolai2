import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SettingPage(BaseAction):
    # 关于百年奥莱
    about_aolai_button = By.XPATH,"//*[@text='关于百年奥莱']"
    # 清理缓存按钮
    clear_cache_button= By.XPATH,"//*[@text = '清理缓存']"
    # 地址管理
    address_list_button = By.XPATH,"//*[@text='地址管理']"

    #点击关于百年奥莱
    @allure.step(title="点击关于百年奥莱")
    def click_about_aolai_button(self):
        # 需要边滑边找
        self.find_element_scroll(self.about_aolai_button).click()

    #点击清理缓存
    @allure.step(title="点击清理缓存")
    def click_clear_cache(self):
        self.find_element_scroll(self.clear_cache_button).click()

    #点击地址管理
    @allure.step(title="点击地址管理")
    def click_address_list(self):
        self.find_element_scroll(self.address_list_button).click()

