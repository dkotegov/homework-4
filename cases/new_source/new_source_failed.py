import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from steps.auth import AuthSteps
from steps.main import MainSteps
from steps.source import SourceSteps


# Добавление ресурса
class NewSourceFailedTest(unittest.TestCase):
    BIG_SOURCE = './sources/big_source.jpeg'
    BIG_SOURCE_STRING = 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAg'
    SUCCESS = 'Сохранение прошло успешно'
    KEY = os.environ['PASSWORD']

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
        self.main_page.go_to_new_source()

    def tearDown(self):
        self.driver.quit()

    def test_new_source_no_tag_failed(self):
        source_page = SourceSteps(self.driver)
        source_page.upload_file(self.BIG_SOURCE)
        source_page.save_img("")
        alert = source_page.do_not_wait_alert()
        self.assertFalse(alert)