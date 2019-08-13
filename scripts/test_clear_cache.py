import time

from base.base_driver import init_driver
from page.page import Page


class TestClearCache:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_clear_cache(self):
        # 如果没有登录就先登录
        self.page.first.is_not_login(self.page)
        self.page.me.click_setting_button()
        self.page.setting.click_clear_cache()
        assert self.page.setting.is_toast_exist("清理成功")