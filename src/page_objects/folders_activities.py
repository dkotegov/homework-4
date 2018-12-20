# -*- coding: utf-8 -*-

from page_object import PageObject
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class FoldersActivities(PageObject):

    def create_folder_by_btn(self, folder_name='NewFolder', parent_folder=None):
        new_folder_btn = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'new-folder-btn__button-wrapper')))
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'new-folder-btn__button-wrapper')))

        new_folder_btn.click()        

        modal = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'c216')))

        if parent_folder:
            modal.find_element_by_css_selector('a[data-test-id="moreSettings"]').click()
            modal.find_element_by_css_selector('.Select-control').click()
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="{}"]'.format(parent_folder)))).click()

        folder_name_input = modal.find_element_by_css_selector('input[data-test-id="name"]')
        folder_name_input.send_keys(folder_name)
        modal.find_element_by_css_selector('button[data-test-id="submit"]').click()

        try:
            modal.find_element_by_css_selector('small[data-test-id="Такая папка уже существует"]')
            modal.find_element_by_css_selector('button[data-test-id="cancel"]').click()
            return False
        except:
            return True


    def delete_folder(self, name, is_child=False):
        folder = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[title="{name}"]{cl}'.format(name=name, cl='[class~=nav__item_child]' if is_child else ''))))
        self.create_ac()
        self.action_chains.context_click(folder).perform()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.contextmenu-folder')))
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-qa-id="delete"]'))).click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.layer-window__block')))
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[title="Удалить"]'))).click()
        self.wait_until_delete(name, is_child)


    def wait_until_delete(self, folder_name, is_child):
        try:
            while(self.driver.find_element_by_css_selector('a[title="{name}"]{cl}'.format(name=folder_name, cl='[class~=nav__item_child]' if is_child else ''))):
                continue
        except:
            return
