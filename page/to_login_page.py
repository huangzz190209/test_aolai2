from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ToLoginPage(BaseAction):
    #已有账号去登陆
    to_login_button = By.ID,"com.yunmall.lc:id/textView1"

    #点击已有账号去登陆
    def click_to_login(self):
        self.click(self.to_login_button)
