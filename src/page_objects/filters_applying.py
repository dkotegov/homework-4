# -*- coding: utf-8 -*-

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


from .page_object import PageObject



class FiltersApplyingPageObject(PageObject):


    def click_to_search_panel(self):
        search_panel = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'select__control')))
        
        search_panel.click()

        standart_selectors = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'select__item-text')))

        selectors_by_text = {
            selector.text: selector
            for selector in standart_selectors
        }

        selector_buttons = {
            "all": selectors_by_text[u"Все письма"],
            "unread": selectors_by_text[u"Непрочитанные"],
            "flag": selectors_by_text[u"С флажком"],
            "attachments": selectors_by_text[u"С вложениями"],
        }

        selector_buttons['unread'].click()
        
        sleep(3)

        print selector_buttons
    

