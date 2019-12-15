import os
import unittest
import config

from selenium import webdriver

from DealPage import DealPage

class DealTest(unittest.TestCase):
    LOGIN_URL = 'https://m.calendar.mail.ru/login'
    BASE_URL = 'https://m.calendar.mail.ru/'
    login = os.environ.get('LOGIN')
    password = os.environ.get('PASSWORD')

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        login_page = DealPage(self.driver)
        login_page.open(self.LOGIN_URL)
        login_page.enter_login(self.login)
        login_page.enter_password(self.password)
        login_page.login()
        login_page.wait_redirect(self.BASE_URL)
    
    def test_create_deal(self):
        page = DealPage(self.driver)
        page.open(self.BASE_URL)
        
        page.wait_redirect('https://m.calendar.mail.ru/todos')
        self.driver.refresh()

    def tearDown(self):
        self.driver.quit()