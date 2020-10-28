import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from pages.main import MainPage
from pages.source import SourcePage
from steps.auth import AuthSteps
from steps.source import SourceSteps
from steps.tag import TagSteps


class SourceTest(unittest.TestCase):
    BIG_SOURCE = './sources/big_source.jpeg'
    PDF_SOURCE = './sources/pdf.pdf'
    BIG_SOURCE_STRING = 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAg'
    PDF_SOURCE_STRING = 'data:application/pdf;base64,JVBERi0xLjUKJ'
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

        self.main_page = MainPage(self.driver)
        self.main_page.menu.new_source_click()
        self.main_page.waitRedirect(SourcePage.BASE_URL + SourcePage.PATH)

        self.tag_page = TagSteps(self.driver)

    def tearDown(self):
        self.driver.quit()

    sources = [[BIG_SOURCE, BIG_SOURCE_STRING], [PDF_SOURCE, PDF_SOURCE_STRING]]

    def test_new_source_success(self):
        for source in self.sources:
            with self.subTest():
                source_path = source[0]
                source_string = source[1]
                source_page = SourceSteps(self.driver)
                image = source_page.upload_file(source_path)
                self.assertIn(source_string, image)
                source_page.save_img(source_path)
                alert = source_page.accept_alert_text()
                self.assertEqual(alert, self.SUCCESS)

                # Удалить созданные
                source_page.back_to_menu()
                self.main_page.tag_list.tag_click(source_path)
                self.tag_page.delete_source()
                self.tag_page.back_to_menu()
                self.main_page.menu.new_source_click()
                self.main_page.waitRedirect(SourcePage.BASE_URL + SourcePage.PATH)

    def test_new_source_no_tag_failed(self):
        source_page = SourceSteps(self.driver)
        source_page.upload_file(self.PDF_SOURCE)
        source_page.save_img("")
        alert = source_page.do_not_wait_alert()
        self.assertFalse(alert)



