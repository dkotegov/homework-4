# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

if __name__ == '__main__':
    browser = webdriver.Chrome('./chromedriver')
    browser.get("https://otvet.mail.ru")
    print(browser.title)
    search = browser.find_element_by_css_selector("[bem-id='182']")
    search.send_keys("TEXT")

    button = browser.find_element_by_css_selector("[bem-id='185']")
    button.click()

    WebDriverWait(browser, 5)
    pass
