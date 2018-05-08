# -*- coding: utf-8 -*-
import os

from selenium.webdriver import DesiredCapabilities, Remote

from Components.component import Component
from PageObjects.page_objects import AuthPage, MainPage, GroupsPage, ShopFeedPage, ShopForumPage, ShopMarketPage


def getDriver():
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
