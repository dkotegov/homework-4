# -*- coding: utf-8 -*-

import os
import urlparse

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException

WAIT_TIME = 10


class Base(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Base):
    LOGIN = '//input[@name="st.email"]'
    PASSWORD = '//input[@name="st.password"]'
    SUBMIT = '//input[@data-l="t,loginButton"]'

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class Main(Base):
    PHOTO_SECTION = '//div[@class="nav-side __navigation __rainbow-menu __small"]/a[5]'
    PHOTO_SECTION_ALBUM = '//div[@class="photo-sc photo-sc__albums __albums"]'

    def check_click(self):
        try:
            self.driver.find_element_by_xpath(self.PHOTO_SECTION).click()
        except (NoSuchElementException, ElementNotVisibleException):
            return False
        return True

    def check_album_section(self):
        try:
            self.driver.find_element_by_xpath(self.PHOTO_SECTION_ALBUM)
        except (NoSuchElementException, ElementNotVisibleException):
            return False
        return True


class CreateAlbum(Base):
    FIELD = '//div[@class="modal_overlay"]'
    CREATE_ALBUM = '//a[@class="portlet_h_ac lp"]'
    CHECKBOX_ALBUM = 'irc'
    NAME_ALBUM = '//input[@name="st.layer.photoAlbumName"]'
    CREATE_ALBUM_SUBMIT = '//input[@name="button_album_create"]'
    ATTR = 'value'
    CANCEL = 'Отменить'
    ALBUM_FIELD = '//div[@class="photo-panel_info"]'

    FRIENDS = {
        'all': 0,
        'all_friend': 1,
        'relatives': 2,
        'his half': 3,
        'best friends': 4,
        'colleagues': 5,
        'schoolfellow': 6,
        'classmates': 7,
        'colleagues': 8,
    } 

    def click(self, elem):
        try:
            elem.click()
        except (NoSuchElementException, ElementNotVisibleException):
            return False
        return True

    def create(self, name_alb):
        res1 = self.check_click()
        res2 = self.create_name_album(name_alb)
        res3 = self.create_album_click()
        if res1 == False or res2 == False or res3 == False:
            return False
        return True

    def check_click(self):
        res = self.click(self.driver.find_element_by_xpath(self.CREATE_ALBUM))
        return res

    def check(self):
        try:
            self.driver.find_element_by_xpath(self.FIELD)
        except (NoSuchElementException, ElementNotVisibleException):
            return False
        return True

    def cancel_click(self):
        res = self.click(self.driver.find_element_by_link_text(self.CANCEL))
        return res

    def check_checkboxes(self):
        cb = self.driver.find_elements(By.CLASS_NAME, self.CHECKBOX_ALBUM)

        for el in cb:
            res = self.click(el)
            if res == False:
                return False
        
        return True

    def check_all_friend_checkboxes(self):
        cb = self.driver.find_elements(By.CLASS_NAME, self.CHECKBOX_ALBUM)
        cb[self.FRIENDS['all_friend']].click()
        cb = self.driver.find_elements(By.CLASS_NAME, self.CHECKBOX_ALBUM)
        
        for el in self.FRIENDS:
            if el == 'all':
                if cb[self.FRIENDS[el]].get_attribute('checked') != None:
                    return False
            elif cb[self.FRIENDS[el]].get_attribute('checked') != "true":
                return False
        
        return True

    def check_not_all_friend_checkboxes(self):
        cb = self.driver.find_elements(By.CLASS_NAME, self.CHECKBOX_ALBUM)
        cb[self.FRIENDS['all_friend']].click()
 
        for el in self.FRIENDS:
            if self.FRIENDS[el] > 1:
                cb[self.FRIENDS[el]].click()
                if cb[self.FRIENDS['all_friend']].get_attribute('checked') != None:
                    return False
                cb[self.FRIENDS['all_friend']].click()

        return True

    def check_not_empty_checkboxes(self):
        cb = self.driver.find_elements(By.CLASS_NAME, self.CHECKBOX_ALBUM)
        cb[self.FRIENDS['all']].click()
        cb = self.driver.find_elements(By.CLASS_NAME, self.CHECKBOX_ALBUM)
 
        if cb[self.FRIENDS['all']].get_attribute('checked') != "true":
            return False
 
        return True

    def create_name_album(self, name_alb):
        self.driver.find_element_by_xpath(self.NAME_ALBUM).send_keys(name_alb)
        txt = self.driver.find_element_by_xpath(self.NAME_ALBUM).get_attribute(self.ATTR)
        if txt == name_alb:
            return True
        return False


    def create_album_click(self):
        res = self.click(self.driver.find_element_by_xpath(self.CREATE_ALBUM_SUBMIT))
        return res


class Album(Base):
    FIELD = '//div[@class="modal_overlay"]'
    EDIT_ALBOM = '//div[@class="photo-menu_edit iblock-cloud_show"]'
    EDIT_NAME_ALBUM = '//input[@class="it h-mod"]'
    ATTR = 'value'
    EDIT_PARAM_PRIVATE = '//li[@class="controls-list_item"]'
    BACK = '//a[@class="al"]'
    DEL_ALBOM = '//input[@name="button_delete_confirm"]'
    NAV_PHOTO = '//a[@class="mctc_navMenuSec mctc_navMenuActiveSec"]'
    COVER = '//a[@class="modal_overlay"]'
    CANCEL = '//a[@class="lp"]'
    ALBUM_FIELD = '//div[@class="photo-panel_info"]'

    def click(self, elem):
        try:
            elem.click()
        except (NoSuchElementException, ElementNotVisibleException):
            return False
        return True

    def check_album_field(self):
        try:
            self.driver.find_element_by_xpath(self.ALBUM_FIELD)
        except (NoSuchElementException, ElementNotVisibleException):
            return False
        return True

    def check_album_edit_field(self):
        try:
            self.driver.find_element_by_xpath(self.BACK)
        except (NoSuchElementException, ElementNotVisibleException):
            return False
        return True

    def check(self, name_alb):
        elem = self.driver.find_elements_by_link_text(name_alb)
        if len(elem) != 0:
            return True
        return False

    def open_click(self, name_alb):
        res = self.click(self.driver.find_element_by_link_text(name_alb))
        return res

    def edit_click(self):
        res = self.click(self.driver.find_element_by_xpath(self.EDIT_ALBOM))
        return res

    def check_rename(self, new_name_alb):
        self.driver.find_element_by_xpath(self.EDIT_NAME_ALBUM).clear()
        self.driver.find_element_by_xpath(self.EDIT_NAME_ALBUM).send_keys(new_name_alb)       
        txt = self.driver.find_element_by_xpath(self.EDIT_NAME_ALBUM).get_attribute(self.ATTR)
        if txt == new_name_alb:
            return True
        return False

    def edit_private_click(self):
        res = self.click(self.driver.find_elements_by_xpath(self.EDIT_PARAM_PRIVATE)[0])
        return res

    def back_click(self):
        res = self.click(self.driver.find_elements_by_xpath(self.BACK)[0])
        return res

    def cancel_click(self):
        res = self.click(self.driver.find_elements_by_xpath(self.CANCEL)[4])
        return res
    
    def photo_click(self):
        wait = WebDriverWait(self.driver, WAIT_TIME)
        wait.until(expected_conditions.invisibility_of_element_located((By.XPATH, self.COVER)))
        res = self.click(self.driver.find_element_by_xpath(self.NAV_PHOTO))
        return res

    def check_edit_private(self):
        try:
            self.driver.find_element_by_xpath(self.FIELD)
        except (NoSuchElementException, ElementNotVisibleException):
            return False
        return True

    def del_click(self):
        try:
            self.driver.find_elements_by_xpath(self.EDIT_PARAM_PRIVATE)[1].click()
            self.driver.find_element_by_xpath(self.DEL_ALBOM).click()
        except (NoSuchElementException, ElementNotVisibleException):
            return False
        return True
