import unittest
import os
from selenium.webdriver import DesiredCapabilities, Remote
from pages.auth_page import AuthPage
from pages.userinfo_page import UserinfoPage


class SuggestTownTest(unittest.TestCase):
    TOWN_PREFIX = 'Мос'
    SUGGEST_LIST = [
        'Москва, Россия',
        'Московский, Московская обл., Россия',
        'Мосальск, Калужская обл., Россия'
    ]

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.authorize()

        userinfo_page = UserinfoPage(self.driver)
        userinfo_page.open()
        userinfo_form = userinfo_page.form
        userinfo_form.set_town(self.TOWN_PREFIX)
        userinfo_form.wait_for_last_suggest(self.SUGGEST_LIST[-1])
        self.assertEqual(self.SUGGEST_LIST, userinfo_form.get_suggests_for_town())