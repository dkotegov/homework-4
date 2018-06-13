# -*- coding: utf-8 -*-
from Components.auth_form import AuthForm
from Components.groups_page import CreateGroupPopup
from Components.main_page import LeftMenuOnMainPage
from Components.shop_feed_page import TopMenuOnShopPage, LeftMenuOnShopFeedPage, HeaderOnShopFeedPage
from Components.shop_market_page import CatalogPopup, CatalogWidget, CatalogPanel, RemoveCatalogPopup, \
    CatalogCounter, ProductCounter, CatalogStub, CreateProductPopup, ProductWidget, ProductStub, \
    SubmitProductActionPopup
from Components.shop_topic_page import TopicPopup, TopicWidget, TopicTags
from PageObjects.page import Page


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
        return CreateGroupPopup(self.driver)


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

    @property
    def topic_widget(self):
        return TopicWidget(self.driver)

    @property
    def topic_tags(self):
        return TopicTags(self.driver)


class ShopMarketPage(Page):
    @property
    def top_menu(self):
        return TopMenuOnShopPage(self.driver)

    @property
    def catalog_popup(self):
        return CatalogPopup(self.driver)

    @property
    def product_popup(self):
        return CreateProductPopup(self.driver)

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
    def catalog_popup(self):
        return CatalogPopup(self.driver)

    @property
    def remove_catalog_popup(self):
        return RemoveCatalogPopup(self.driver)

    @property
    def submit_product_action_popup(self):
        return SubmitProductActionPopup(self.driver)

    @property
    def create_product_popup(self):
        return CreateProductPopup(self.driver)

    @property
    def product_widget(self):
        return ProductWidget(self.driver)
