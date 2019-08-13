import time

from base.base_driver import init_driver
from page.page import Page


class TestVersionUpdata:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_version_updata(self):
        # 现在首页点击我的，查看是否登录
        self.page.first.is_not_login(self.page)
        # 如果登录，我 点击 设置
        self.page.me.click_setting_button()
        # 点击百年奥莱
        self.page.setting.click_about_aolai_button()
        #点击版本更新
        self.page.abouta_aolai.click_new_button()
        assert self.page.abouta_aolai.is_toast_exist("当前已是最新版本")