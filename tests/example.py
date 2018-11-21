#!/usr/bin/python

from os import environ
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import unittest


if __name__ == '__main__':

    driver = webdriver.Firefox()
    user_data = {
        'login': 'tarados_feroces',
        'password': 'Welc0me_to_Tarad0s!'
    }

    try:
        driver.get('https://e.mail.ru/login')

        
        wait = WebDriverWait(driver, 10)
        wait.until(EC.frame_to_be_available_and_switch_to_it(driver.find_element_by_xpath('//iframe[@class="ag-popup__frame__layout__iframe"]')))

        login_input = driver.find_element_by_name('Login')
        login_input.send_keys(user_data['login'])

        continue_button = driver.find_element_by_tag_name('button')
        continue_button.click()

        password_input = wait.until(EC.visibility_of_element_located((By.NAME, 'Password')))
        password_input.send_keys(user_data['password'])

        continue_button.click()

        driver.switch_to_default_content()
        
        # checkboxes = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'b-datalist__item__cbx')))

        all_checkbox = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-name="toggle"] > .b-checkbox__box')))
        all_checkbox.click()
        
        # for cbx in checkboxes:
        #     cbx.click()

        messages = driver.find_elements_by_class_name('b-datalist__item__panel')[0]
        target_dir = driver.find_element_by_css_selector('div[data-id="500001"]')

        ActionChains(driver).drag_and_drop(messages, target_dir).perform()

        time.sleep(3)
        
    
    finally:
        driver.close()
