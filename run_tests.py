# -*- coding: utf-8 -*-

import unittest
from selenium.webdriver.support import expected_conditions as EC


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


class EmailMistakeTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path='/home/mark/.wdm/drivers/geckodriver/linux64/v0.29.1/geckodriver')
        self.addCleanup(self.browser.quit)
        self.browser.get('https://mailer.ru.com/signin')

    def testEmailMistake(self):
        enter = WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > section > div > div > section > div > form > fieldset > div.row > div.column.large-4 > button')))
        enter.click()
        self.assertIn('Войти', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)
