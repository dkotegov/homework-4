# -*- coding: utf-8 -*-

from page_object import PageObject
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


MESSAGE_TITLE = '.ll-sj__normal'
DATASET_ITEMS = '.dataset__items'
MESSAGE = '.llc_normal'
MESSAGE_AVATAR = '.llc__avatar'
SELECT_ALL = 'span[title="Выделить все (Ctrl+A)"]'
MOVE_TO_FOLDER = 'span[title="В папку (V)"]'
FOLDERS = '.nav-folders'
MORE = 'span[title="Ещё (.)"]'
DROPDOWN_MENU = '.dropdown__menu'
REMOVE_SELECTION = 'span[title="Снять выделение (Ctrl+A)"]'
FILTERS = '.filters-control'
FILTER_ITEMS = '.select__items'
FILTER_TEXT = '.filters-control__filter-text'


class MessageActivities(PageObject):
    def get_message_title(self, msg):
        try:
            return msg.find_element_by_css_selector(MESSAGE_TITLE).text
        except StaleElementReferenceException:
            return msg.find_element_by_css_selector(MESSAGE_TITLE).text

    def get_all_titles(self, data):
        titles = []
        for item in data:
            titles.append(self.get_message_title(item))

        return titles

    def get_messages(self):
        data = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, DATASET_ITEMS)))
        messages = data.find_elements_by_css_selector(MESSAGE)

        return messages, len(messages)

    def move_all_msgs_to(self, destination):
        messages, msg_count = self.get_messages()
        titles = self.get_all_titles(messages)

        if msg_count:
            messages[0].find_element_by_css_selector(MESSAGE_AVATAR).click()
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, SELECT_ALL))).click()
            self.__move(destination)
            self.wait_until_moved(messages[0])

        return messages, titles

    def move_n_msgs_to(self, n, destination):
        messages, msg_count = self.get_messages()
        result = []
        titles = []

        if n > msg_count: 
            n = msg_count

        if msg_count:
            for i in range(0, n):
                result.append(messages[msg_count - i - 1])
                titles.append(self.get_message_title(result[-1]))
                messages[msg_count - i - 1].find_element_by_css_selector(MESSAGE_AVATAR).click()

            self.__move(destination)

            self.wait_until_moved(result[0])
        return result, titles

    def wait_until_moved(self, msg):
        msg_id = self.driver.execute_script('return arguments[0].attributes["data-id"].value', msg)
        self.wait.until(
            lambda d: not self.element_exists('a[data-id="{}"]'.format(msg_id)))

    def wait_until_appear(self):
        self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, MESSAGE)))

    def check_moved_messages(self, titles):
        messages = self.get_messages()[0]
        message_titles = self.get_all_titles(messages)
        
        result = True
        for item in titles:
            if not item in message_titles:
                result = False
                break

        return result

    def __move(self, destination):
        self.driver.find_element_by_css_selector(MOVE_TO_FOLDER).click()
        self.driver.find_element_by_css_selector('a[title="{}"]'.format(destination)).click()

    def go_to(self, destination):
        folders = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, FOLDERS)))
        folders.find_element_by_css_selector('a[title="{}"]'.format(destination)).click()
        self.wait_until_appear()

    def apply_flag_for_n(self, n, flag_type):
        messages, msg_count = self.get_messages()
        result = []

        if n > msg_count: 
            n = msg_count

        if msg_count:
            for i in range(0, n):
                messages[i].find_element_by_css_selector(MESSAGE_AVATAR).click()
                result.append(messages[i])
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, MORE))).click()
            self.driver.find_element_by_css_selector(DROPDOWN_MENU)
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.list-item__ico_{}'.format(flag_type)))).click()
            for i in range(0, n):
                messages[i].find_element_by_css_selector(MESSAGE_AVATAR).click()

        return result

    def apply_flag_for_all(self, flag_type):
        messages, msg_count = self.get_messages()
        
        if msg_count:
            messages[0].find_element_by_css_selector(MESSAGE_AVATAR).click()
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, SELECT_ALL))).click()
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, MORE))).click()
            self.driver.find_element_by_css_selector(DROPDOWN_MENU)
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.list-item__ico_{}'.format(flag_type)))).click()
            self.remove_selection()

        return messages

    def remove_selection(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, REMOVE_SELECTION))).click()

    def show_by_filter(self, flag_type):
        if flag_type == 'unread':
            flag_type = 'point'
        elif flag_type == 'all':
            flag_type = False
        
        self.driver.find_element_by_css_selector(FILTERS).click()
        filters_menu = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, FILTER_ITEMS)))
        if flag_type:
            filters_menu.find_element_by_css_selector('.ico_16-{}'.format(flag_type)).click()
        else:
            filters_menu.find_element_by_css_selector('.list > .list-item').click()
            

    def wait_until_content_change(self, flag_type):
        state = self.driver.find_element_by_css_selector('.filters-control__filter-text')
        while(flag_type.decode('utf-8') != state.text):
            continue
        return True
        