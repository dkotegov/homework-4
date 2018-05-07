# -*- coding: utf-8 -*-
from Components.component import Component


class TopicPopup(Component):
    CREATE_THEME = '//a[contains(@data-l, "OpenPostingPopup")]'
    THEME_TEXT = '//div[@data-module="postingForm/mediaText"]'
    SUBMIT = '//div[@data-action="submit"]'

    def open_popup(self):
        super(TopicPopup, self).click_element(self.CREATE_THEME)

    def set_text(self, text="Default text"):
        super(TopicPopup, self).input_text_to_element(self.THEME_TEXT, text)

    def submit(self):
        super(TopicPopup, self).click_element_without_waiting(self.SUBMIT)
