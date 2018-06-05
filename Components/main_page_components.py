# -*- coding: utf-8 -*-
import re

from Components.component import Component


class LeftMenuOnMainPage(Component):
    USERNAME = '//a[contains(@data-l,"userPage")]/span'
    GROUPS_ITEM = '//a[contains(@href,"groups")]'
    GROUPS_BLOCK = '//div[@id="hook_Block_MyGroupsNavBlock"]/div'
    NUMBER_OF_GROUPS = '//a[starts-with(text(), "Все мои группы")]'

    def get_username(self):
        return super(LeftMenuOnMainPage, self).get_element_text(self.USERNAME)

    def open_groups_page(self):
        super(LeftMenuOnMainPage, self).click_element(self.GROUPS_ITEM)

    def are_there_any_groups(self):
        return super(LeftMenuOnMainPage, self).is_exist_element(self.GROUPS_BLOCK)

    def get_number_of_groups(self):
        number_of_groups_str = super(LeftMenuOnMainPage, self).get_element_text(self.NUMBER_OF_GROUPS)
        return int(re.search(r'\d+', number_of_groups_str).group())
