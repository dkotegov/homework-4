# -*- coding: utf-8 -*-

from components.base_component import BaseComponent

class CommunityForm(BaseComponent):

    BUTTON_LEAVE = "//i[@class='tico_img ic ic_exit_arrow']"
    BUTTON_ACCEPT = "//input[@id='hook_FormButton_button_remove']"

    def leave(self):
        self.get_clickable_element(self.BUTTON_LEAVE).click()
        self.get_clickable_element(self.BUTTON_ACCEPT).click()

