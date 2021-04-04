import os
import platform
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.chrome.options import Options
from steps.BaseSteps import Steps


class BaseTest(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        options = None
        if browser == 'CHROME' and platform.system() == 'Linux':
            # fix for unknown error: DevToolsActivePort file doesn't exist
            options = Options()
            options.add_argument('--no-sandbox')

        self.driver = Remote(
            options=options,
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.login = os.environ['LOGIN']
        self.password = os.environ['PASSWORD']

    def test(self):
        main_page = Steps(self.driver)
        main_page.open_page()
        expected_title = 'OnMeet'
        actual_title = main_page.get_page_title()
        self.assertEqual(actual_title, expected_title,
                         f'Page title {actual_title} does not match {expected_title}')

    def tearDown(self):
        self.driver.quit()
