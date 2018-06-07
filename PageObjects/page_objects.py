# -*- coding: utf-8 -*-
from Components.auth_form import AuthForm
from Components.feed_page_components import TopMenuOnShopPage, LeftMenuOnShopFeedPage, HeaderOnShopFeedPage
from Components.forum_page_components import (TopicCreationPopup,
                                              TopicListElement,
                                              TopicPopup,
                                              NotifyPanel)
from Components.groups_page_components import CreateGroupsPopup
from Components.keyword_components import KeywordsComponent
from Components.main_page_components import LeftMenuOnMainPage
from Components.market_page_components import CatalogPopup, CatalogWidget, CatalogPanel, RemoveCatalogPopup
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
    def notify_panel(self):
        return NotifyPanel(self.driver)

    @property
    def topic_creation_popup(self):
        return TopicCreationPopup(self.driver)

    @property
    def topic_list_element(self):
        return TopicListElement(self.driver)

    @property
    def topic_popup(self):
        return TopicPopup(self.driver)

    @property
    def keyword_component(self):
        return KeywordsComponent(self.driver)


class ShopMarketPage(Page):
    @property
    def top_menu(self):
        return TopMenuOnShopPage(self.driver)

    @property
    def catalog_popup(self):
        return CatalogPopup(self.driver)

    def catalog_widget(self):
        return CatalogWidget(self.driver)


class CatalogPage(Page):
    @property
    def catalog_panel(self):
        return CatalogPanel(self.driver)

    @property
    def remove_popup(self):
        return RemoveCatalogPopup(self.driver)
