# -*- coding: utf-8 -*-
from PageObjects.page import Page
from Components.auth_form import AuthForm
from Components.create_groups_popup import CreateGroupsPopup
from Components.left_menu_on_main_page import LeftMenuOnMainPage
from Components.main_group_page_components import ShopMainPage, GroupTopMenu
from Components.shop_page_components import TopMenu, ShopPage
from Components.theme_page_components import ThemeForm


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


class MainGroupPage(Page):
    @property
    def group_top_menu(self):
        return GroupTopMenu(self.driver)

    @property
    def shop_main_page(self):
        return ShopMainPage(self.driver)


class ThemesPage(Page):
    @property
    def theme_form(self):
        return ThemeForm(self.driver)


class ShopAdminPage(Page):
    @property
    def top_menu(self):
        return TopMenu(self.driver)

    @property
    def shop_main_page(self):
        return ShopPage(self.driver)
