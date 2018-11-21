#!/usr/bin/python


import unittest

from tests import get_webdriver, get_credentials


class TestApplyingFilters(unittest.TestCase):
    
    def test_example(self):
        driver = get_webdriver()
        login, password = get_credentials()

        print (login, password)

        try:
            driver.get("https://www.github.com/")

            log_in_button = list(filter(
                lambda elem: elem.text == "Sign in",
                driver.find_elements_by_class_name('HeaderMenu-link')
            ))[0]
            
            log_in_button.click()

            login_input = driver.find_element_by_id("login_field")
            password_input = driver.find_element_by_id("password")

            login_input.send_keys(login)
            password_input.send_keys(password)
            
            submit_button = driver.find_element_by_name("commit")

            submit_button.click()

            error_window = driver.find_elements_by_class_name("container")

            self.assertEqual(error_window[1].text, "Incorrect username or password.")
        
        finally:
            driver.close()

