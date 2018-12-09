# -*- coding: utf-8 -*-

from component import Component
from write_letter import WriteLetter
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class Sidebar(Component):
    BASE = '//div[@data-qa-id="full"] '
    BASE_WITHOUT_QA_ID = '//div[contains(@class,"sidebar__full")]'
    CONTEXTMENU = '//div[@data-qa-id="contextmenu"] '

    INBOX_BUTTON = BASE + '//a[@data-qa-id="0"]'
    NEW_DIR = BASE + '//div[@class="new-folder-btn__button-wrapper"]'
    FOLDER_NAME_TEXT = BASE + \
        '//a[@title="{}"]//div[@class="nav__folder-name__txt"]'
    REMOVE_FROM_TRASH = BASE + \
        '//a[@data-qa-id="500002"]//div[@class="nav__folder-clear"]'
    SUBMIT_REMOVE_FROM_TRASH = '//div[@class="layer__submit-button"]'
    FOLDER_ELEM = './/a[@title="{}"]'
    DELETE_BUT = '//div[@data-qa-id="delete"]'
    FOLDER_DIV = './/a[@title="{}"]'
    SUBMIT_DELETE = '//div[@class="layer__submit-button"]'
    SUBMIT_ACTION = '//div[@class="layer__submit-button"]'
    LINK_TRASH = '//a[@title="Корзина"]'
    LOCK_FOLDER = CONTEXTMENU + '//span[contains(text(), "Заблокировать")]'
    UNLOCK_FOLDER = CONTEXTMENU + '//span[contains(text(), "Разблокировать")]'
    WRITE_LETTER_BUTTON = BASE + '//span[@data-qa-id="compose"]'

    FOLDER_ARROW = '//div[@data-qa-id="folder-arrow"]'
    NESTED_FOLDER_DIV = '//a[@class="nav__item_child" and @title="{}"]'

    CONTEXT_MENU_FOLDER = '//div[@data-qa-id="contextmenu"' + \
        ' and @class="contextmenu-folder"] '
    ELEMENT_OF_FOLDER_CONTEXT_MENU = CONTEXT_MENU_FOLDER + \
        '//span[@class="list-item__text" and contains(text(),"{}")]/parent::*'
    FOLDER = BASE + '//a[@title="{}"]'
    FOLDER_ACTIVE = BASE + '//a[@title="{}" and contains(concat(" ", normalize-space(@class), " "), " {} ")]'
    EDIT_FOLDER = '//span[contains(text(), "Редактировать папку")]'

    def write_letter(self):
        write_letter_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.WRITE_LETTER_BUTTON)
        )
        write_letter_button.click()

    def write_and_send_letter(self, whom, theme, letter):
        self.write_letter()
        write_letter = WriteLetter(self.driver)
        write_letter.set_whom(whom)
        write_letter.set_theme(theme)
        write_letter.set_text(letter)
        write_letter.send_letter()
        write_letter.close_window()

    def create_new_dir(self):
        create_dir_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.NEW_DIR)
        )
        create_dir_button.click()

    def click_to_inbox(self):
        WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.INBOX_BUTTON)
        ).click()

    def waitForVisible(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.BASE_WITHOUT_QA_ID))

    def get_text_by_folder_name(self, f_name):
        F_NAME_TEXT = self.FOLDER_NAME_TEXT.format(f_name)
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(F_NAME_TEXT).text
        )

    def is_trash_empty(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.BASE))
        clear_button = self.driver.find_elements_by_xpath(
            self.REMOVE_FROM_TRASH)
        if len(clear_button) == 0:
            return True
        else:
            return False

    def clear_trash(self):
        if self.is_trash_empty():
            return
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.REMOVE_FROM_TRASH)).click()
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(
                self.SUBMIT_REMOVE_FROM_TRASH)).click()

    def clear_folder(self, folder_name):
        if (not self.is_folder_exists(folder_name)):
            return
        if (self.is_folder_empty(folder_name)):
            return
        self.right_click_by_folder(folder_name)
        self.click_context_menu_element('Очистить содержимое')
        self.submit_action()

    def is_folder_empty(self, folder_name):
        self.right_click_by_folder(folder_name)
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CONTEXT_MENU_FOLDER)
        )

        button = self.driver.find_element_by_xpath(
            self.ELEMENT_OF_FOLDER_CONTEXT_MENU.format('Очистить содержимое'))

        action_chains = ActionChains(self.driver)
        action_chains.send_keys(Keys.ESCAPE).perform()

        isButtonDisabled = button.get_attribute('disabled')
        if (isButtonDisabled):
            return True
        return False

    def click_context_menu_element(self, element_name):
        button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(
                self.ELEMENT_OF_FOLDER_CONTEXT_MENU.format(element_name))
        )
        button.click()

    def delete_folder_by_name(self, folder_name):
        self.right_click_by_folder(folder_name)
        self.click_delete()
        self.submit_delete()

    def right_click_by_folder(self, folder_name):
        FOLDER_EL = self.FOLDER_ELEM.format(folder_name)
        folder = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(FOLDER_EL)
        )
        action_chains = ActionChains(self.driver)
        action_chains.context_click(folder).perform()

    def click_by_folder(self, folder_name):
        FOLDER_EL = self.FOLDER_ELEM.format(folder_name)
        folder = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(FOLDER_EL)
        )
        folder.click()

    def get_folder_element(self, folder_name):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.FOLDER.format(folder_name))
        )

    def click_delete(self):
        button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DELETE_BUT)
        )
        button.click()

    def try_click_delete(self):
        button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DELETE_BUT)
        )
        try:
            button.click()
            return True
        except WebDriverException:
            return False

    def try_delete_folder(self, folder_name):
        self.right_click_by_folder(folder_name)
        result = self.try_click_delete()
        return result

    def submit_delete(self):
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT_DELETE)
        )
        submit.click()

    def submit_action(self):
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT_ACTION)
        )
        submit.click()

    def is_folder_deleted(self, f_name):
        F_DIV = self.FOLDER_DIV.format(f_name)
        WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.BASE_WITHOUT_QA_ID))

        folders = self.driver.find_elements_by_xpath(F_DIV)

        if len(folders) == 0:
            return True
        else:
            return False

    def go_to_trash(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LINK_TRASH)).click()

    def click_block_folder(self):
        button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LOCK_FOLDER)
        )
        button.click()

    def click_unlock_folder(self):
        button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.UNLOCK_FOLDER)
        )
        button.click()

    def go_to_folder(self, folder_name, active_class='nav__item_active'):
        folder = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.FOLDER.format(folder_name)))
        folder.click()
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.FOLDER_ACTIVE.format(folder_name, active_class))
        )

    def delete_folder(self, folder_name):
        if (not self.is_folder_exists(folder_name)):
            return
        self.right_click_by_folder(folder_name)
        self.click_delete()
        self.submit_action()

    def is_folder_exists(self, folder_name):
        try:
            self.driver.find_element_by_xpath(
                self.FOLDER_ELEM.format(folder_name))
            return True
        except NoSuchElementException:
            return False

    def is_folder_created(self, folder_name):
        folder_div = self.FOLDER_DIV.format(folder_name)
        self.driver.refresh()
        WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.BASE_WITHOUT_QA_ID))
        folders = self.driver.find_elements_by_xpath(folder_div)
        if len(folders) == 0:
            return False

        return True

    def open_folder_wrapper(self):
        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.FOLDER_ARROW)
        ).click()

    def is_folder_locked(self):
        try:
            WebDriverWait(self.driver, 2, 0.1).until(
                lambda d: d.find_element_by_xpath(self.UNLOCK_FOLDER)
            )
        except TimeoutException:
            return False
        return True

    def is_folder_unlocked(self):
        try:
            WebDriverWait(self.driver, 2, 0.1).until(
                lambda d: d.find_element_by_xpath(self.LOCK_FOLDER)
            )
        except TimeoutException:
            return False
        return True

    def click_edit(self):
        button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.EDIT_FOLDER)
        )
        button.click()

    def is_folder_nested(self, folder_name):
        nested_folder_div = self.NESTED_FOLDER_DIV.format(folder_name)
        self.driver.refresh()
        WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.BASE_WITHOUT_QA_ID))
        folders = self.driver.find_elements_by_xpath(nested_folder_div)
        return folders != 0

    def block_folder_by_name(self, folder_name):
        self.right_click_by_folder(folder_name)
        self.click_block_folder()

    def click_unlock_folder_by_name(self, folder_name):
        self.right_click_by_folder(folder_name)
        self.click_unlock_folder()
