import os
import unittest

from pages.login import AuthPage
from selenium.webdriver import DesiredCapabilities, Remote



class ExampleTest(unittest.TestCase):

    USERNAME = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']
    # BLOG = 'Флудилка'
    # TITLE = u'ЗаГоЛоВоК'
    # MAIN_TEXT = u'Текст под катом! Отображается внутри топика!'

    def setUp(self):

        #capabilities = DesiredCapabilities.CHROME
        #capabilities.update({'logLevel': 'DEBUG'})

        #print('===================\nbrowser:'+capabilities.get('BROWSER', 'ERR GET BROWSER!!!')+'\n---------------------\n')


        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):

        auth_page = AuthPage(self.driver)
        auth_page.open()

