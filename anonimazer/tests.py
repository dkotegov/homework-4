import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from anonimazer.anonimazer import Anonimazer


class TestAnonimazer(unittest.TestCase):

    BROWSER_NAME = os.getenv("SELENIUM_TEST_BROWSER", "CHROME")

    def setUp(self):
        self.driver = Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            desired_capabilities=DesiredCapabilities.FIREFOX
        )
        print("Driver is ready")
        self.anonimazer = Anonimazer(self.driver)
        print("Anonimazer is ready")

    def tearDown(self):
        self.driver.quit()

    # Открытие pop-up окна после нажатия кнопки "Добавить анонимный адрес"
    def test_pop_up_open_success(self):
        self.anonimazer.redirect_to_anonimazer()
        self.anonimazer.create_new_email()
        self.assertEqual(True, self.anonimazer.is_pop_up_open())

    # Закрытие pop-up окна после нажатия кнопки "Отмена"
    def test_pop_up_close_success(self):
        self.anonimazer.redirect_to_anonimazer()
        self.anonimazer.create_new_email()
        self.anonimazer.close_new_email_pop_up()
        self.assertEqual(False, self.anonimazer.is_pop_up_open())

    # Исчезновение ComboBox c разрешенными доменами, при добавлении знака "At sign"(@) в поле для вводы почты
    def test_at_sign_append(self):
        self.anonimazer.redirect_to_anonimazer()
        self.anonimazer.create_new_email()
        self.anonimazer.enter_email("@")
        self.assertEqual(False, self.anonimazer.is_combobox_in_form())

    # Появление ComboBox c разрешенными доменами, при удалении знака "At sign"(@) из поля для вводы почты
    def test_at_sign_delete(self):
        self.anonimazer.redirect_to_anonimazer()
        self.anonimazer.create_new_email()
        self.anonimazer.enter_email("@")
        self.assertEqual(False, self.anonimazer.is_combobox_in_form())
        self.anonimazer.clear_email()
        self.assertEqual(True, self.anonimazer.is_combobox_in_form())

    # При нажатии на линк "Не вижу код" меняется капча
    def test_captcha_change(self):
        self.anonimazer.redirect_to_anonimazer()
        self.anonimazer.create_new_email()
        c1 = self.anonimazer.get_captcha_url()
        self.anonimazer.change_captcha()
        c2 = self.anonimazer.get_captcha_url()
        self.assertIsNot(c1, c2)







