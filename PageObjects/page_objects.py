# -*- coding: utf-8 -*-
from Components.feed_page_components import TopMenuOnShopPage, LeftMenuOnShopFeedPage, HeaderOnShopFeedPage
from Components.market_page_components import CatalogPopup, CatalogWidget, CatalogPanel, RemoveCatalogPopup, \
    CatalogCounter, ProductCounter, CatalogStub, ProductPopup, ProductWidget, ProductStub, RemoveProductPopup
from PageObjects.page import Page
from Components.auth_form import AuthForm
from Components.groups_page_components import CreateGroupsPopup
from Components.main_page_components import LeftMenuOnMainPage
from Components.forum_page_components import TopicPopup


class AuthPage(Page):
    @property
    def form(self):
        return AuthForm(self.driver)


class MainPage(Page):
    @property
    def left_menu(self):
        return LeftMenuOnMainPage(self.driver)


class GroupsPage(Page):
    @property
    def popup(self):
        return CreateGroupsPopup(self.driver)


class ShopFeedPage(Page):
    @property
    def top_menu(self):
        return TopMenuOnShopPage(self.driver)

    @property
    def left_menu(self):
        return LeftMenuOnShopFeedPage(self.driver)

    @property
    def header(self):
        return HeaderOnShopFeedPage(self.driver)


class ShopForumPage(Page):
    @property
    def top_menu(self):
        return TopMenuOnShopPage(self.driver)

    @property
    def topic_popup(self):
        return TopicPopup(self.driver)


class ShopMarketPage(Page):
    @property
    def top_menu(self):
        return TopMenuOnShopPage(self.driver)

    @property
    def catalog_popup(self):
        return CatalogPopup(self.driver)

    @property
    def product_popup(self):
        return ProductPopup(self.driver)

    @property
    def catalog_widget(self):
        return CatalogWidget(self.driver)

    @property
    def catalog_counter(self):
        return CatalogCounter(self.driver)

    @property
    def product_counter(self):
        return ProductCounter(self.driver)

    @property
    def catalog_stub(self):
        return CatalogStub(self.driver)

    @property
    def product_stub(self):
        return ProductStub(self.driver)

    @property
    def product_widget(self):
        return ProductWidget(self.driver)


class CatalogPage(Page):
    @property
    def catalog_panel(self):
        return CatalogPanel(self.driver)

    @property
    def remove_catalog_popup(self):
        return RemoveCatalogPopup(self.driver)

    @property
    def remove_product_popup(self):
        return RemoveProductPopup(self.driver)

    @property
    def product_popup(self):
        return ProductPopup(self.driver)

    @property
    def product_widget(self):
        return ProductWidget(self.driver)
