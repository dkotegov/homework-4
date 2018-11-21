#!/usr/bin/python

from os import environ
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        
        time.sleep(3)
    
    finally:
        driver.close()
