# -*- coding: utf-8 -*-

from page_object import PageObject
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

ADD_FOLDER_BTN_CLASS = 'new-folder-btn__button-wrapper'
CREATION_FOLDER_MODAL_CLASS = 'c216'
CF_MORE_SETTINGS_SELECTOR = 'a[data-test-id="moreSettings"]'
CF_PARENT_FOLDERS_SELECTOR = '.Select-control'
PARENT_FOLDER_SELECTOR = 'div[aria-label="{}"]'
FOLDER_NAME_INPUT_SELECTOR = 'input[data-test-id="name"]'
CF_SUBMIT_SELECTOR = 'button[data-test-id="submit"]'
CF_ERROR_SELECTOR = 'small[data-test-id="Такая папка уже существует"]'
CF_CANCEL_SELECTOR = 'button[data-test-id="cancel"]'

RIGHT_CLICK_FOLDER_MENU_SELECTOR = '.contextmenu-folder'
FOLDER_DELETE_BUTTON_SELECTOR = 'div[data-qa-id="delete"]'
DELETE_CONFIRMATION_MODAL_SELECTOR = '.layer-window__block'
SUBMIT_DELETION = 'span[title="Удалить"]'

class FoldersActivities(PageObject):

    def create_folder_by_btn(self, folder_name, parent_folder=None):
        new_folder_btn = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, ADD_FOLDER_BTN_CLASS)))
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, ADD_FOLDER_BTN_CLASS)))

        new_folder_btn.click()        

        modal = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, CREATION_FOLDER_MODAL_CLASS)))

        if parent_folder:
            modal.find_element_by_css_selector(CF_MORE_SETTINGS_SELECTOR).click()

            modal.find_element_by_css_selector(CF_PARENT_FOLDERS_SELECTOR).click()

            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, PARENT_FOLDER_SELECTOR
                .format(parent_folder)))).click()

        folder_name_input = modal.find_element_by_css_selector(FOLDER_NAME_INPUT_SELECTOR)
        folder_name_input.send_keys(folder_name)

        modal.find_element_by_css_selector(CF_SUBMIT_SELECTOR).click()

        try:
            modal.find_element_by_css_selector(CF_ERROR_SELECTOR)
            modal.find_element_by_css_selector(CF_CANCEL_SELECTOR).click()
            return False
        except:
            return True

    def delete_folder(self, name, is_child=False):
        folder = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[title="{name}"]{cl}'
            .format(name=name, cl='[class~=nav__item_child]' if is_child else ''))))
        self.create_ac()
        self.action_chains.context_click(folder).perform()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, RIGHT_CLICK_FOLDER_MENU_SELECTOR)))

        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, FOLDER_DELETE_BUTTON_SELECTOR))).click()

        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, DELETE_CONFIRMATION_MODAL_SELECTOR)))
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, SUBMIT_DELETION))).click()
        self.wait_until_delete(name, is_child)

    def wait_until_delete(self, folder_name, is_child):
        self.wait.until(not self.element_exists('a[title="{name}"]{cl}'
                    .format(name=folder_name, cl='[class~=nav__item_child]' if is_child else '')))

    

