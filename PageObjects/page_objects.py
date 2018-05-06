# -*- coding: utf-8 -*-
from PageObjects.page import Page
from Components.main_group_page_components import (ShopMainPage,
                                                   GroupTopMenu)
from Components.theme_page_components import (ThemeForm)
from Components.group_page_components import (Popup)
from Components.auth_page_components import (AuthForm)
from Components.main_page_components import (LeftMenu)


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)


class MainPage(Page):
    @property
    def left_menu(self):
        return LeftMenu(self.driver)


class GroupsPage(Page):
    @property
    def popup(self):
        return Popup(self.driver)


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
