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
    

class BasicTest(unittest.TestCase):
    MAIL_URL = 'https://e.mail.ru/inbox'
    LOGIN_URL = 'https://account.mail.ru/login'
    SIGNUP_URL = 'https://account.mail.ru/signup'
    AUTH_URL = 'https://e.mail.ru/login'
    auth_frame = 'ag-popup__frame__layout__iframe'

    login = os.environ.get('LOGIN')
    password = os.environ.get('PASSWORD')

    def setUp(self):
        if (config.ON_DRIVER):
            self.driver = webdriver.Chrome(config.DRIVER)
        else:
            # Selenium Grid in development
            nodeURL = 'http://localhost:4444/wd/hub'
            capabilities = DesiredCapabilities.chrome()
            capabilities.setBrowserName("chrome")
            capabilities.setVersion("79")

            self.driver = Remote(
                command_executor=nodeURL,
                desired_capabilities=getattr(
                    DesiredCapabilities, config.DEFAULT_BROWSER).copy()
            )
        self.pre_tests()

    def tearDown(self):
        self.driver.quit()

    def pre_tests(self):
      pass

    def auth(self):
        login_page = LoginPage(self.driver)
        login_page.wait_redirect(self.AUTH_URL)
        login_page.open_iframe(self.auth_frame)
        login_page.sign_in(self.login, self.password)
