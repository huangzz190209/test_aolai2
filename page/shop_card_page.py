from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure

class ShopCartPage(BaseAction):

    #全选按钮
    select_all_button = By.ID,"com.yunmall.lc:id/iv_select_all"
    #编辑按钮
    edit_button = By.ID,"com.yunmall.lc:id/tv_right_second"
    #完成按钮
    commit_button = By.XPATH,"//*[@text='完成']"
    #加号按钮
    add_button = By.ID,"com.yunmall.lc:id/iv_add"
    #单价特征
    price_feature = By.ID,"com.yunmall.lc:id/tv_price"
    #总价特征
    all_price_feature = By.ID,"com.yunmall.lc:id/tv_count_money"

    #点击全选
    @allure.step(title="点击全选按钮")
    def click_select_all(self):
        self.click(self.select_all_button)
    #点击编辑
    @allure.step(title="点击编辑")
    def click_edit(self):
        self.click(self.edit_button)
    #点击完成
    @allure.step(title="点击完成")
    def click_commit(self):
        self.click(self.commit_button)
    #点击加号
    @allure.step(title="点击加号")
    def click_add(self):
        self.click(self.add_button)

    #处理价格
    @allure.step(title="处理价格")
    def del_with_price(self,price):
        return float(price[2:])

    #获取单价
    @allure.step(title="获取单价")
    def get_price(self):
        #获取到价格￥ 28.50
        price_text = self.get_text(self.price_feature)
        # 通过 deal_with_price 去掉前面的人民币符号，并且转化成float类型
        return self.del_with_price(price_text)

    #获取所有价格
    @allure.step(title="获取所有价格")
    def get_all_price(self):
        price_text = self.get_text(self.all_price_feature)
        return self.del_with_price(price_text)


    #删除按钮
    delete_button= By.XPATH,"//*[@text='删除']"
    #确认按钮
    yes_button = By.XPATH,"//*[@text='确认']"

    #点击删除
    @allure.step(title="在购物车点击删除")
    def click_delete(self):
        self.click(self.delete_button)

    #点击确认
    @allure.step(title="在购物车点击确认")
    def click_yes(self):
        self.click(self.yes_button)

    #判断购物车是否为空
    def is_shop_cart_empty(self):
        xpath = By.XPATH,"//*[contains(@text,'购物车还是空的')]"
        return self.is_feature_exist(xpath)



