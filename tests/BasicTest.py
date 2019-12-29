import os
import unittest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote

from config import config

from pages.LoginPage import LoginPage

class BasicTest(unittest.TestCase, LoginPage):
  MAIL_URL = 'https://e.mail.ru/inbox'
  LOGIN_URL = 'https://account.mail.ru/login'
  SIGNUP_URL = 'https://account.mail.ru/signup'
  
  login = os.environ.get('LOGIN')
  password = os.environ.get('PASSWORD')
  
  def setUp(self):
    if (config.ON_DRIVER):
      self.driver = webdriver.Chrome(config.DRIVER)
    else:
      # Selenium Grig in development
      nodeURL = "http://localhost:4444/wd/hub";
      capabilities = DesiredCapabilities.chrome();
      capabilities.setBrowserName("chrome");
      capabilities.setVersion("79");
      capabilities.setPlatform(Platform.WIN8_1);
      extent = ExtentReports("./extentReport.html",true,DisplayOrder.NEWEST_FIRST);
      driver = RemoteWebDriver(URL(nodeURL),capabilities);
      self.driver = Remote(
            command_executor = "http://localhost:4444/wd/hub",
            desired_capabilities = getattr(DesiredCapabilities, config.DEFAULT_BROWSER).copy()
        )
    self.pre_tests()

  def tearDown(self):
    self.driver.quit()
    
  def pre_tests(self):
    pass
    
    
        