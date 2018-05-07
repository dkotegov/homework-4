# -*- coding: utf-8 -*-
from Components.feed_page_components import TopMenuOnShopPage, LeftMenuOnShopFeedPage, HeaderOnShopFeedPage
from PageObjects.page import Page
from Components.auth_form import AuthForm
from Components.groups_page_components import CreateGroupsPopup
from Components.main_page_components import LeftMenuOnMainPage
from Components.forum_page_components import TopicPopup


class AuthPage(Page):
    PATH = ''

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
