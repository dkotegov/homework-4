# -*- coding: utf-8 -*-

from components.base_component import BaseComponent
from selenium.common.exceptions import NoSuchElementException, TimeoutException



class StatusesForm(BaseComponent):
    INPUT_STATUS_PLACEHOLDER="//div[@class='input_placeholder']"
    INPUT_STATUS_POSTING_PLACEHOLDER = "//div[@class='posting_itx emoji-tx h-mod js-ok-e ok-posting-handler']"
    MARK_BUTTON = "//div[@class='ucard-mini_cnt']//div[@class='ucard-mini_cnt_i ellip' and text()='"
    BLOCKED_MARK_BUTTON = "//div[@class='ucard-mini_info' and text()='"

    def input_status_placeholder(self): 
        return self.get_clickable_element(self.INPUT_STATUS_PLACEHOLDER)

    def input_status_posting_placeholder(self): 
        return self.get_clickable_element(self.INPUT_STATUS_POSTING_PLACEHOLDER)

    def mark_button(self, name): 
        return self.get_clickable_element(self.MARK_BUTTON + name + "']")

    def blocked_mark_button(self):
        text = u'не разрешает отмечать себя'
        return self.get_visibility_element(self.BLOCKED_MARK_BUTTON + text + "']")
