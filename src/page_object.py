# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class PageObject(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

        self.user_data = {
            'login': 'tarados_feroces',
            'password': 'Welc0me_to_Tarad0s!'
        }

    def open(self, url):
        self.driver.get(url)
        self.wait = WebDriverWait(self.driver, 10)

    def login(self):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(self.driver.find_element_by_xpath('//iframe[@class="ag-popup__frame__layout__iframe"]')))

        login_input = self.driver.find_element_by_name('Login')
        login_input.send_keys(self.user_data['login'])

        continue_button = self.driver.find_element_by_tag_name('button')
        continue_button.click()

        password_input = self.wait.until(EC.visibility_of_element_located((By.NAME, 'Password')))
        password_input.send_keys(self.user_data['password'])

        continue_button.click()

        self.driver.switch_to_default_content()

    def move_all_msgs(self, destination):
        all_dropdown = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.b-dropdown_selectAll > .b-dropdown__ctrl > .b-dropdown__arrow')))
        self.wait.until(EC.element_to_be_clickable(all_dropdown))
        all_dropdown.click()

        print 'lol'

        toggle_data = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.b-dropdown_selectAll > .b-dropdown__list')))
        print 'lol2'
        toggle_data.find_element_by_css_selector('div[data-group="selectAll"] > .b-dropdown__list > a[data-name="all"]').click()
    
        self.__move(destination)

    def move_n_msgs(self, n, destination):
        checkboxes = self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'b-datalist__item__cbx')))
        print len(checkboxes)
        for i in range(0, n):
            checkboxes[i].click()

        self.__move(destination)

    def __move(self, destination):
        move_to = self.driver.find_element_by_css_selector('div[data-group="moveTo"]')
        move_to.click()

        target_dir = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.b-dropdown__group_ > a[data-text="{}"]'.format(destination))))
        target_dir.click()

    def go_to_spam(self):
        self.driver.find_element_by_css_selector('div[data-id="950"]').click()

    def close(self):
        self.driver.close()



# class Inbox(PageObject): 
#     def __init__(self):
        


    

    