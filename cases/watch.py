import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from steps.auth import AuthSteps
from steps.edit import EditSteps
from steps.main import MainSteps
from steps.new_proj import NewProjSteps
from steps.watch import WatchSteps


# Просмотр проекта
class WatchTestWithLegend(unittest.TestCase):
    KEY = os.environ['PASSWORD']
    FAILED_PIN = 'Ресурс отсутствует'
    PROJ_NAME = 'ВралУЫЕдр'
    LEGEND_NAME = 'acPCaycla'

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

        self.main_page.go_to_edit(self.proj_id)

        self.edit_page = EditSteps(self.driver)
        self.edit_page.open_leg_lib()
        self.edit_page.create_legend(self.LEGEND_NAME)
        self.edit_page.accept_alert_text()
        self.edit_page.open_control_lib()
        self.edit_page.save_proj()
        self.edit_page.back_to_menu()

        self.watch_page = WatchSteps(self.driver)
        self.main_page.go_to_watch(self.proj_id)
        self.watch_page.wait_to_load()

        self.createdProj = [self.PROJ_NAME]

    def tearDown(self):
        self.watch_page.back_to_menu()
        for proj in self.createdProj:
            self.main_page.delete_proj(proj)

        self.driver.quit()

    def test_show_panel_success(self):
        result = self.watch_page.hide_panels()
        self.assertTrue(result)

    def test_hide_panel_success(self):
        self.watch_page.hide_panels()

        result = self.watch_page.show_panels()
        self.assertFalse(result)

    def test_show_legend_success(self):
        self.watch_page.open_legend_tab()
        result = self.watch_page.show_legend(self.LEGEND_NAME)
        self.assertTrue(result)

    def test_hide_legend_success(self):
        self.watch_page.open_legend_tab()
        self.watch_page.show_legend(self.LEGEND_NAME)

        result = self.watch_page.hide_legend()
        self.assertFalse(result)

    def test_show_slide_success(self):
        self.watch_page.open_legend_tab()
        result = self.watch_page.show_slide()
        self.assertTrue(result)

    def test_hide_slide_success(self):
        self.watch_page.open_legend_tab()
        self.watch_page.show_slide()

        result = self.watch_page.hide_slide()
        self.assertFalse(result)


class WatchTestNoLegend(unittest.TestCase):
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

        self.createdProj = [self.PROJ_NAME]

    def tearDown(self):
        self.watch_page.back_to_menu()
        for proj in self.createdProj:
            self.main_page.delete_proj(proj)

        self.driver.quit()

    def test_show_slide_missing_failed(self):
        self.watch_page.open_legend_tab()
        alert = self.watch_page.show_empty_slide()
        self.assertEqual(alert, self.FAILED)

