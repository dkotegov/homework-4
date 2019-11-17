import unittest
import os
from selenium.webdriver import DesiredCapabilities, Remote
from pages.auth_page import AuthPage
from pages.userinfo_page import UserinfoPage

class GenderTest(unittest.TestCase):
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

        unselected_gender_before = userinfo_form.get_unselected_gender()
        unselected_gender_before_id = unselected_gender_before.id
        unselected_gender_before.click()
        userinfo_form.save()

        userinfo_page.open()
        userinfo_form = userinfo_page.form

        unselected_gender_after = userinfo_form.get_unselected_gender()
        unselected_gender_after_id = unselected_gender_after.id
        self.assertNotEqual(unselected_gender_before_id, unselected_gender_after_id)