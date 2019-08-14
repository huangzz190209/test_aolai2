import time

from base.base_driver import init_driver
from page.page import Page


class TestShopCart:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_add_shop_cart(self):
        # 首页，如果没有登录就登录
        self.page.first.is_not_login(self.page)
        # 首页 - 分类
        self.page.first.click_category()
        # 分类 - 商品列表
        self.page.category.click_goods_list()
        # 商品列表 - 商品详情
        self.page.goods_list.click_goods()
        #获取商品标题
        goods_title = self.page.goods_detail.get_goods_title_text()
        # 商品详情 - 加入购物车
        self.page.goods_detail.click_add_shop_cart()
        #商品详情 — 选择规格
        self.page.goods_detail.click_spec()
        #商品详情 — 购物车
        self.page.goods_detail.click_shop_cart()
        time.sleep(3)
        #断言
        assert self.page.goods_detail.is_goods_title_exist(goods_title)

    def test_shop_cart_price(self):
        # 首页，如果没有登录就登录
        self.page.first.is_not_login(self.page)
        # 首页 - 点击购物车
        self.page.first.click_shop_cart()
        # 购物车 - 点击全选
        self.page.shop_cart.click_select_all()
        # 购物车 - 记录总价
        all_price = self.page.shop_cart.get_all_price()
        # 购物车 - 点击编辑
        self.page.shop_cart.click_edit()
        # 购物车 - 点击加号
        self.page.shop_cart.click_add()
        # 购物车 - 点击完成
        self.page.shop_cart.click_commit()
        # 购物车 - 获取单价
        price = self.page.shop_cart.get_price()
        # 断言 当前总价 = 记录总价 + 单价
        assert self.page.shop_cart.get_all_price() == all_price + price

    #测试购物车，如果有商品就删除，没有商品就添加
    def test_del_shop_cart(self):
        #首页，如果没有登录就登录
        self.page.first.is_not_login(self.page)
        #首页点击购物车
        self.page.first.click_shop_cart()

        #如果购物车没有商品，就添加商品
        if self.page.shop_cart.is_shop_cart_empty():
            # 首页 - 分类
            self.page.first.click_category()
            # 分类 - 商品列表
            self.page.category.click_goods_list()
            # 商品列表 - 商品详情
            self.page.goods_list.click_goods()
            # 获取商品标题
            goods_title = self.page.goods_detail.get_goods_title_text()
            # 商品详情 - 加入购物车
            self.page.goods_detail.click_add_shop_cart()
            # 商品详情 — 选择规格
            self.page.goods_detail.click_spec()
            #两次返回
            self.page.goods_detail.press_back()
            time.sleep(2)
            self.page.goods_detail.press_back()
            #首页点击购物车
            self.page.first.click_shop_cart()

        #购物车点击全选
        self.page.shop_cart.click_select_all()
        #点击编辑
        self.page.shop_cart.click_edit()
        #点击删除
        self.page.shop_cart.click_delete()
        #点击确认
        self.page.shop_cart.click_yes()

        #断言 toast是不是为  删除成功
        assert self.page.shop_cart.is_toast_exist("删除成功")
        #断言  当前页面是不是有一个叫做"购物车还是空的"
        assert self.page.shop_cart.is_shop_cart_empty()



