# -*- coding: utf-8 -*-
import os

from selenium.webdriver import DesiredCapabilities, Remote

from Components.component import Component
from PageObjects.page_objects import AuthPage, MainPage, GroupsPage, ShopFeedPage, ShopForumPage, ShopMarketPage, \
    CatalogPage


def get_driver():
    browser = os.environ.get('BROWSER', 'CHROME')
    return Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=getattr(DesiredCapabilities, browser).copy()
    )


class Auth(Component):
    LOGIN = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

    def sign_in(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_login(self.LOGIN)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()


class Main(Component):
    def open_groups_page(self):
        main_page = MainPage(self.driver)
        main_page.left_menu.open_groups_page()


class Shop(Component):
    def create(self, shop_name=u'Ларек-Марек'):
        groups_page = GroupsPage(self.driver)
        popup = groups_page.popup
        popup.open_popup()

        popup.create_shop()

        popup.set_shop_name(shop_name)
        popup.set_subcategory()
        popup.submit_creation()

    def remove(self):
        shop_feed_page = self.open_feed_page()

        left_menu = shop_feed_page.left_menu
        left_menu.other_actions()
        left_menu.remove_shop()
        left_menu.submit_remove()

    def open_feed_page(self):
        shop_feed_page = ShopFeedPage(self.driver)
        shop_feed_page.top_menu.open_feed_page()
        return shop_feed_page

    def open_forum_page(self):
        shop_forum_page = ShopForumPage(self.driver)
        shop_forum_page.top_menu.open_forum_page()
        return shop_forum_page

    def open_market_page(self):
        shop_market_page = ShopMarketPage(self.driver)
        shop_market_page.top_menu.open_market_page()
        return shop_market_page


class Catalog(object):
    def __init__(self, driver):
        self.shop_market_page = ShopMarketPage(driver)
        self.catalog_page = CatalogPage(driver)

    def create(self, name=u'Каталог'):
        catalog_popup = self.shop_market_page.catalog_popup
        catalog_popup.open_popup_from_catalog_panel()

        catalog_popup.set_catalog_name(name)
        catalog_popup.save()
        catalog_popup.waiting_until_close()

    def open(self):
        catalog_widget = self.shop_market_page.catalog_widget
        catalog_widget.open_catalog()
        self.catalog_page.catalog_panel.waiting_opening()

    def remove(self):
        self.open()

        catalog_panel = self.catalog_page.catalog_panel
        catalog_panel.remove_catalog()

        remove_catalog_popup = self.catalog_page.remove_popup
        remove_catalog_popup.submit_remove()
        remove_catalog_popup.waiting_until_close()


class Product(object):
    def __init__(self, driver):
        self.catalog_page = CatalogPage(driver)

    def create(self, name=u'Товар', price='100', about=u'Описание'):
        product_popup = self.catalog_page.product_popup
        product_popup.open_popup()
        product_popup.waiting_opening()

        product_popup.set_product_name(name)
        product_popup.set_product_price(price)
        product_popup.set_product_about(about)

        product_popup.submit()
        product_popup.waiting_until_close()
