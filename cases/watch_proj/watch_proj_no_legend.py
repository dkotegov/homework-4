import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from steps.auth import AuthSteps
from steps.main import MainSteps
from steps.new_proj import NewProjSteps
from steps.watch import WatchSteps


# Просмотр проекта
class WatchProjTestNoLegend(unittest.TestCase):
    KEY = os.environ['PASSWORD']
    PROJ_NAME = 'ВралУЫЕдр'
    FAILED = 'Легенды отсутствуют'

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
        self.main_page.go_to_new_proj()

        self.proj_page = NewProjSteps(self.driver)
        self.proj_page.fill_form(self.PROJ_NAME, self.PROJ_NAME)
        self.proj_page.back_to_menu()
        self.proj_id = self.main_page.get_proj_id(self.PROJ_NAME)

        self.watch_page = WatchSteps(self.driver)
        self.main_page.go_to_watch(self.proj_id)
        self.watch_page.wait_to_load()

    def tearDown(self):
        self.driver.quit()

    def test_show_slide_missing_failed(self):
        self.watch_page.open_legend_tab()
        alert = self.watch_page.show_empty_slide()
        self.assertEqual(alert, self.FAILED)

