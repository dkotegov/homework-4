import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from steps.auth import AuthSteps
from steps.main import MainSteps
from steps.source import SourceSteps
from steps.tag import TagSteps


# Список тегов
class TagListAppearsTest(unittest.TestCase):
    BIG_SOURCE = './sources/big_source.jpeg'
    BIG_SOURCE_STRING = 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAg'
    SUCCESS = 'Удаление прошло успешно'
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

        self.source_page = SourceSteps(self.driver)
        self.source_page.upload_file(self.BIG_SOURCE)
        self.source_page.save_img(self.BIG_SOURCE)
        self.source_page.accept_alert_text()
        self.source_page.back_to_menu()

        self.main_page.go_to_tag(self.BIG_SOURCE)
        self.tag_page = TagSteps(self.driver)

    def tearDown(self):
        self.tag_page.delete_source()

        self.driver.quit()

    def test_new_source_appears_success(self):
        image = self.tag_page.image_presents(self.BIG_SOURCE_STRING)
        self.assertIn(self.BIG_SOURCE_STRING, image)
