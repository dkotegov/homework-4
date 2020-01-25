# -*- coding: utf-8 -*-
import datetime
import random
import time

from BasicTest import BasicTest
from pages.MainPage import MainPage
from pages.SignUpPage import SignUpPage


class SignUpTest(BasicTest):
    ERROR_FIRSTNAME = u'Укажите имя'
    ERROR_LASTNAME = u'Укажите фамилию'
    ERROR_BIRTHDATE = u'Укажите дату рождения'
    ERROR_SEX = u'Укажите ваш пол'
    ERROR_EMAIL = u'Укажите желаемое имя аккаунта'
    ERROR_PASSWORD_EMPTY = u'Укажите пароль'
    ERROR_SHORT_PASSWORD = u'Используйте не менее 8 символов'
    ERROR_FUTURE_DATE = u'Машину времени еще не изобрели, Марти, выбери другую дату'

    def setUp(self):
        super(SignUpTest, self).setUp()
        self.signup_page = SignUpPage(self.driver)
        self.signup_page.open()

    # Из-за ограничений антиспама регистрация не всегда проходит
    # Поэтому эта функция жмет на кнопку регистрации,
    # пока не произойдет переход на следующую страницу
    def anti_bot_register(self):
        while(True):
            try:
                self.signup_page.click_signup()
                self.signup_page.wait_redirect(self.SIGNUP_VERIFY_URL, 7)

                return
            except:
                pass

    def test_correct_registration_mail(self):  # Work only in corp network
        email = self.signup_page.generate_fake_email()
        password = self.signup_page.generate_fake_password()

        data = {
            "firstname": "Abba",
            "lastname": "Miya",
            "day": 16,
            "month": "May",
            "year": 1999,
            "sex": "male",
            "email": email,
            "domain": "mail",
            "password": password,
            "password_retry": password
        }

        self.signup_page.enter_signup_data(data, False)
        self.anti_bot_register()

    def test_correct_registration_inbox(self):  # Work only in corp network
        email = self.signup_page.generate_fake_email()
        password = self.signup_page.generate_fake_password()

        data = {
            "firstname": "1",
            "lastname": "2",
            "day": 16,
            "month": "May",
            "year": 1999,
            "sex": "female",
            "email": email,
            "domain": "inbox",
            "password": password,
            "password_retry": password
        }

        self.signup_page.enter_signup_data(data, False)
        self.anti_bot_register()

    def test_correct_registration_list(self):  # Work only in corp network
        email = self.signup_page.generate_fake_email()
        password = self.signup_page.generate_fake_password()

        data = {
            "firstname": "1",
            "lastname": "2",
            "day": 16,
            "month": "May",
            "year": 1999,
            "sex": "male",
            "email": email,
            "domain": "list",
            "password": password,
            "password_retry": password
        }

        self.signup_page.enter_signup_data(data, False)
        self.anti_bot_register()

    def test_correct_registration_bk(self):  # Work only in corp network
        email = self.signup_page.generate_fake_email()
        password = self.signup_page.generate_fake_password()

        data = {
            "firstname": "1",
            "lastname": "2",
            "day": 29,
            "month": "February",
            "year": 2016,
            "sex": "female",
            "email": email,
            "domain": "bk",
            "password": password,
            "password_retry": password
        }

        self.signup_page.enter_signup_data(data, False)
        self.anti_bot_register()

    def test_correct_registration_firstname_more_40_chars(self):
        FIRSTNAME = "f"*41

        self.signup_page.enter_firstname(FIRSTNAME)
        wrote_text = self.signup_page.give_firstname()

        EXPECTED = 40

        self.assertEqual(EXPECTED, len(wrote_text))

    def test_correct_registration_lastname_more_40_chars(self):
        LASTNAME = "f"*41

        self.signup_page.enter_lastname(LASTNAME)
        wrote_text = self.signup_page.give_lastname()

        EXPECTED = 40

        self.assertEqual(EXPECTED, len(wrote_text))

    def test_empty_data(self):
        data = {}

        self.signup_page.enter_signup_data(data, False)
        self.signup_page.click_signup()

        elem_err_firstname = self.signup_page.wait_render(
            self.signup_page.error_message(self.ERROR_FIRSTNAME))
        elem_err_lastname = self.signup_page.wait_render(
            self.signup_page.error_message(self.ERROR_LASTNAME))
        elem_err_birthdate = self.signup_page.wait_render(
            self.signup_page.error_message(self.ERROR_BIRTHDATE))
        elem_err_sex = self.signup_page.wait_render(
            self.signup_page.error_message(self.ERROR_SEX))
        elem_err_email = self.signup_page.wait_render(
            self.signup_page.error_message(self.ERROR_EMAIL))
        elem_err_password_empty = self.signup_page.wait_render(
            self.signup_page.error_message(self.ERROR_PASSWORD_EMPTY))

        self.assertEqual(self.ERROR_FIRSTNAME, elem_err_firstname.text)
        self.assertEqual(self.ERROR_LASTNAME, elem_err_lastname.text)
        self.assertEqual(self.ERROR_BIRTHDATE, elem_err_birthdate.text)
        self.assertEqual(self.ERROR_SEX, elem_err_sex.text)
        self.assertEqual(self.ERROR_EMAIL, elem_err_email.text)
        self.assertEqual(self.ERROR_PASSWORD_EMPTY,
                         elem_err_password_empty.text)

    def test_future_date(self):
        email = self.signup_page.generate_fake_email()
        password = self.signup_page.generate_fake_password()
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        year = int(tomorrow.strftime('%Y'))
        month = tomorrow.strftime('%B')
        day = int(tomorrow.strftime('%d'))

        data = {
            "firstname": '1',
            "lastname": '2',
            "day": day,
            "month": month,
            "year": year,
            "sex": "male",
            "email": email,
            "domain": "bk",
            "password": password,
            "password_retry": password
        }

        self.signup_page.enter_signup_data(data, False)
        self.signup_page.click_signup()

        elem_err = self.signup_page.wait_render(
            self.signup_page.error_message(self.ERROR_FUTURE_DATE))
        self.assertEqual(self.ERROR_FUTURE_DATE, elem_err.text)

    def test_short_password(self):
        email = self.signup_page.generate_fake_email()
        SHORT_PASSWORD = '1'

        data = {
            "firstname": '1',
            "lastname": '2',
            "day": 4,
            "month": "April",
            "year": 2000,
            "sex": "male",
            "email": email,
            "domain": "mail",
            "password": SHORT_PASSWORD,
            "password_retry": SHORT_PASSWORD
        }

        self.signup_page.enter_signup_data(data, False)
        self.signup_page.click_signup()

        elem_err = self.signup_page.wait_render(
            self.signup_page.error_message(self.ERROR_SHORT_PASSWORD))
        self.assertEqual(self.ERROR_SHORT_PASSWORD, elem_err.text)

    def test_weak_password(self):
        email = self.signup_page.generate_fake_email()
        WEAK_PASSWORD = '12345678'

        data = {
            "firstname": '1',
            "lastname": '2',
            "day": 4,
            "month": "April",
            "year": 2000,
            "sex": "male",
            "email": email,
            "domain": "mail",
            "password": WEAK_PASSWORD,
            "password_retry": WEAK_PASSWORD
        }

        self.signup_page.enter_signup_data(data, False)
        self.signup_page.click_signup()

        password_err_popup = self.signup_page.wait_render(
            self.signup_page.password_popup_message)

        expected_message = u'Не используйте личные данные, последовательности (123456, qwerty) и популярные пароли (password).'

        self.assertEqual(expected_message, password_err_popup.text)

    def test_bad_password(self):
        email = self.signup_page.generate_fake_email()
        bad_password = email

        data = {
            "firstname": '1',
            "lastname": '2',
            "day": 4,
            "month": "April",
            "year": 2000,
            "sex": "male",
            "email": email,
            "domain": "mail",
            "password": bad_password,
            "password_retry": bad_password
        }

        self.signup_page.enter_signup_data(data, False)
        self.signup_page.click_signup()

        password_err_popup = self.signup_page.wait_render(
            self.signup_page.password_popup_message)

        EXPECTED_MESSAGE = u'Не используйте имя аккаунта и другие личные данные'

        self.assertEqual(EXPECTED_MESSAGE, password_err_popup.text)

    def test_user_exists(self):
        EXISTING_LOGIN = 'TPWAO'
        password = self.signup_page.generate_fake_password()

        data = {
            "firstname": '1',
            "lastname": '2',
            "day": 4,
            "month": "April",
            "year": 2000,
            "sex": "male",
            "email": EXISTING_LOGIN,
            "domain": "mail",
            "password": password,
            "password_retry": password
        }

        self.signup_page.enter_signup_data(data, False)
        self.signup_page.click_signup()

        email_err_popup = self.signup_page.wait_render(
            self.signup_page.email_popup_message)

        EXPECTED_MESSAGE = u'Аккаунт с таким именем уже существует.\nВозможно, вам понравятся имена:'

        self.assertEqual(EXPECTED_MESSAGE, email_err_popup.text)

    def test_incorrect_login(self):
        INCORRECT_LOGIN = 'TPWAO@'
        password = self.signup_page.generate_fake_password()

        data = {
            "firstname": '1',
            "lastname": '2',
            "day": 4,
            "month": "January",
            "year": 2000,
            "sex": "male",
            "email": INCORRECT_LOGIN,
            "domain": "bk",
            "password": password,
            "password_retry": password
        }

        self.signup_page.enter_signup_data(data, False)
        self.signup_page.click_signup()

        email_err_popup = self.signup_page.wait_render(
            self.signup_page.email_popup_message)

        EXPECTED_MESSAGE = u'Некорректное имя аккаунта. Допустимо использовать только латинские буквы, цифры,\nзнак подчеркивания («_»), точку («.»), минус («-»)'

        self.assertEqual(EXPECTED_MESSAGE, email_err_popup.text)

    def test_cyrillic_login(self):
        CYRILLIC_LOGIN = u' гошан777'
        password = self.signup_page.generate_fake_password()

        data = {
            "firstname": '1',
            "lastname": '2',
            "day": 4,
            "month": "April",
            "year": 2000,
            "sex": "male",
            "email": CYRILLIC_LOGIN,
            "domain": "mail",
            "password": password,
            "password_retry": password
        }

        self.signup_page.enter_signup_data(data, False)
        self.signup_page.click_signup()

        email_err_popup = self.signup_page.wait_render(
            self.signup_page.email_popup_message)

        EXPECTED_MESSAGE = u'В имени аккаунта нельзя использовать кириллицу'

        self.assertEqual(EXPECTED_MESSAGE, email_err_popup.text)

    def test_hiding_password(self):
        self.signup_page.click_use_condition()
        self.driver.switch_to.window(window_name=self.driver.window_handles[1])
        self.signup_page.wait_redirect(self.SIGNUP_USE_CONDITION)

    def test_captcha_update(self):
        email = self.signup_page.generate_fake_email()
        password = self.signup_page.generate_fake_password()

        data = {
            "firstname": "Abba",
            "lastname": "Miya",
            "day": 16,
            "month": "May",
            "year": 1999,
            "sex": "male",
            "email": email,
            "domain": "mail",
            "password": password,
            "password_retry": password
        }

        self.signup_page.enter_signup_data(data, False)
        self.anti_bot_register()
        captcha_id = self.signup_page.get_captcha_id()
        self.signup_page.update_captcha()
        new_captcha_id = self.signup_page.get_captcha_id()

        self.assertFalse(captcha_id == new_captcha_id)

    def test_back_from_captcha(self):
        email = self.signup_page.generate_fake_email()
        password = self.signup_page.generate_fake_password()

        data = {
            "firstname": "Abba",
            "lastname": "Miya",
            "day": 16,
            "month": "May",
            "year": 1999,
            "sex": "male",
            "email": email,
            "domain": "mail",
            "password": password,
            "password_retry": password
        }

        self.signup_page.enter_signup_data(data, False)
        self.anti_bot_register()

        self.signup_page.back_from_captcha()

        self.signup_page.wait_redirect(self.SIGNUP_URL)

    def test_you_shall_not_pass(self):
        WRONG_CAPTCHA_CODE = 'Balrog'
        email = self.signup_page.generate_fake_email()
        password = self.signup_page.generate_fake_password()

        data = {
            "firstname": "Abba",
            "lastname": "Miya",
            "day": 16,
            "month": "May",
            "year": 1999,
            "sex": "male",
            "email": email,
            "domain": "mail",
            "password": password,
            "password_retry": password
        }

        self.signup_page.enter_signup_data(data, False)
        self.anti_bot_register()

        self.signup_page.enter_captcha_code(WRONG_CAPTCHA_CODE)
        self.signup_page.submit_captcha()

        EXPECTED_MESSAGE = u'Вы указали неправильный код с картинки'
        error_msg = self.signup_page.get_captcha_error_message()

        self.assertEqual(EXPECTED_MESSAGE, error_msg)

    def test_empty_captcha(self):
        email = self.signup_page.generate_fake_email()
        password = self.signup_page.generate_fake_password()

        data = {
            "firstname": "Abba",
            "lastname": "Miya",
            "day": 16,
            "month": "May",
            "year": 1999,
            "sex": "male",
            "email": email,
            "domain": "mail",
            "password": password,
            "password_retry": password
        }

        self.signup_page.enter_signup_data(data, False)
        self.anti_bot_register()

        self.signup_page.submit_captcha()

        EXPECTED_MESSAGE = u'Укажите код с картинки'
        error_msg = self.signup_page.get_captcha_error_message()

        self.assertEqual(EXPECTED_MESSAGE, error_msg)

    def test_form_keep_data(self):
        email = self.signup_page.generate_fake_email()
        password = self.signup_page.generate_fake_password()

        data = {
            "firstname": "Abba",
            "lastname": "Miya",
            "day": 16,
            "month": "May",
            "year": 1999,
            "sex": "male",
            "email": email,
            "domain": "mail",
            "password": password,
            "password_retry": password
        }

        self.signup_page.enter_signup_data(data, False)
        self.anti_bot_register()

        self.signup_page.back_from_captcha()
        self.signup_page.wait_redirect(self.SIGNUP_URL)

        kept_data = self.signup_page.get_full_data()

        self.assertDictEqual(data, kept_data)

    def test_change_date_after_back(self):
        email = self.signup_page.generate_fake_email()
        password = self.signup_page.generate_fake_password()

        data = {
            "firstname": "Abba",
            "lastname": "Miya",
            "day": 16,
            "month": "May",
            "year": 1999,
            "sex": "male",
            "email": email,
            "domain": "mail",
            "password": password,
            "password_retry": password
        }

        self.signup_page.enter_signup_data(data, False)
        self.anti_bot_register()

        self.signup_page.back_from_captcha()
        self.signup_page.wait_redirect(self.SIGNUP_URL)

        NEW_DATA = {
            "firstname": "Privet"
        }

        self.signup_page.enter_signup_data(NEW_DATA, True)
        self.anti_bot_register()

    def test_incorrect_date(self):
        self.signup_page.enter_month("February")
        self.signup_page.enter_year(2016)

        self.assertTrue(self.signup_page.day_input(30))

    def test_max_month_date(self):
        self.signup_page.enter_day(31)
        self.signup_page.enter_month("November")

        day_number = self.signup_page.get_day()

        EXPECTED = 30

        self.assertEqual(day_number, EXPECTED)
