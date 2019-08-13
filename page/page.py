from base.base_driver import init_driver
from page.about_aolai_page import AboutAolaiPage
from page.address_list_page import AddressListPage
from page.edit_address_page import EditAddressPage
from page.first_page import FirstPage
from page.login_page import LoginPage
from page.me_page import MePage
from page.setting_page import SettingPage
from page.to_login_page import ToLoginPage
from page.vip_page import VipPage


class Page:
    def __init__(self,driver):
        self.driver = driver

    @property
    def first(self):
        return FirstPage(self.driver)

    @property
    def to_login(self):
        return ToLoginPage(self.driver)

    @property
    def login(self):
        return LoginPage(self.driver)

    @property
    def me(self):
        return MePage(self.driver)

    @property
    def setting(self):
        return SettingPage(self.driver)

    @property
    def abouta_aolai(self):
        return AboutAolaiPage(self.driver)

    @property
    def vip(self):
        return VipPage(self.driver)

    @property
    def address_list(self):
        return AddressListPage(self.driver)

    @property
    def edit_address(self):
        return EditAddressPage(self.driver)

