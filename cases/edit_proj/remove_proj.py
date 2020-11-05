import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from steps.auth import AuthSteps
from steps.main import MainSteps
from steps.new_proj import NewProjSteps


# Удаление проекта
class RemoveProjTest(unittest.TestCase):
    KEY = os.environ['PASSWORD']
    SUCCESS = 'Клонирование прошло успешно'
    SUCCESS_DELETE = 'Удаление прошло успешно'
    FAILED = 'Имя проекта уже занято'
    PROJ_NAME = 'ВралУЫЕдр'
    CLONE_NAME = 'ВввфвЦццр'

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

    def tearDown(self):
        self.driver.quit()

    def test_remove_success(self):
        alert = self.main_page.delete_proj(self.PROJ_NAME)
        self.assertEqual(alert, self.SUCCESS_DELETE)
