from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os
import time
import unittest

class TooBigQuestionTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://otvet.mail.ru/ask')
        self.username = 'test_qwerty1122@mail.ru'
        self.password = os.getenv('PASSWORD')

    def test_01(self):
        driver = self.driver

        inputQuestionField = driver.find_elements_by_name('question_text')[0]
        inputQuestionField.click()

        for _ in range(122):
            inputQuestionField.send_keys('a')

        alert = driver.find_elements_by_class_name('z1LfJpugzE39YVXERE-f__0')[0]
        self.assertEqual(alert.get_attribute('innerHTML'), 'Поле «Тема вопроса» не может быть больше 120 символов.')

    def tearDown(self):
        self.driver.quit() 