import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction

class FirstPage(BaseAction):
    # 我
    me_button = By.ID,"com.yunmall.lc:id/tab_me"

    #分类
    category_button = By.ID,"com.yunmall.lc:id/tab_category"

    # 购物车
    shop_cart_button = By.ID,"com.yunmall.lc:id/tab_shopping_cart"

    # 首页
    home_button = By.ID, "com.yunmall.lc:id/tab_home"

    # 放大镜 按钮
    search_button = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"

    #首页点击我
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

    #点击分类
    @allure.step(title="点击分类按钮")
    def click_category(self):
        self.click(self.category_button)

    #点击购物车
    @allure.step(title="点击购物车")
    def click_shop_cart(self):
        self.click(self.shop_cart_button)

    #点击首页
    @allure.step(title='主页 点击 首页')
    def click_home(self):
        self.click(self.home_button)

    #点击放大镜
    @allure.step(title='主页 点击 放大镜')
    def click_search(self):
        self.click(self.search_button)

