# -*- coding: utf-8 -*-

from BasicPage import BasicPage
from letters.LetterManager import LetterManager
from menu.navigation.NavigationManager import NavigationManager

class MainPage(BasicPage):
  
  app_loader = 'div#app-loader'
  
  inbox_menu_item = "div.list-item[title='Входящие']"
  confirm_remove_button = '.layer__submit-button'
  
  link_to_clean_trash = "a.link[rel='noopener noreferer']"
  
  def open(self):
    self.driver.get(self.LOGIN_URL)
  
  def __init__(self, driver):
      self.driver = driver
      self.letter_manager = LetterManager(self.driver)
      self.navigation_manager = NavigationManager(self.driver)
    
  # def get_first_letter(self):
  #   elem = self.wait_render(self.first_letter_subject)
  #   return elem
    
  def click_inbox_menu_item(self):
    elem = self.wait_render(self.inbox_menu_item)
    elem.click()
    
  def hide_app_loader(self):
    self.wait_invisible(self.app_loader)
    
  def click_signout(self):
    elem = self.wait_render(self.signout_button)
    elem.click()
    
  def click_confirm_remove_button(self):
    elem = self.wait_render(self.confirm_remove_button)
    elem.click()
    
  def click_link_clean_trash(self):
    elem = self.wait_render(self.link_to_clean_trash)
    elem.click()
    
  def clean_trash(self):
    self.click_link_clean_trash()
    self.click_confirm_remove_button()
    
  