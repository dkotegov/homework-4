# -*- coding: utf-8 -*-

from components.base_component import BaseComponent
from selenium.common.exceptions import NoSuchElementException, TimeoutException



class PhotoForm(BaseComponent):
    COMMENT_INPUT = "//div[@class = 'itx js-comments_add js-ok-e comments_add-ceditable ']"
    MARK_BUTTON = "//div[@class='ucard-mini_cnt']//div[@class='ucard-mini_cnt_i ellip' and text()='"
    BLOCKED_MARK_BUTTON = "//div[@class='ucard-mini_info' and text()='"

    def mark_button(self, name): 
        return self.get_clickable_element(self.MARK_BUTTON + name + "']")

    def blocked_mark_button(self):
        text = u'не разрешает отмечать себя'
        return self.get_visibility_element(self.BLOCKED_MARK_BUTTON + text + "']") 

    def comment_input(self):
        return self.get_clickable_element(self.COMMENT_INPUT)