# -*- coding: utf-8 -*-
from Components.component import Component


class LeftMenuOnMainPage(Component):
    USERNAME = '//a[contains(@data-l,"userPage")]/span'
    GROUPS_ITEM = '//a[contains(@href,"groups")]'

    def get_username(self):
        return super(LeftMenuOnMainPage, self).get_element_text(self.USERNAME)

    def open_groups_page(self):
        super(LeftMenuOnMainPage, self).click_element(self.GROUPS_ITEM)
