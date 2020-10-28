import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from pages.main import MainPage
from pages.transform import TransformPage
from steps.auth import AuthSteps
from steps.transform import TransformSteps


class TransformTest(unittest.TestCase):
    MIDDLE_SOURCE = './sources/middle_source.jpg'
    PDF_SOURCE = './sources/pdf.pdf'
    FAILED = 'Изображение отсутствует'
    KEY = os.environ['PASSWORD']
    HEIGHT = 100
    WIDTH = 100
    SIZE_LABEL_SUCCESS = 'Ширина: {width}\nВысота: {height}'

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
        self.main_page.menu.transform_click()
        self.main_page.waitRedirect(TransformPage.BASE_URL + TransformPage.PATH)

    def tearDown(self):
        self.driver.quit()

    sources = [MIDDLE_SOURCE, PDF_SOURCE]

    def test_transform_success(self):
        for source in self.sources:
            with self.subTest():
                transform_page = TransformSteps(self.driver)
                transform_page.set_size(self.HEIGHT, self.WIDTH)
                transform_page.select_image(source)
                width, height = transform_page.transform_finished()
                self.assertEqual("%s" % self.HEIGHT, height)
                self.assertEqual("%s" % self.WIDTH, width)
                size_label = transform_page.check_size_label()
                self.assertIn(self.SIZE_LABEL_SUCCESS.format(width=self.WIDTH, height=self.HEIGHT), size_label)
                transform_page.go_to_transform()

    wrong_sizes = [0, "", "a"]

    def test_transform_wrong_size_success(self):
        for size in self.wrong_sizes:
            with self.subTest():
                transform_page = TransformSteps(self.driver)
                transform_page.set_size(size, size)
                transform_page.select_image(self.MIDDLE_SOURCE)
                transform_page.transform()
                size_label = transform_page.check_size_label()
                self.assertIn(self.SIZE_LABEL_SUCCESS.format(width=0, height=0), size_label)
                transform_page.go_to_transform()

    def test_transform_no_file_failed(self):
        transform_page = TransformSteps(self.driver)
        transform_page.set_size(self.HEIGHT, self.WIDTH)
        transform_page.transform()
        alert = transform_page.accept_alert_text()
        self.assertEqual(self.FAILED, alert)
        




