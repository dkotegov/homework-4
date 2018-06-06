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


class Main(object):
    def __init__(self, driver):
        self.main_page = MainPage(driver)

    def get_username(self):
        return self.main_page.left_menu.get_username()

    def open_groups_page(self):
        self.main_page.left_menu.open_groups_page()

    def are_there_any_groups(self):
        return self.main_page.left_menu.are_there_any_groups()

    def get_number_of_groups(self):
        return self.main_page.left_menu.get_number_of_groups()


class Shop(object):
    def __init__(self, driver):
        self.shop_feed_page = ShopFeedPage(driver)
        self.shop_forum_page = ShopForumPage(driver)
        self.shop_market_page = ShopMarketPage(driver)
        self.groups_page = GroupsPage(driver)

    @property
    def market_page(self):
        return self.shop_market_page

    def open_feed_page(self):
        self.shop_feed_page.top_menu.open_feed_page()

    def open_forum_page(self):
        self.shop_forum_page.top_menu.open_forum_page()

    def open_market_page(self):
        self.shop_market_page.top_menu.open_market_page()

    def get_name(self):
        return self.shop_feed_page.header.get_shop_name()

    def get_category(self):
        return self.shop_feed_page.header.get_shop_category()

    def create(self, shop_name=u'Ларек-Марек'):
        popup = self.groups_page.popup
        popup.open()

        popup.create_shop()

        popup.set_shop_name(shop_name)
        popup.set_subcategory()
        popup.submit()

    def remove(self):
        self.open_feed_page()
        left_menu = self.shop_feed_page.left_menu

        left_menu.remove_shop()
        left_menu.submit_removing()


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

    def create_with_image(self, image_name='image_512x512.jpg'):
        catalog_popup = self.shop_market_page.catalog_popup
        catalog_popup.open_from_catalog_panel()

        catalog_popup.set_name()
        catalog_popup.upload_catalog_image(image_name)
        catalog_popup.waiting_image_upload()
        creating_image_src = catalog_popup.get_image_src()
        catalog_popup.save()
        catalog_popup.waiting_closing()

        return creating_image_src

    def open(self):
        catalog_widget = self.shop_market_page.catalog_widget
        catalog_widget.open_catalog()
        self.catalog_page.catalog_panel.waiting_opening()
        return self.catalog_page

    def get_name(self):
        return self.catalog_page.catalog_panel.get_name()

    def set_name(self, other_name=u'Другой каталог'):
        self.catalog_page.catalog_panel.edit()
        catalog_popup = self.catalog_page.catalog_popup
        catalog_popup.set_name(other_name)
        catalog_popup.save()
        catalog_popup.waiting_closing()

    def set_image(self, image_name='image_512x512.jpg'):
        self.catalog_page.catalog_panel.edit()
        catalog_popup = self.catalog_page.catalog_popup

        catalog_popup.upload_catalog_image(image_name)
        catalog_popup.waiting_image_upload()
        upload_image_src = catalog_popup.get_image_src()
        catalog_popup.save()
        catalog_popup.waiting_closing()

        return upload_image_src

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
