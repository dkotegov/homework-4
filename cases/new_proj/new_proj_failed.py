import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from pages.new_proj import NewProjPage
from steps.auth import AuthSteps
from steps.main import MainSteps
from steps.new_proj import NewProjSteps


# Добавление проекта
class NewProjFailedTest(unittest.TestCase):
    KEY = os.environ['PASSWORD']
    FAILED = 'Название пусто'
    PROJ_NAME = 'ВралУЫЕдр'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='127.17.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.auth_page = AuthSteps(self.driver)
        self.auth_page.open()
        self.auth_page.login(self.KEY)

        self.main_page = MainSteps(self.driver)
        self.main_page.page.menu.new_proj_click()
        self.main_page.page.waitRedirect(NewProjPage.BASE_URL + NewProjPage.PATH)

    def tearDown(self):
        self.driver.quit()

    def test_no_tag_failed(self):
        proj_page = NewProjSteps(self.driver)
        alert = proj_page.fill_form("", "")
        self.assertEqual(alert, self.FAILED)





