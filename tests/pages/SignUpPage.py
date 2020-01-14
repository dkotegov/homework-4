# -*- coding: utf-8 -*-
import random
import time

from BasicPage import BasicPage

class SignUpPage(BasicPage):
  firstname_field  = 'input[name="firstname"]'
  lastname_field  = 'input[name="lastname"]'
  day_block = '.b-date__day'
  month_block = '.b-date__month'
  year_block = '.b-date__year'
  sex_male_input = 'input[value="male"]'
  sex_female_input = 'input[value="female"]'
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
  
  error_blocks = '.b-form-field__errors__error.js-required.b-form-field__errors__error_visible'
  
  #### dynamic selectors
  def day_input(self, day = 4):
    return ('a[data-text="' + str(day) + '"]')
  
  def month_input(self, month_index = 4):
    months = [
      "Январь",
      "Февраль",
      "Март",
      "Апрель",
      "Май",
      "Июнь",
      "Июль",
      "Август",
      "Сентябрь",
      "Октябрь",
      "Ноябрь",
      "Декабрь"
    ]
    return ('a[data-text="' + months[month_index] + '"]')
  
  def year_input(self, year = 2010):
    return ('a[data-text="' + str(year) + '"]')
  
  #### simple functions
  
  def open(self):
    self.driver.get(self.SIGNUP_URL)
    
  def enter_firstname(self, firstname):
    elem = self.wait_render(self.firstname_field)
    elem.send_keys(firstname)
    
  def enter_lastname(self, lastname):
    elem = self.wait_render(self.lastname_field)
    elem.send_keys(lastname)
    
  def enter_day(self, day):
    elem = self.wait_render(self.day_block)
    elem.click()
    elem = self.wait_render(self.day_input(day))
    elem.send_keys(day)
    
  def enter_month(self, month):
    elem = self.wait_render(self.month_block)
    elem.click()
    elem = self.wait_render(self.month_input(month))
    elem.send_keys(month)
    
  def enter_year(self, year):
    elem = self.wait_render(self.year_block)
    elem.click()
    elem = self.wait_render(self.year_input(year))
    elem.send_keys(year)
  
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
    unit_to_multiplier = {
      "mail": self.email_input_mail,
      "inbox": self.email_input_inbox,
      "list": self.email_input_list,
      "bk": self.email_input_bk
    }
    if emaildomain in unit_to_multiplier:
      mult = unit_to_multiplier[unit]
      elem = self.wait_render(mult)
      elem.click()
    else:
      print("Err 'enter_emaildomain': haven't parametr " + emaildomain + " as domain name!")
      
  def enter_password(self, password):
    elem = self.wait_render(self.password_field)
    elem.send_keys(password)
    
  def enter_password_retry(self, password):
    elem = self.wait_render(self.password_retry_field)
    elem.send_keys(password)
  
  def show_password(self):
    elem = self.wait_render(self.password_show_block)
    elem.click()
    
  def hide_password(self):
    elem = self.wait_render(self.password_hide_block)
    elem.click()
    
  def click_additionalemail(self):
    elem = self.wait_render(self.additional_email_block)
    elem.click()
    
  def click_additionalphone(self):
    elem = self.wait_render(self.additional_phone_block)
    elem.click()
    
  def enter_additionalemail(self, email):
    elem = self.wait_render(self.additional_email_block)
    elem.send_keys(email)
    
  def click_signup(self):
    elem = self.wait_render(self.button_signup)
    elem.click()
    
  def signup(self, data):
    try:
      firstname = data['firstname']
      lastname = data['lastname']
      day = data['day']
      month = data['month']
      year = data['year']
      sex = data['sex']
      email = data['email']
      domain = data['domain']
      password = data['password']
      addition_email = data['addition_email']
      
    except KeyError as e:
      # можно также присвоить значение по умолчанию вместо бросания исключения
      raise ValueError('Undefined unit: {}'.format(e.args[0]))
    
    self.enter_firstname(firstname)
    self.enter_lastname(lastname)
    self.enter_day(day)
    self.enter_month(month)
    self.enter_year(year)
    
    if (sex):
      self.click_sex_male()
    else:
      self.click_sex_female()
      
    self.enter_email(email)
    
    if (not domain):
      self.enter_emaildomain("mail")
    else:
      self.enter_emaildomain(domain)
    
    self.enter_password(password)
    self.enter_password_retry(password)
    
    if (addition_email):
      self.click_additionalemail()
      self.enter_additionalemail(addition_email)
    
    self.click_signup()
    
    #### utils for registration
    
  def generate_fake_email(self):
    return ('waocustom_email' + str(random.randrange(1, 10000000)))
  
  def generate_fake_password(self):
    return ('CooL!WaOPaSs' + str(random.randrange(1, 10000000)) + '!_1A')