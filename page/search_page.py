import allure
import time
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SearchPage(BaseAction):
    #输入框
    keyword_deit_text= By.ID,"com.yunmall.lc:id/text_search_keyword"
    #搜索按钮
    search_button = By.ID, "com.yunmall.lc:id/button_search"
    #删除搜索记录 按钮
    search_del_button = By.ID, "com.yunmall.lc:id/search_del"

    #输入关键字
    @allure.step(title='搜索页面 输入 关键字')
    def input_keyword(self,text):
        self.input(self.keyword_deit_text,text)

    # 点击 搜索
    @allure.step(title='搜索页面 点击 搜索')
    def click_search(self):
        self.click(self.search_button)
        time.sleep(2)

    # 点击 搜索记录的删除
    @allure.step(title='搜索页面 点击 删除搜索记录')
    def click_search_del(self):
        self.click(self.search_del_button)

    @allure.step(title='关键字是否存在')
    def is_keyword_exist(self,keyword):
        xpath = By.XPATH,"//*[//*[@resource-id='com.yunmall.lc:id/keyayout']/*/*[@text='%s']" % keyword
        return self.is_feature_exist(xpath)

    @allure.step(title='搜索记录是否为空')
    def is_search_record_empty(self):
        feature = By.XPATH, "//*[@text='暂无搜索历史']"
        return self.is_feature_exist(feature)