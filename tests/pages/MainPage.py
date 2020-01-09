# -*- coding: utf-8 -*-

from BasicPage import BasicPage
from letters.LetterManager import LetterManager
from cleaners.TrashCleaner import TrashCleaner
from menu.navigation.NavigationManager import NavigationManager

class MainPage(BasicPage):
  
  app_loader = 'div#app-loader'
  
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
    
  