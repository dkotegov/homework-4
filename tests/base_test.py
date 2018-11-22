import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from components.login_and_write import login_and_write


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
        #self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()
        # pass

    def test(self):
        login_and_write(self.driver, self.USEREMAIL, self.PASSWORD)
