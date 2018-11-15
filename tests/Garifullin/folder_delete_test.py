# -*- coding: utf-8 -*-

import os
import unittest
import urlparse

from selenium.webdriver import DesiredCapabilities, Remote, ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from mail_auth import Authentification

class Component(object):
    def __init__(self, driver):
        self.driver = driver

class CreateFolderForm(Component):
    # CREATE_BUTTON = '//span[@title="Новая папка"]'
    CREATE_BUTTON = '//div[@class="new-folder-btn__button-wrapper"]'
    INPUT_FOLDER_NAME = '//input[@data-test-id="name"]'
    SUBMIT = '//button[@data-test-id="submit"]'
    # CREATE_BUTTON = '//span[contains(text(),"Новая папка")]'

    def open_create_form(self):
        # WebDriverWait(self.driver, 30, 1).until(
        #     expected_conditions.element_to_be_clickable((By.XPATH, self.CREATE_BUTTON))).click()

        create_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CREATE_BUTTON)
        )
        WebDriverWait(self.driver, 30, 1).until(
            expected_conditions.visibility_of(create_button))
        create_button.click()

    def set_name(self, name):
        name_input = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.INPUT_FOLDER_NAME)
        )
        name_input.send_keys(name)
    
    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()
        
class DeleteFolder(Component):
    FOLDER_ELEM = './/a[@title="{}"]'
    DELETE_BUT = '//div[@data-qa-id="delete"]'
    SUBMIT = '//div[@class="layer__submit-button"]'


    def delete(self, folder_name):
        self.right_click(folder_name)
        self.click_delete()
        self.submit()

    def right_click(self, folder_name):
        FOLDER_EL = self.FOLDER_ELEM.format(folder_name)
        folder = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(FOLDER_EL)
        )
        actionChains = ActionChains(self.driver)
        actionChains.context_click(folder).perform()
    
    def click_delete(self):
        button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DELETE_BUT)
        )
        button.click()
    
    def submit(self):
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT)
        )
        submit.click()

class MailMainPage(Component):
    FOLDER_NAME_TEXT = '//a[@title="{}"]//div[@class="nav__folder-name__txt"]'
    FOLDER_DIV = './/a[@title="{}"]'
    FOLDERS_DIV = '//div[@class="nav-folders"]'
    SELECT_MESSAGE = '//a[contains(@class, "llc_normal")]'
    MOVE_TO_BUTTON = '//span[contains(text(), "Переместить в папку")]'
    NEW_FOLDER_FOR_LETTER = '//div[@title="{}"]'
    REMOVE_FROM_TRASH = '//div[@class="nav__folder-clear"]'
    SUBMIT_REMOVE_FROM_TRASH = '//div[@class="layer__submit-button"]'
    MAIL_FROM = '//span[@class="ll-crpt"]'
    MAIL_TEXT = '//span[@class="ll-sp__normal"]'
    MAIL_TIME = '//div[@class="llc__item llc__item_date"]'
    LINK_TRASH = '//a[@title="Корзина"]'


    def get_text_by_folder_name(self, f_name):
        F_NAME_TEXT = self.FOLDER_NAME_TEXT.format(f_name)
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(F_NAME_TEXT).text
        )
    
    def is_folder_deleted(self, f_name):
        F_DIV = self.FOLDER_DIV.format(f_name)
        self.driver.refresh()
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.FOLDERS_DIV))    
        folders = self.driver.find_elements_by_xpath(F_DIV)
        if len(folders) == 0:
            return True
        else:
            return False
    
    def move_letters_to_folder(self, folder_name):
        folder = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SELECT_MESSAGE)
        )
        actionChains = ActionChains(self.driver)
        actionChains.context_click(folder).perform()

        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MOVE_TO_BUTTON)).click()
        
        new_folder = self.NEW_FOLDER_FOR_LETTER.format(folder_name)
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(new_folder)).click()

    def is_trash_empty(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.FOLDERS_DIV))
        clear_button = self.driver.find_elements_by_xpath(self.REMOVE_FROM_TRASH)
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
            lambda d: d.find_element_by_xpath(self.SUBMIT_REMOVE_FROM_TRASH)).click()
        
    def get_mail_from(self):
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MAIL_FROM).text
        )
    def get_mail_text(self):
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MAIL_TEXT).text
        )
    def get_mail_time(self):
        return WebDriverWait(self.driver, 10, 0.1).until(
            lambda d: d.find_element_by_xpath(self.MAIL_TIME).text
        )
    
    def go_to_trash(self):
        self.driver.find_element_by_xpath(self.LINK_TRASH).click()


class FolderDeleteTest(unittest.TestCase):
    FOLDER_NAME = 'TEST-FOLDER'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        prepare = Authentification(self.driver)
        prepare.auth()

        mailPage = MailMainPage(self.driver)
        createFolderForm = CreateFolderForm(self.driver)
        deleteFolder = DeleteFolder(self.driver)

        #  create a simple folder
        createFolderForm.open_create_form()
        createFolderForm.set_name(self.FOLDER_NAME)
        createFolderForm.submit()
        folder_name = mailPage.get_text_by_folder_name(self.FOLDER_NAME)
        self.assertEqual(self.FOLDER_NAME, folder_name)

        mailPage.clear_trash()

        #  delete a folder and then check letters in a trash
        mailFrom = mailPage.get_mail_from()
        mailText = mailPage.get_mail_text()
        mailTime = mailPage.get_mail_time()
        mailPage.move_letters_to_folder(self.FOLDER_NAME)
        deleteFolder.delete(self.FOLDER_NAME)
        isFolderDeleted = mailPage.is_folder_deleted(self.FOLDER_NAME)
        self.assertTrue(isFolderDeleted)
        mailPage.go_to_trash()
        mailFromInTrash = mailPage.get_mail_from()
        mailTextInTrash = mailPage.get_mail_text()
        mailTimeInTrash = mailPage.get_mail_time()
        self.assertEqual(mailFrom, mailFromInTrash)
        self.assertEqual(mailText, mailTextInTrash)
        self.assertEqual(mailTime, mailTimeInTrash)


        #should be replaced by wait
        # import time
        # time.sleep(5)
        #end(should be replaced by wait)