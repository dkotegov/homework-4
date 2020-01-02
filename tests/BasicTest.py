import os
import unittest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote

from config import config

from pages.LoginPage import LoginPage

class BasicTest(unittest.TestCase, LoginPage):
  MAIN_PAGE_URL = 'https://mail.ru/'
  MAIL_URL = 'https://e.mail.ru/inbox'
  LOGIN_URL = 'https://account.mail.ru/login'
  SIGNUP_URL = 'https://account.mail.ru/signup'
  
  login = os.environ.get('LOGIN')
  password = os.environ.get('PASSWORD')
  BROWSER_NAME = os.getenv("SELENIUM_BROWSER", config.DEFAULT_BROWSER)
  BROWSER_VERSION = '79'
  
  def setUp(self):
    if (config.ON_DRIVER):
      self.driver = webdriver.Chrome(config.DRIVER)
    else:
      self.driver = Remote(
          command_executor = "http://localhost:4444/wd/hub",
          desired_capabilities = {
            "browserName":"chrome",
            "browserVersion": "79.0.3945.36"
          }
        )
    self.pre_tests()

  def tearDown(self):
    self.driver.quit()
    
  def pre_tests(self):
    pass
    
    
        