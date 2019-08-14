import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressListPage(BaseAction):
    # 新增地址
    add_address_button = By.XPATH,"//*[@text='新增地址']"
    # 默认姓名和电话的信息特征
    default_recipet_name_text_view = By.ID,"com.yunmall.lc:id/receipt_name"
    # 默认特征
    is_default_feature = By.ID,"com.yunmall.lc:id/address_is_default"
    #编辑按钮
    edit_button = By.XPATH,"//*[@text='编辑']"
    #删除按钮
    delete_button = By.XPATH,"//*[@text='删除']"
    #确定按钮
    commit_button = By.XPATH,"//*[@text='确认']"



    # 点击新增地址
    @allure.step(title="点击新增地址")
    def click_add_address(self):
        self.find_element_scroll(self.add_address_button).click()

    #获取 默认的姓名和电话的文字信息
    @allure.step(title="获取默认的姓名和电话的文字信息")
    def get_default_recipet_name_text(self):
        return self.get_text(self.default_recipet_name_text_view)

    # 判断默认标记是否存在
    @allure.step(title="默认标记是否存在")
    def is_dafault_feature_exist(self):
        return self.is_feature_exist(self.is_default_feature)

    #点击默认地址
    @allure.step(title="点击默认的地址")
    def click_default_address(self):
        self.click(self.is_default_feature)

    #判断删除按钮是否存在
    @allure.step(title="判断删除按钮是否存在")
    def is_delete_address_exist(self):
        return self.is_feature_exist(self.delete_button)

    #点击编辑
    @allure.step(title="点击编辑按钮")
    def click_edit(self):
        self.click(self.edit_button)

    #点击删除
    @allure.step(title="点击删除按钮")
    def click_delete(self):
        self.click(self.delete_button)

    #点击确定
    @allure.step(title="点击确定按钮")
    def click_commit(self):
        self.click(self.commit_button)
