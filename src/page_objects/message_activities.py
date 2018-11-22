# -*- coding: utf-8 -*-

from page_object import PageObject

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MessageActivities(PageObject):
    
    def move_all_msgs(self, destination):
        data = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'dataset__items')))
        
        try:
            data.find_element_by_css_selector('.llc__avatar').click()


            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span[title="Выделить все (Ctrl+A)"]'))).click()
    
            self.__move(destination)
        except:
            throw 

    def move_n_msgs(self, n, destination):

        data = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'dataset__items')))
        checkboxes = data.find_elements_by_css_selector('.llc__avatar')

        print len(checkboxes)
        for i in range(0, n):
            checkboxes[i].click()

        self.__move(destination)

    def __move(self, destination):
        self.driver.find_element_by_css_selector('span[title="В папку (V)"]').click()
        self.driver.find_element_by_css_selector('a[title="{}"]'.format(destination)).click()

    def go_to(self, destination):
        folders = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.nav-folders')))
        folders.find_element_by_css_selector('a[title="{}"]'.format(destination)).click()
        