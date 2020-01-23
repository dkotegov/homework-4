# -*- coding: utf-8 -*-
from tests.pages.BasicPage import BasicPage


class TopMenuManager(BasicPage):
    top_menu_move = 'div.portal-menu-element_move'
    top_menu_trash = 'div.portal-menu-element_remove'

    inbox_menu_item = "div.list-item[title='Входящие']"

    def remove_letter_from_menu(self):
        elem = self.wait_render(self.top_menu_trash)
        elem.click()

    def click_top_menu_move_letter_button(self):
        elem = self.wait_render(self.top_menu_move)
        elem.click()

    def click_inbox_menu_item(self):
        elem = self.wait_render(self.inbox_menu_item)
        elem.click()
