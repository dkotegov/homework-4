import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote


class BaseTest(unittest.TestCase):
    USEREMAIL = 'park.test.testovich@mail.ru'
    PASSWORD = 'rha_the_best_team'

    # PASSWORD = os.environ['PASSWORD']
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
        )

    def tearDown(self):
        # self.driver.quit()
        pass