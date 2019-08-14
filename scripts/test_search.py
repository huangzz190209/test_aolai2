import time
import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestShopCart:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize("args",analyze_file("search_data.yaml","test_search"))
    def test_search(self,args):
        keyword = args["keyword"]
        # 首页，如果没有登录就登录
        self.page.first.is_not_login(self.page)
        # 我 - 点击首页
        self.page.first.click_home()
        # 首页 - 点击放大镜
        self.page.first.click_search()
        # 搜索 - 输入文字
        self.page.search.input_keyword(keyword)
        # 搜索 - 点击搜索按钮
        self.page.search.click_search()
        # 搜索 - 返回
        self.page.search.press_back()

        # 断言 搜索的关键字，是不是存在在搜索的页面
        assert self.page.search.is_keyword_exist(keyword)

    def test_search_del(self):
        # 添加搜索记录
        # 首页，如果没有登录就登录
        self.page.first.is_not_login(self.page)
        # 我 - 点击首页
        self.page.first.click_home()
        # 首页 - 点击放大镜
        self.page.first.click_search()
        # 搜索 - 输入文字
        self.page.search.input_keyword("nike")
        # 搜索 - 点击搜索按钮
        self.page.search.click_search()
        # 搜索 - 返回
        self.page.search.press_back()

        # 删除操作
        self.page.search.click_search_del()
        # 断言 搜索记录是否为空
        assert self.page.search.is_search_record_empty()
