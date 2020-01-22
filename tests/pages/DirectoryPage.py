# -*- coding: utf-8 -*-
from BasicPage import BasicPage
from MainPage import MainPage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from tests.pages.main_page.notifications.NotificationManager import NotificationManager
from tests.pages.main_page.menu.top_menu import TopMenuManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.touch_actions import TouchActions
import time

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
    drafts_button = 'nav.nav_expanded > a.nav__item.js-shortcut[href="/drafts/"]'
    
    nav_social_button = 'nav.nav_expanded > .nav__item.nav__item_child.nav__item_expanded_true[href="/social/"]'
    nav_news_letter_button = 'nav.nav_expanded > .nav__item.nav__item_child.nav__item_expanded_true[href="/newsletters/"]'

    nav_archive_button = "a.nav__item[title='Архив']"
    nav_all_folders_button = "a.sidebar__menu-item"
    select_letter_button = 'a.llc:first-of-type .ll-rs'
    save_letter_button = '.button2.button2_base.button2_hover-support.js-shortcut:nth-child(2)'
    close_write_letter_window = '.container--2lPGK.type_base--rkphf.color_base--hO-yz:last-of-type'
    class_error_text = 'div.rowError--O4k-g'
    empty_subject_text = u'<Без темы>'
    first_mail = '.llc.js-tooltip-direction_letter-bottom.js-letter-list-item.llc_normal.llc_first'
    

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
        
        elem = self.wait_render(self.nav_news_letter_button)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        self.wait_redirect(self.NEWS_LETTERS_URL)
    
    def go_to_social(self):
        elem = self.wait_render(self.nav_all_folders_button)
        elem.click()
        
        elem = self.wait_render(self.nav_social_button)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        self.wait_redirect(self.SOCIAL_URL)
    
    def go_to_drafts(self):
        elem = self.wait_render(self.nav_all_folders_button)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()

        elem = self.wait_render(self.drafts_button)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        self.wait_redirect(self.DRAFTS_URL)
        
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

    def check_error_message(self):
        elem = self.wait_render(self.class_error_text)
        if elem.get_attribute('title') == (u'Не указан адрес получателя'):
            return True
        return False
    
    def close_writer_window(self):
        elem = self.wait_render(self.close_write_letter_window)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()

    def click_save_mail(self):
        elem = self.wait_render(self.save_letter_button)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()
        self.notification_manager.hide_notification()
    
    def open_draft(self):
        elem = self.wait_render(self.first_mail)
        elem.click()
    
    def select_text(self):
        actions = ActionChains(self.driver)
        the_only_element = "div.cke_editable > div > div:first-child"
        element = self.wait_render(the_only_element)
        length = len(element.text)
        actions.click(element)
        actions.key_down(Keys.SHIFT)
        for i in range(length):
            actions.send_keys(Keys.ARROW_LEFT)
        actions.key_up(Keys.SHIFT)
        actions.perform()
        time.sleep(5)
        


