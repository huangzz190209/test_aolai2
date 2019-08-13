import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestAddress:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize("args",analyze_file("address_data.yaml","test_add_address"))
    def test_add_address(self,args):
        # 解析
        name = args["name"]
        phone = args["phone"]
        info = args["info"]
        post_code = args["post_code"]
        toast = args["toast"]
        # 如果没有登录就先登录
        self.page.first.is_not_login(self.page)
        # 点击设置
        self.page.me.click_setting_button()
        #点击地址管理
        self.page.setting.click_address_list()
        #点击新增地址
        self.page.address_list.click_add_address()
        # 新增地址 输入 姓名
        self.page.edit_address.input_name_edit(name)
        # 新增地址 输入 电话
        self.page.edit_address.input_phone_edit(phone)
        # 新增地址 输入 详细地址
        self.page.edit_address.input_info_edit(info)
        # 新增地址 输入 邮编
        self.page.edit_address.input_post_edit(post_code)
        # 新增地址 勾选 设为默认地址
        self.page.edit_address.click_default_address()
        time.sleep(3)
        # 新增地址 选择一个随机的区域
        self.page.edit_address.choose_region()
        # 新增地址 点击 保存
        self.page.edit_address.click_save()
        #断言  "张三  18888888888"
        if toast is None:
            assert self.page.address_list.get_default_recipet_name_text() =="%s  %s" % (name, phone)
        else:
            assert self.page.edit_address.get_toast_text(toast)
        time.sleep(5)


     #测试编辑地址
    def test_edit_address(self):
        #首页，如果没有登录就登录
        self.page.first.is_not_login(self.page)
        # 我 点击 设置
        self.page.me.click_setting_button()
        #设置 点击 地址管理
        self.page.setting.click_address_list()

        if not self.page.address_list.is_dafault_feature_exist():
            # 点击新增地址
            self.page.address_list.click_add_address()
            # 新增地址 输入 姓名
            self.page.edit_address.input_name_edit("张三")
            # 新增地址 输入 电话
            self.page.edit_address.input_phone_edit("18888888888")
            # 新增地址 输入 详细地址
            self.page.edit_address.input_info_edit("三单元 504")
            # 新增地址 输入 邮编
            self.page.edit_address.input_post_edit("100000")
            # 新增地址 勾选 设为默认地址
            self.page.edit_address.click_default_address()
            # 新增地址 选择一个随机的区域
            self.page.edit_address.choose_region()
            # 新增地址 点击 保存
            self.page.edit_address.click_save()

        #进入默认地址(进入edit_adress界面)
        self.page.address_list.click_default_address()
        # 重新输入 姓名
        self.page.edit_address.input_name_edit("张三")
        # 重新输入 输入 电话
        self.page.edit_address.input_phone_edit("18888888888")
        # 重新输入 输入 详细地址
        self.page.edit_address.input_info_edit("三单元 504")
        # 重新输入 输入 邮编
        self.page.edit_address.input_post_edit("10000")
        # 重新输入 选择一个随机的区域
        self.page.edit_address.choose_region()
        # 重新输入 点击 保存
        self.page.edit_address.click_save()
        #断言 是否出现保存成功
        assert self.page.edit_address.is_toast_exist("保存成功")
        time.sleep(5)
    #测试删除地址
    def test_delete_address(self):
        #如果没有登录就先登录
        self.page.first.is_not_login(self.page)
        #我 点击 设置
        self.page.me.click_setting_button()
        #点击地址管理
        self.page.setting.click_address_list()
        #断言 是否有地址可删除(默认标记是否存在)
        assert self.page.address_list.is_dafault_feature_exist(),"默认标记不存在，没有地址可以删除"
        # 循环删除
        for i in range(10):
            #点击编辑
            self.page.address_list.click_edit()
            #判断删除是否存在
            if not self.page.address_list.is_delete_address_exist():
            # 如果不存在，直接返回
                break
            #如果存在，点击
            self.page.address_list.click_delete()
            self.page.address_list.click_commit()

        #循环10次之后，点击编辑,再次确认是否都删除了
        self.page.address_list.click_edit()
        #断言 删除按钮是否存在 如果不存在则通过，如果存在则有问题
        assert not self.page.address_list.is_delete_address_exist(),"收货地址没有删除完毕"
        time.sleep(5)







