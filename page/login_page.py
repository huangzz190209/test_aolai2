from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):
    # 用户名
    username = By.ID,"com.yunmall.lc:id/logon_account_textview"
    # 密码
    password = By.ID,"com.yunmall.lc:id/logon_password_textview"
    # 登陆
    login_button = By.ID,"com.yunmall.lc:id/logon_button"

    #输入用户名
    def input_username(self,text):
        self.input(self.username,text)
    # 输入密码
    def input_password(self,text):
        self.input(self.password,text)
    #点击登录
    def click_login_button(self):
        self.click(self.login_button)