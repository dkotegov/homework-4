# -*- coding: utf-8 -*-

from page_object import PageObject

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MessageActivities(PageObject):

    def get_message_title(self, msg):
        return msg.find_element_by_css_selector('.ll-sj__normal').text

    def get_messages(self):
        try:
            data = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'dataset__items')))
            messages = data.find_elements_by_css_selector('.llc_normal')

        except:
            messages = []
        
        return messages, len(messages)

    def move_all_msgs_to(self, destination):
        messages, msg_count = self.get_messages()
        
        if msg_count > 0:
            messages[0].click()
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="Выделить все (Ctrl+A)"]'))).click()
            self.__move(destination)
            
    def move_n_msgs_to(self, n, destination):
        messages, msg_count = self.get_messages()
        titles = []
        if msg_count:
            for i in range(0, n):
                titles.append(self.get_message_title(messages[msg_count - i - 1]))
                messages[msg_count - i - 1].find_element_by_css_selector('.llc__avatar').click()

            self.__move(destination)
        self.wait_until_moved(messages[-1])
        return titles

    def wait_until_moved(self, msg):
        msg_id = self.driver.execute_script('return arguments[0].attributes["data-id"].value', msg)
        try:
            while (self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-id="{}"]'.format(msg_id))))):
                pass
        except:
            return True

    def check_moved_messages(self, titles):
        messages = self.get_messages()[0]
        print messages
        message_titles = [self.get_message_title(msg) for msg in messages]
        print 'lol', message_titles

        result = True
        for item in titles:
            if not item in message_titles:
                result = False
                break
        
        return result

    def __move(self, destination):
        self.driver.find_element_by_css_selector('span[title="В папку (V)"]').click()
        self.driver.find_element_by_css_selector('a[title="{}"]'.format(destination)).click()

    def go_to(self, destination):
        folders = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.nav-folders')))
        folders.find_element_by_css_selector('a[title="{}"]'.format(destination)).click()
        