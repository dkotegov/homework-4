# -*- coding: utf-8 -*-
from BasicPage import BasicPage
from MainPage import MainPage
from selenium.webdriver import ActionChains
from tests.pages.main_page.notifications.NotificationManager import NotificationManager
from tests.pages.main_page.menu.top_menu import TopMenuManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class DirectoryPage(MainPage):
    ARCHIVE_URL = 'https://e.mail.ru/archive'
    DRAFTS_URL = 'https://e.mail.ru/drafts'
    SOCIAL_URL = 'https://e.mail.ru/social'
    NEWS_LETTERS_URL = 'https://e.mail.ru/newsletters'
    click_flag = '.ll-fs'
    top_menu_move = 'div.portal-menu-element_move'
    click_flag_activate = ".ll-fs_is-active"
    flag_activate_class = "ll-fs ll-fs_is-active"
    archive_button = "div.portal-menu-element_archive"
    social_button = "div.list-item[title='Социальные сети']"
    news_letter_button = "div.list-item[title='Рассылки']"
    drafts_button = "div.portal-menu-element_drafts"
    nav_archive_button = "a.nav__item[title='Архив']"
    nav_drafts_button = "a.nav__item[title='Черновики']"
    nav_newsletters_button = "a.nav__item[title='Рассылки']"
    nav_all_folders_button = "a.sidebar__menu-item"
    select_letter_button = 'a.llc:first-of-type .ll-rs'


    def __init__(self, driver):
        self.driver = driver
        self.notification_manager = NotificationManager(self.driver)
    
    def open(self):
        self.driver.get(self.LOGIN_URL)

    def move_to_social(self):
        elem = self.wait_render(self.top_menu_move)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        
        elem = self.wait_render(self.social_button)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        self.notification_manager.hide_notification()

    def move_to_newsletters(self):
        elem = self.wait_render(self.top_menu_move)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()

        elem = self.wait_render(self.news_letter_button)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        self.notification_manager.hide_notification()

    
    def move_to_archive(self):
        elem = self.wait_render(self.archive_button)
        elem.click()
        self.notification_manager.hide_notification()

    def click_nav_archive_button(self):
        elem = self.wait_render(self.nav_archive_button)
        elem.click()
        self.wait_redirect(self.ARCHIVE_URL)
    
    def go_to_newsletters(self):
        elem = self.wait_render(self.nav_all_folders_button)
        elem.click()
        self.driver.get(self.NEWS_LETTERS_URL)
        self.wait_redirect(self.NEWS_LETTERS_URL)
    
    def go_to_social(self):
        elem = self.wait_render(self.nav_all_folders_button)
        elem.click()
        self.driver.get(self.SOCIAL_URL)
        self.wait_redirect(self.SOCIAL_URL)
        
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


