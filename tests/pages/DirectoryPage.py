# -*- coding: utf-8 -*-
from BasicPage import BasicPage
from MainPage import MainPage
from selenium.webdriver import ActionChains
from tests.pages.main_page.notifications.NotificationManager import NotificationManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class DirectoryPage(MainPage):
    ARCHIVE_URL = 'https://e.mail.ru/archive'
    click_flag = '.ll-fs'
    click_flag_activate = ".ll-fs_is-active"
    flag_activate_class = "ll-fs ll-fs_is-active"
    archive_button = "div.portal-menu-element_archive"
    nav_archive_button = "a.nav__item[title='Архив']"
    select_letter_button = 'a.llc:first-of-type .ll-rs'


    def __init__(self, driver):
        self.driver = driver
        self.notification_manager = NotificationManager(self.driver)
    
    def open(self):
        self.driver.get(self.LOGIN_URL)

    def move_to_archive(self):
        elem = self.wait_render(self.archive_button)
        elem.click()
        self.notification_manager.hide_notification()

    def click_nav_archive_button(self):
        elem = self.wait_render(self.nav_archive_button)
        elem.click()
        self.wait_redirect(self.ARCHIVE_URL)
        
    def select_letter(self):
        elem = self.wait_render(self.select_letter_button)
        elem.click()

    def set_check_flag(self):
        elem = self.wait_render(self.click_flag)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
    
    def unset_check_flag(self):
        elem = self.wait_render(self.click_flag_activate)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
    
    def get_important_status(self):
        elem = self.wait_render(self.click_flag)
        if elem.get_attribute('class') == self.flag_activate_class: 
            return True
        else:
            return False


