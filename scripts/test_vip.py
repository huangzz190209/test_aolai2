import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page




class TestVip:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize("args",analyze_file("vip_data.yaml","test_vip"))
    def test_vip(self,args):
        # 解析
        keyword = args["keyword"]
        expect = args["expect"]

        # 如果没有登录就先登录
        self.page.first.is_not_login(self.page)
        # 我 点击 加入vip
        self.page.me.click_be_vip()
        print(self.driver.contexts)
        # 切换web环境
        self.driver.switch_to.context("WEBVIEW_com.yunmall.lc")
        #vip输入邀请码
        self.page.vip.input_invite(keyword)
        # 点击加入会员
        self.page.vip.click_be_vip()

        # 断言,"邀请码输入不正确"是否在page_source中
        assert self.page.vip.is_keyword_in_page_source(expect)

        # 切换原生环境
        self.driver.switch_to.context("NATIVE_APP")

























    # def is_can_not_be_vip(self,timeout=10,poll=0.1):
    #     """
    #     如果不能成为会员，有输入邀请码的字符串，返回True
    #     :return:
    #     """
    #     end_time = time.time()+timeout
    #     while True:
    #         if end_time < time.time():
    #             return False
    #         if "邀请码输入不正确" in self.driver.page_source:
    #             return True
    #
    #         time.sleep(poll)



