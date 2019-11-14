# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("https://park.mail.ru/")
    driver.quit()