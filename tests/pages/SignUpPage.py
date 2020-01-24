# -*- coding: utf-8 -*-
import random
import calendar
from BasicPage import BasicPage


class SignUpPage(BasicPage):
  firstname_field = 'input[name="firstname"]'
  lastname_field = 'input[name="lastname"]'
  day_block = '.b-date__day'
  month_block = '.b-date__month'
  year_block = '.b-date__year'
  sex_male_input = 'label[data-mnemo="sex-male"]'
  sex_female_input = 'label[data-mnemo="sex-female"]'
  email_field = 'input[data-blockid="email_name"]'
  email_block = 'div[type="email"] .b-email__domain'
  email_input_mail = 'a[data-text="@mail.ru"]'
  email_input_inbox = 'a[data-text="@inbox.ru"]'
  email_input_list = 'a[data-text="@list.ru"]'
  email_input_bk = 'a[data-text="@bk.ru"]'
  password_field = 'input[name="password"]'
  password_retry_field = 'input[name="password_retry"]'
  password_show_block = '.b-password__eye'
  password_hide_block = '.b-password__eye.b-password__eye_active'
  button_signup = 'button[data-bem="btn"]'
  additional_email_block = 'a.js-signup-simple-link'
  additional_email_field = 'input[name="additional_email"][tabindex="9"]'
  additional_phone_block = 'a.js-signup-link'
  email_popup_message = '.b-vacant-email__message'
  password_popup_message = '.b-password__reasons'
  error_blocks = '.b-form-field__errors__error.js-required.b-form-field__errors__error_visible'
  use_condition_block = '.b-form__controls__message a'
  captcha = '.js-captcha-img.b-captcha__captcha'
  update_captcha_button = 'a[data-input-name="captcha"]'
  captcha_input = '.b-input.b-input_captcha.b-input_responsive'
  captcha_back_button = 'button[data-name="back"]'
  captcha_submit_button = 'button[data-name="submit"]'
  captcha_error_msg = '.b-captcha__error-msg'
  domain_field = 'span.b-email__domain > div > input'
  day_field = 'input[name="days"]'
  month_field = 'input[name="month"]'
  year_field = 'input[name="year"]'
  sex_field = 'div[aria-checked="checked"] input[name="sex"]'

  unit_to_multiplier = {
    "mail": email_input_mail,
    "inbox": email_input_inbox,
    "list": email_input_list,
    "bk": email_input_bk
  }

  def day_input(self, day):
    return ('a[data-text="' + str(day) + '"]')

  def month_input(self, month):
    return ('a[data-text="' + month + '"]')

  def year_input(self, year):
    return ('a[data-text="' + str(year) + '"]')

  def error_message(self, text):
    return ('div[data-text="' + text + '"]')

  def open(self):
    self.driver.get(self.SIGNUP_URL)

  def enter_firstname(self, firstname):
    elem = self.wait_render(self.firstname_field)
    elem.clear()
    elem.send_keys(firstname)
  
  def give_firstname(self):
    elem = self.wait_render(self.firstname_field)
    return elem.get_attribute("value").encode('utf-8', errors='ignore')

  def enter_lastname(self, lastname):
    elem = self.wait_render(self.lastname_field)
    elem.clear()
    elem.send_keys(lastname)

  def give_lastname(self):
    elem = self.wait_render(self.lastname_field)
    return elem.get_attribute("value").encode('utf-8', errors='ignore')

  def enter_day(self, day):
    elem = self.wait_render(self.day_block)
    elem.click()
    elem = self.wait_render(self.day_input(day))
    elem.click()

  def enter_month(self, month):
    elem = self.wait_render(self.month_block)
    elem.click()
    elem = self.wait_render(self.month_input(month))
    elem.click()

  def enter_year(self, year):
    elem = self.wait_render(self.year_block)
    elem.click()
    elem = self.wait_render(self.year_input(year))
    elem.click()

  def click_sex_male(self):
    elem = self.wait_render(self.sex_male_input)
    elem.click()

  def click_sex_female(self):
    elem = self.wait_render(self.sex_female_input)
    elem.click()

  def enter_email(self, email):
    elem = self.wait_render(self.email_field)
    elem.send_keys(email)

  def enter_emaildomain(self, emaildomain):
    elem = self.wait_render(self.email_block)
    elem.click()
    elem = self.wait_render(self.unit_to_multiplier[emaildomain])
    elem.click()

  def enter_password(self, password):
    elem = self.wait_render(self.password_field)
    elem.clear()
    elem.send_keys(password)

  def enter_password_retry(self, password):
    elem = self.wait_render(self.password_retry_field)
    elem.clear()
    elem.send_keys(password)

  def show_password(self):
    elem = self.wait_render(self.password_show_block)
    elem.click()

  def hide_password(self):
    elem = self.wait_render(self.password_hide_block)
    elem.click()
  
  def give_password(self):
    elem = self.wait_render(self.password_field)
    return elem.get_attribute("value").encode('utf-8', errors='ignore')

  def get_captcha_id(self):
    elem = self.wait_render(self.captcha)
    return elem.get_attribute("src").encode('utf-8', errors='ignore')

  def update_captcha(self):
    elem = self.wait_render(self.update_captcha_button)
    elem.click()

  def back_from_captcha(self):
    elem = self.wait_render(self.captcha_back_button)
    elem.click()

  def enter_captcha_code(self, code):
    elem = self.wait_render(self.captcha_input)
    elem.clear()
    elem.send_keys(code)

  def submit_captcha(self):
    elem = self.wait_render(self.captcha_submit_button)
    elem.click()

  def get_captcha_error_message(self):
    elem = self.wait_render(self.captcha_error_msg)
    return elem.text

  def click_additionalemail(self):
    elem = self.wait_render(self.additional_email_block)
    elem.click()

  def click_additionalphone(self):
    elem = self.wait_render(self.additional_phone_block)
    elem.click()

  def enter_additionalemail(self, email):
    elem = self.wait_render(self.additional_email_field)
    elem.clear()
    elem.send_keys(email)

  def click_signup(self):
    elem = self.wait_render(self.button_signup)
    elem.click()
  
  def click_use_condition(self):
    elem = self.wait_render(self.use_condition_block)
    elem.click()

  def enter_signup_data(self, data, simple):
    if 'firstname' in data:
      self.enter_firstname(data['firstname'])
    if 'lastname' in data:      
      self.enter_lastname(data['lastname'])
    if 'day' in data:
      self.enter_day(data['day'])
    if 'month' in data:
      self.enter_month(data['month'])
    if 'year' in data:
      self.enter_year(data['year'])
    if ('sex' in data):
      if (data['sex'] == 'male'):
        self.click_sex_male()
      elif (data['sex'] == 'female'):
        self.click_sex_female()
    if 'email' in data:
      self.enter_email(data['email'])
    if 'domain' in data:
      self.enter_emaildomain(data['domain'])
    if 'password' in data:
      self.enter_password(data['password'])
    if 'password_retry' in data:
      self.enter_password_retry(data['password_retry'])
    if not simple:
      self.click_additionalemail()
    if 'addition_email' in data:
      self.enter_additionalemail(data['addition_email'])

  def get_day(self):
    return int(self.wait_presence_located(self.day_field).get_attribute("value").encode('utf-8', errors='ignore')) + 1

  def get_full_data(self):
    firstname = self.wait_render(self.firstname_field).get_attribute("value").encode('utf-8', errors='ignore')
    lastname = self.wait_render(self.lastname_field).get_attribute("value").encode('utf-8', errors='ignore')
    email = self.wait_render(self.email_field).get_attribute("value").encode('utf-8', errors='ignore')
    password = self.wait_render(self.password_field).get_attribute("value").encode('utf-8', errors='ignore')
    password_retry = self.wait_render(self.password_retry_field).get_attribute("value").encode('utf-8', errors='ignore')

    day = self.get_day()
    month_num = int(self.wait_presence_located(self.month_field).get_attribute("value").encode('utf-8', errors='ignore')) + 1
    month = calendar.month_name[month_num]
    year = int(self.wait_presence_located(self.year_field).get_attribute("value").encode('utf-8', errors='ignore'))

    domain = self.wait_presence_located(self.domain_field).get_attribute("value").encode('utf-8', errors='ignore').split('.')[0]
    sex = self.wait_presence_located(self.sex_field).get_attribute("value").encode('utf-8', errors='ignore')


    data = {
      "firstname": firstname,
      "lastname": lastname,
      "day": day,
      "month": month,
      "year": year,
      "sex": sex,
      "email": email,
      "domain": domain,
      "password": password,
      "password_retry": password_retry
    }

    return data

  def generate_fake_email(self):
    return ('waocustom_emailA' + str(random.randrange(1, 10000000)))

  def generate_fake_password(self):
    return ('CooL!WaOPaSs' + str(random.randrange(1, 10000000)) + '!_1A')
