# -*- coding: utf-8 -*-

from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


from .page_object import PageObject
from .message import Message


class FiltersApplyingPageObject(PageObject):

    def __to_message(self, web_object):
        print web_object.get_property('title')
        read_status = web_object.find_element_by_class_name('llc__read-status')

        try:
            
            read_status = read_status.find_element_by_css_selector('button[class="ll-rs_is-active"]')
        except NoSuchElementException:
            read_status = True
        else:
            read_status = False

        return read_status


    def get_messages(self):
        messages = []
        try:
            data = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'dataset__items')))
            messages = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[data-shortcut="list-letter"]')))
        except:
            messages = []

        return list(map( lambda x: self.__to_message(x), messages ))


    def madness(self):

        search_panel = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'search-panel-button__text'))
        )
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'search-panel-button__text')))
        
        with open('.sources/before.html', 'w') as out:
            out.write(self.driver.page_source.encode('utf-8').strip())

        search_panel.click()
        sleep(4)

        with open('.sources/after.html', 'w') as out:
            out.write(self.driver.page_source.encode('utf-8').strip())


    
    def click_inbox(self):
        filter_control = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-qa-id="folder-name:name:Входящие"]'))
        )

        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-qa-id="folder-name:name:Входящие"]')))
        
        filter_control.click()


    def click_filter_flag(self):

        search_panel = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span[class="search-panel-button__text"]'))
        )
        self.wait.until(EC.p((By.CSS_SELECTOR, 'span[class="search-panel-button__text"]')))
        
        search_panel.click()

        controls = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span[data-qa-id="button:point"]'))
        )

        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[data-qa-id="button:point"]')))

        print controls
        
        controls.click()
        print self.get_messages()



    def click_to_search_panel(self):

        messages = self.get_messages()
        print messages

        filter_control = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'filters-control__filter-text'))
        )

        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'filters-control__filter-text')))
        
        filter_control.click()

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

        messages = self.get_messages()
        print messages

    

