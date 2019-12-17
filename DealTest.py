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
        self.driver.refresh()
    
    def test_create_deal(self):
        page = DealPage(self.driver)    
        page.wait_redirect('https://m.calendar.mail.ru/todos')
        self.driver.refresh()
        page.click_on_name_deal()
        page.enter_deal_name('New deal')
        page.click_on_add_btn()
        self.driver.refresh()

    def tearDown(self):
        self.driver.quit()


        