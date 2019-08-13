import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction

class FirstPage(BaseAction):
    # 我的
    me_button = By.ID,"com.yunmall.lc:id/tab_me"

    #首页点击我的
    @allure.step(title="点击我的")
    def click_me(self):
        self.click(self.me_button)

    @allure.step(title="如果没有登录先点击我的")
    def is_not_login(self,page):
        # 如果没有登录，先点击我的
        self.click_me()
        if self.driver.current_activity !="com.yunmall.ymctoc.ui.activity.LogonActivity":
            return
        #点击已有账号登录
        page.to_login.click_to_login()
        page.login.input_username("tangqifeng")
        page.login.input_password("123456")
        page.login.click_login_button()


