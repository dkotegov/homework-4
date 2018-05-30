# -*- coding: utf-8 -*-
from Components.component import Component


class CreateGroupsPopup(Component):
    CREATE_GROUP = '//div[@class="create-group"]//a'
    CREATE_SHOP = '//a[contains(@href,"SHOP")]'

    SHOP_NAME = '//input[@id="field_name"]'
    GAMES_SUBCATEGORY = '//select[@id="field_pageMixedCategory"]/option[@value="subcatVal12006"]'
    SUBMIT = '//input[@id="hook_FormButton_button_create"]'

    def open(self):
        super(CreateGroupsPopup, self).click_element(self.CREATE_GROUP)

    def create_shop(self):
        super(CreateGroupsPopup, self).click_element(self.CREATE_SHOP)

    def set_shop_name(self, shop_name):
        super(CreateGroupsPopup, self).input_text_to_element(self.SHOP_NAME, shop_name)

    def set_subcategory(self):
        super(CreateGroupsPopup, self).click_element(self.GAMES_SUBCATEGORY)

    def submit(self):
        super(CreateGroupsPopup, self).click_element(self.SUBMIT)
