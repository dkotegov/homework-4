# -*- coding: utf-8 -*-
from selenium import webdriver

import unittest
import os
import time

class AskTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://otvet.mail.ru/ask')
        self.username = 'test_qwerty1122@mail.ru'
        self.password = os.getenv('PASSWORD')

    def test_01(self):
        driver = self.driver

        input = driver.find_elements_by_class_name('B1kkDlxig1yJhDIKljYs2_0')


    def tearDown(self):
        self.driver.quit() 

if __name__ == '__main__':
    unittest.main()    
    pass


