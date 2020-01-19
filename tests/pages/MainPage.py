# -*- coding: utf-8 -*-

from BasicPage import BasicPage
from main_page.letters.LetterManager import LetterManager
from main_page.cleaners.TrashCleaner import TrashCleaner
from main_page.menu.navigation.NavigationManager import NavigationManager
from LoginPage import LoginPage

class MainPage(BasicPage):
  
  app_loader = 'div#app-loader'
  signout_button = '#PH_logoutLink'
  
  def open(self):
    self.driver.get(self.LOGIN_URL)
  
  def __init__(self, driver):
      self.driver = driver
      self.letter_manager = LetterManager(self.driver)
      self.navigation_manager = NavigationManager(self.driver)
      self.trash_cleaner = TrashCleaner(self.driver)
    
  def hide_app_loader(self):
    self.wait_invisible(self.app_loader)
    
  def click_signout(self):
    elem = self.wait_render(self.signout_button)
    elem.click()
  
  def auth(self, email, password):
    login_page = LoginPage(self.driver)
    login_page.sign_in(email, password)
    login_page.wait_redirect(self.MAIL_URL)
        
  def relogin(self, email, password):
    self.click_signout()
    self.open()
    self.auth(email, password)
    self.hide_app_loader()
    
  