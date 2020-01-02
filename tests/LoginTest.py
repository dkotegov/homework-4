# -*- coding: utf-8 -*-
from BasicTest import BasicTest

from pages.LoginPage import LoginPage
from pages.MainPage import MainPage

import time
class LoginTest(BasicTest):
  
  def pre_tests(self):
    self.login_page = LoginPage(self.driver)
    self.login_page.open()
    self.main_page = MainPage(self.driver)
    
  def test_correct_login(self):
    self.login_page.sign_in(self.login, self.password)
    self.login_page.wait_redirect(self.MAIL_URL)
    
  def test_wrong_password(self):
    wrong_password = 'wrongpassword'
    self.login_page.sign_in(self.login, wrong_password)
    test_validation = self.login_page.get_validation_message()
    expected_validation = 'Неверный пароль, попробуйте ещё раз'
    self.assertEqual(test_validation, expected_validation)
    
  def test_yandex_login(self):
    test_login = '123@yandex.ru'
    self.login_page.enter_login(test_login)
    self.login_page.click_continue()
    self.wait_redirect('https://passport.yandex.ru/auth')
  
  def test_gmail_login(self):
    test_login = '123@gmail.com'
    self.login_page.enter_login(test_login)
    self.login_page.click_continue()
    self.wait_redirect('https://accounts.google.com/signin/oauth/identifier')
  
  def test_yahoo_login(self):
    test_login = '123@yahoo.com'
    self.login_page.enter_login(test_login)
    self.login_page.click_continue()
    self.wait_redirect('https://login.yahoo.com/')
    
  def test_rambler_login(self):
    test_login = '123@rambler.ru'
    self.login_page.sign_in(test_login, self.password)
    err = self.login_page.get_protocol_err()
    expected_err = 'Вы можете добавить любой почтовый ящик, поддерживающий сбор почты по протоколу POP/IMAP. Если логин введен неверно, авторизуйтесь заново.'
    self.assertEqual(err, expected_err)
  
  def test_custom_login(self):
    custom_login = 'custom@petrov.ru'
    custom_password = 'customPassword123'
    self.login_page.sign_in(custom_login, custom_password)
    err = self.login_page.get_domain_err()
    expected_err = 'Произошла ошибка! Пожалуйста, повторите попытку через некоторое время или введите имя и пароль другого аккаунта.'
    self.assertEqual(err, expected_err)
  
  def test_empty_password(self):
    empty_password = ''
    self.login_page.sign_in(self.login, empty_password)
    test_validation = self.login_page.get_validation_message()
    expected_validation = 'Поле «Пароль» должно быть заполнено'
    self.assertEqual(test_validation, expected_validation)
  
  def test_signout(self):
    self.login_page.sign_in(self.login, self.password)
    self.login_page.wait_redirect(self.MAIL_URL)
    self.main_page.click_signout()
    self.main_page.wait_redirect(self.MAIN_PAGE_URL)
        