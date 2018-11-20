#!/usr/bin/python

from os import environ
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager



if __name__ == '__main__':

    # print environ["BROWSER"]


    driver = webdriver.Firefox()

    try:
        driver.get("https://www.github.com/")

        # print driver.current_url


        log_in_button = list(filter(
            lambda elem: elem.text == "Sign in",
            driver.find_elements_by_class_name('HeaderMenu-link')
        ))[0]
        
        # print log_in_button.text
        log_in_button.click()

        login = driver.find_element_by_id("login_field")
        password = driver.find_element_by_id("password")

        login.send_keys("ap.kuznecov.3b@Yandex.ur")
        password.send_keys("Not a my password :(")
        
        

        submit_button = driver.find_element_by_name("commit")

        submit_button.click()

        error_window = driver.find_elements_by_class_name("container")

        assert error_window[1].text == "Incorrect username or password."


        assert "No results found." not in driver.page_source
    
    finally:
        driver.close()
