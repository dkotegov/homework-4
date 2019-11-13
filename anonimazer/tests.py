import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from anonimazer.anonimazer import Anonimazer


class TestAnonimazer(unittest.TestCase):

    BROWSER_NAME = os.getenv("SELENIUM_TEST_BROWSER", "CHROME")

    def setUp(self):
        self.email = "6fdovlmuryg1@mail.ru"
        self.comment = "QA-228"
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

        # При нажатии на link "Подробнее", появляется pop-up форма с описанием возможностей анонимайзера.
    def test_more_details_success(self):
        self.anonimazer.redirect_to_anonimazer()
        self.anonimazer.more_details()
        self.assertEqual(True, self.anonimazer.is_more_details_pop_up_open())

    # При нажатии на иконку удаления почтового ящика, появляется pop-up окно, предупреждающее об удалении ящика.
    def test_delete_email_pop_up_open_success(self):
        self.anonimazer.redirect_to_anonimazer()
        self.anonimazer.delete_email(self.email)
        self.assertEqual(True, self.anonimazer.is_delete_pop_up_open())

    # При нажатии на кнопку "Отменить", pop-up окно, предупреждающее об удалении ящика, исчезает, однако ящик остается.
    def test_cancel_delete_email_success(self):
        self.anonimazer.redirect_to_anonimazer()
        self.anonimazer.delete_email(self.email)
        self.assertEqual(True, self.anonimazer.is_delete_pop_up_open())
        self.anonimazer.cancel_delete_email()
        #        self.assertEqual(False, self.anonimazer.is_delete_pop_up_open())
        self.assertEqual(True, self.anonimazer.is_email_alive(self.email))

    # При нажатии на link ящика, появляется pop-up форма редактирования ящика. В EditLine "Комментарий" убираем все символы и вставляем "QA". При нажатии на кнопку "Готово", комментарий возле ящика с которым мы работали изменился на "QA".
    def test_change_comment_success(self):
        self.anonimazer.redirect_to_anonimazer()
        self.assertEqual(True, self.anonimazer.is_email_alive(self.email))
        self.anonimazer.edit_email(self.email)
        self.assertEqual(True, self.anonimazer.is_edit_pop_up_open())
        self.anonimazer.edit_comment(self.comment)
        self.anonimazer.submit_edit()
        self.anonimazer.edit_email(self.email)
        self.assertEqual(self.comment, self.anonimazer.get_comment())







