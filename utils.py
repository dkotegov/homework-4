from selenium.webdriver import DesiredCapabilities, Remote, ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from selenium.webdriver.common.by import By

class Utils:
    BASE_URL = 'https://m.calendar.mail.ru/login'
    driver = None
    
    def sign_in(self, login, password):
  
        def open():
            url = self.BASE_URL
            self.driver.get(url)
            self.wait_redirect(url)
            self.driver.maximize_window()

        def enter_login(login):
            elem = self.wait_renderbtn('input[name=Login]')
            elem.send_keys(login)

        def enter_password(password):
            elem = self.wait_renderbtn('input[name=Password]')
            elem.send_keys(password)

        def func_login():
            elem = self.wait_renderbtn('.login-button')
            elem.click()
        
        open()
        enter_login(login)
        enter_password(password)
        func_login()
        self.wait_redirect('https://m.calendar.mail.ru/', 10)
        
        
    def wait_redirect(self, url, timeout = 10):
      return WebDriverWait(self.driver, timeout).until(EC.url_matches(url))
    
    def wait_renderbtn(self, selector):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
    
    def wait_presenceLocated(self, selector):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    
    def wait_invisible(self, selector):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))

    def open_sidebar(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.header-menu-item.header-menu-item__sidebutton.header-menu-item__list'))).click()