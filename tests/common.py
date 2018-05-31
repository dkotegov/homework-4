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
        popup.open()

        popup.create_shop()

        popup.set_shop_name(shop_name)
        popup.set_subcategory()
        popup.submit()

    def remove(self):
        shop_feed_page = self.open_feed_page()

        left_menu = shop_feed_page.left_menu
        left_menu.other_actions()
        left_menu.remove_shop()
        left_menu.submit_removing()

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
        catalog_popup.open_from_catalog_panel()

        catalog_popup.set_name(name)
        catalog_popup.save()
        catalog_popup.waiting_closing()

    def open(self):
        catalog_widget = self.shop_market_page.catalog_widget
        catalog_widget.open_catalog()
        self.catalog_page.catalog_panel.waiting_opening()

    def remove_saving_products(self):
        catalog_panel = self.catalog_page.catalog_panel
        catalog_panel.remove()

        remove_catalog_popup = self.catalog_page.remove_catalog_popup
        remove_catalog_popup.submit_removing()
        remove_catalog_popup.waiting_closing()

    def remove_with_products(self):
        catalog_panel = self.catalog_page.catalog_panel
        catalog_panel.remove()

        remove_catalog_popup = self.catalog_page.remove_catalog_popup
        remove_catalog_popup.remove_products()
        remove_catalog_popup.submit_removing()
        remove_catalog_popup.waiting_closing()


class Product(object):
    def __init__(self, driver):
        self.catalog_page = CatalogPage(driver)

    def create(self, name=u'Товар', price='100', about=u'Описание'):
        create_product_popup = self.catalog_page.create_product_popup
        create_product_popup.open()
        create_product_popup.waiting_opening()

        create_product_popup.set_name(name)
        create_product_popup.set_price(price)
        create_product_popup.set_about(about)

        create_product_popup.submit()
        create_product_popup.waiting_closing()

    def remove(self):
        product_widget = self.catalog_page.product_widget
        product_widget.remove()

        submit_product_action_popup = self.catalog_page.submit_product_action_popup
        submit_product_action_popup.submit()
        submit_product_action_popup.waiting_closing()

    def mark_as_out_of_stock(self):
        product_widget = self.catalog_page.product_widget
        product_widget.mark_as_out_of_stock()

        submit_product_action_popup = self.catalog_page.submit_product_action_popup
        submit_product_action_popup.submit()
        submit_product_action_popup.waiting_closing()

    def return_on_sale(self):
        product_widget = self.catalog_page.product_widget
        product_widget.return_on_sale()

        submit_product_action_popup = self.catalog_page.submit_product_action_popup
        submit_product_action_popup.submit()
        submit_product_action_popup.waiting_closing()

    def pin(self):
        product_widget = self.catalog_page.product_widget
        product_widget.pin()
        product_widget.waiting_pin()

    def unpin(self):
        product_widget = self.catalog_page.product_widget
        product_widget.unpin()
        product_widget.waiting_unpin()
