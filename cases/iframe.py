import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from steps.auth import AuthSteps
from steps.iframe import IframeSteps
from steps.main import MainSteps
from steps.new_proj import NewProjSteps


# Преобразование картинки
class IframeTest(unittest.TestCase):
    KEY = os.environ['PASSWORD']
    SUCCESS = 'page/player?p_id={id}" height="600px" width="100%"'
    FAILED = 'Проект отсутствует'
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
        self.main_page.go_to_new_proj()

        self.proj_page = NewProjSteps(self.driver)
        self.proj_page.fill_form(self.PROJ_NAME, self.PROJ_NAME)
        self.proj_page.back_to_menu()

        self.proj_id = self.main_page.get_proj_id(self.PROJ_NAME)
        self.main_page.go_to_iframe()

        self.frame_page = IframeSteps(self.driver)

        self.createdProj = [self.PROJ_NAME]

    def tearDown(self):
        self.frame_page.back_to_menu()
        for proj in self.createdProj:
            self.main_page.delete_proj(proj)

        self.driver.quit()

    def test_frame_success(self):
        self.frame_page.generate(self.proj_id)
        iframe = self.frame_page.iframe_presents()
        self.assertIn(self.SUCCESS.format(id=self.proj_id), iframe)

    def test_frame_wrong_id_failed(self):
        self.frame_page.generate("a")
        alert = self.frame_page.accept_alert_text()
        self.assertIn(alert, self.FAILED)





