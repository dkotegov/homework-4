import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from steps.auth import AuthSteps
from steps.main import MainSteps
from steps.transform import TransformSteps


# Преобразование картинки
class TransformTest(unittest.TestCase):
    MIDDLE_SOURCE = './sources/middle_source.jpg'
    FAILED = 'Изображение отсутствует'
    KEY = os.environ['PASSWORD']
    HEIGHT = 100
    WIDTH = 100
    SIZE_LABEL_SUCCESS = 'Ширина: {width}\nВысота: {height}'
    wrong_sizes = [0, "", "a"]

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
        self.main_page.go_to_transform()

    def tearDown(self):
        self.driver.quit()

    def test_transform_success(self):
        transform_page = TransformSteps(self.driver)
        transform_page.set_size(self.HEIGHT, self.WIDTH)
        transform_page.select_image(self.MIDDLE_SOURCE)
        width, height = transform_page.transform_finished()
        self.assertEqual("%s" % self.HEIGHT, height)
        self.assertEqual("%s" % self.WIDTH, width)
        size_label = transform_page.check_size_label()
        self.assertIn(self.SIZE_LABEL_SUCCESS.format(width=self.WIDTH, height=self.HEIGHT), size_label)
        transform_page.go_to_transform()

    def test_transform_wrong_size_failed(self):
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
        




