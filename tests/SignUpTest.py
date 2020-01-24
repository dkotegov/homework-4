# -*- coding: utf-8 -*-
import datetime
import random
import time

from BasicTest import BasicTest
from pages.MainPage import MainPage
from pages.SignUpPage import SignUpPage


class SignUpTest(BasicTest):
  error_firstname = 'Enter your first name'
  error_lastname = 'Enter your last name'
  error_birthdate = 'Enter your birth date'
  error_sex = 'Enter your gender'
  error_email = u'Укажите желаемое имя аккаунта'
  error_password_empty = 'Enter your password'
  error_short_password = 'Use at least 8 characters'
  error_future_date = 'Marty, the time machine hasn\'t been invented yet. Select a different date.'

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
        self.signup_page.wait_redirect(self.SIGNUP_VERIFY_URL, 10)

        return
      except:
        pass

  def test_correct_registration_mail(self): # Work only in corp network
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
    
  def test_correct_registration_inbox(self): # Work only in corp network
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
    
  def test_correct_registration_list(self): # Work only in corp network
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
    
  def test_correct_registration_bk(self): # Work only in corp network
    email = self.signup_page.generate_fake_email()
    password = self.signup_page.generate_fake_password()

    data = {
      "firstname": "1",
      "lastname": "2",
      "day": 29 ,
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
    firstname = "f"*41

    self.signup_page.enter_firstname(firstname)
    wrote_text = self.signup_page.give_firstname()
    self.assertEqual(40, len(wrote_text))
    
  def test_correct_registration_lastname_more_40_chars(self):
    lastname = "f"*41

    self.signup_page.enter_lastname(lastname)
    wrote_text = self.signup_page.give_lastname()
    self.assertEqual(40, len(wrote_text))

  def test_empty_data(self):
    data = {}

    self.signup_page.enter_signup_data(data, False)
    self.signup_page.click_signup()

    elem_err_firstname = self.signup_page.wait_render(self.signup_page.error_message(self.error_firstname))
    elem_err_lastname = self.signup_page.wait_render(self.signup_page.error_message(self.error_lastname))
    elem_err_birthdate = self.signup_page.wait_render(self.signup_page.error_message(self.error_birthdate))
    elem_err_sex = self.signup_page.wait_render(self.signup_page.error_message(self.error_sex))
    elem_err_email = self.signup_page.wait_render(self.signup_page.error_message(self.error_email))
    elem_err_password_empty = self.signup_page.wait_render(self.signup_page.error_message(self.error_password_empty))

    self.assertEqual(self.error_firstname, elem_err_firstname.text)
    self.assertEqual(self.error_lastname, elem_err_lastname.text)
    self.assertEqual(self.error_birthdate, elem_err_birthdate.text)
    self.assertEqual(self.error_sex, elem_err_sex.text)
    self.assertEqual(self.error_email, elem_err_email.text)
    self.assertEqual(self.error_password_empty, elem_err_password_empty.text)

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

    elem_err = self.signup_page.wait_render(self.signup_page.error_message(self.error_future_date))
    self.assertEqual(self.error_future_date, elem_err.text)

  def test_short_password(self):
    email = self.signup_page.generate_fake_email()
    short_password = '1'

    data = {
      "firstname": '1',
      "lastname": '2',
      "day": 4,
      "month": "April",
      "year": 2000,
      "sex": "male",
      "email": email,
      "domain": "mail",
      "password": short_password,
      "password_retry": short_password
    }

    self.signup_page.enter_signup_data(data, False)
    self.signup_page.click_signup()

    elem_err = self.signup_page.wait_render(self.signup_page.error_message(self.error_short_password))
    self.assertEqual(self.error_short_password, elem_err.text)

  def test_weak_password(self):
    email = self.signup_page.generate_fake_email()
    weak_password = '12345678'

    data = {
      "firstname": '1',
      "lastname": '2',
      "day": 4,
      "month": "April",
      "year": 2000,
      "sex": "male",
      "email": email,
      "domain": "mail",
      "password": weak_password,
      "password_retry": weak_password
    }

    self.signup_page.enter_signup_data(data, False)
    self.signup_page.click_signup()

    password_err_popup = self.signup_page.wait_render(self.signup_page.password_popup_message)

    expected_message = 'Don\'t use personal data, sequences (123456, qwerty), or common passwords (for example, "password").'

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

    password_err_popup = self.signup_page.wait_render(self.signup_page.password_popup_message)

    expected_message = u'Не используйте имя аккаунта и другие личные данные'

    self.assertEqual(expected_message, password_err_popup.text)

  def test_user_exists(self):
    existing_login = 'TPWAO'
    password = self.signup_page.generate_fake_password()

    data = {
      "firstname": '1',
      "lastname": '2',
      "day": 4,
      "month": "April",
      "year": 2000,
      "sex": "male",
      "email": existing_login,
      "domain": "mail",
      "password": password,
      "password_retry": password
    }

    self.signup_page.enter_signup_data(data, False)
    self.signup_page.click_signup()

    email_err_popup = self.signup_page.wait_render(self.signup_page.email_popup_message)

    expected_message = u'Аккаунт с таким именем уже существует.\nYou might like these email addresses:'

    self.assertEqual(expected_message, email_err_popup.text)

  def test_incorrect_login(self):
    incorrect_login = 'TPWAO@'
    password = self.signup_page.generate_fake_password()

    data = {
      "firstname": '1',
      "lastname": '2',
      "day": 4,
      "month": "April",
      "year": 2000,
      "sex": "male",
      "email": incorrect_login,
      "domain": "mail",
      "password": password,
      "password_retry": password
    }

    self.signup_page.enter_signup_data(data, False)
    self.signup_page.click_signup()

    email_err_popup = self.signup_page.wait_render(self.signup_page.email_popup_message)

    expected_message = u'Некорректное имя аккаунта. Допустимо использовать только латинские буквы, цифры,\nзнак подчеркивания («_»), точку («.»), минус («-»)'

    self.assertEqual(expected_message, email_err_popup.text)

  def test_cyrillic_login(self):
    cyrillic_login = u' гошан777'
    password = self.signup_page.generate_fake_password()

    data = {
      "firstname": '1',
      "lastname": '2',
      "day": 4,
      "month": "April",
      "year": 2000,
      "sex": "male",
      "email": cyrillic_login,
      "domain": "mail",
      "password": password,
      "password_retry": password
    }

    self.signup_page.enter_signup_data(data, False)
    self.signup_page.click_signup()

    email_err_popup = self.signup_page.wait_render(self.signup_page.email_popup_message)

    expected_message = u'В имени аккаунта нельзя использовать кириллицу'

    self.assertEqual(expected_message, email_err_popup.text)

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
    wrong_captcha_code = 'Balrog'
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

    self.signup_page.enter_captcha_code(wrong_captcha_code)
    self.signup_page.submit_captcha()

    expected_message = 'The code you entered from the picture is incorrect'
    error_msg = self.signup_page.get_captcha_error_message()

    self.assertEqual(expected_message, error_msg)

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

    expected_message = 'Enter the code from the picture'
    error_msg = self.signup_page.get_captcha_error_message()

    self.assertEqual(expected_message, error_msg)

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

    new_data = {
      "firstname": "Privet"
    }

    self.signup_page.enter_signup_data(new_data, True)
    self.anti_bot_register()

  def test_incorrect_date(self):
    self.signup_page.enter_month("February")
    self.signup_page.enter_year(2016)

    self.assertTrue(self.signup_page.day_input(30))

  def test_max_month_date(self):
    self.signup_page.enter_day(31)
    self.signup_page.enter_month("November")

    day_number = self.signup_page.get_day()

    self.assertEqual(day_number, 30)
