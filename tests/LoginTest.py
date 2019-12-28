import os
import unittest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote

from ..config import config
from LoginPage import LoginPage

class LoginTest(unittest.TestCase):
  MAIL_URL = 'https://e.mail.ru/inbox'
  login = os.environ.get('LOGIN')
  password = os.environ.get('PASSWORD')
  
  def setUp(self):
    if (config.ON_DRIVER):
      self.driver = webdriver.Chrome(config.DRIVER)
    else:
      self.driver = Remote(
            command_executor = "http://localhost:4444/wd/hub",
            desired_capabilities = getattr(DesiredCapabilities, config.DEFAULT_BROWSER).copy()
        )
    self.login_page = LoginPage(self.driver)
    self.login_page.open()

  def tearDown(self):
    self.driver.quit()
    
  def test_correct_login(self):
    self.login_page.enter_login(self.login)
    self.login_page.click_next()
    self.login_page.enter_password(self.password)
    self.login_page.click_next()
    self.login_page.wait_redirect(self.MAIL_URL)
    
        