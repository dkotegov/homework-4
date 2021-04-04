import os
import platform
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.chrome.options import Options

from steps.auth_steps import AuthSteps


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

    def auth(self):
        auth_page = AuthSteps(self.driver)
        auth_page.open_page()
        auth_page.open_login_form()
        auth_page.fill_login_form(self.login, self.password)
        auth_page.close_login_form_by_submit()

    def tearDown(self):
        self.driver.quit()
