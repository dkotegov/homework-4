# -*- coding: utf-8 -*-

from BasicPage import BasicPage
from selenium.webdriver import ActionChains
import time

class MainPage(BasicPage):
  INBOX_URL = 'https://e.mail.ru/inbox/'
  TRASH_URL = 'https://e.mail.ru/trash/'
  SENT_URL = 'https://e.mail.ru/sent/'
  
  write_letter_button = '.compose-button_white'
  
  email_receiver_field = "input[type='text']"
  subject_field = "input[name='Subject']"
  textbox_field = "div[role='textbox']"
  send_letter_button = '.button2__txt:nth-child(1)'
  close_sent_window_button = "span.button2_close[title='Закрыть']"
  
  first_letter = '.llc:first-of-type > .llc__container'
  first_letter_subject = 'a.llc:first-of-type > .llc__container .llc__subject'
  first_letter_text = 'a.llc:first-of-type > .llc__container .llc__snippet'
  first_letter_read_status = 'a.llc:first-of-type .ll-rs'
  first_letter_avatar = '.llc:first-of-type button.ll-av'
  
  nav_inbox_button = "a.nav__item[title='Входящие']"
  nav_sent_button = "a.nav__item[title='Отправленные']"
  nav_trash_button = "a.nav__item[title='Корзина']"
  
  banner = "div.layer-window[__mediators='layout-manager']"
  
  top_menu_move = 'div.portal-menu-element_move'
  top_menu_trash = 'div.portal-menu-element_remove'
  
  
  inbox_menu_item = "div.list-item[title='Входящие']"
  all_letters = 'div.portal-menu-element_select'
  confirm_remove_button = '.layer__submit-button'
  dataset_empty = '.dataset__empty'
  
  notify_inline = '.notify_inline'
  hide_notification_button = '.button2_actions_close'
  
  link_to_clean_trash = "a.link[rel='noopener noreferer']"
  
  def open(self):
    self.driver.get(self.LOGIN_URL)
  
  def click_write_letter_button(self):
    elem = self.wait_render(self.write_letter_button)
    elem.click()

  def enter_email_receiver(self, email):
    elem = self.wait_render(self.email_receiver_field)
    elem.send_keys(email)
    
  def enter_subject(self, subject):
    elem = self.wait_render(self.subject_field)
    elem.send_keys(subject)
    
  def enter_textbox(self, text):
    elem = self.wait_render(self.textbox_field)
    elem.send_keys(text)
    
  def close_sent_window(self):
    self.wait_render(self.banner)
    elem = self.wait_render(self.close_sent_window_button)
    ActionChains(self.driver).move_to_element(elem).click(elem).perform()
    # Successful window must be closed before executing other operations
    self.wait_invisible(self.banner)
    
  ##### Basic operations with a letter ########
  ############################################# 
  
  def write_letter(self, email, subject, text):
    self.click_write_letter_button()
    self.enter_email_receiver(email)
    self.enter_subject(subject)
    self.enter_textbox(text)
    self.click_send_letter_button()
    self.close_sent_window()
    
  def remove_first_letter(self): 
    self.select_first_letter()
    self.click_menu_remove_letter_button()
    self.hide_notification()
    
  # Call only while in the recycle bin
  def restore_first_letter(self):
    self.select_first_letter()
    self.click_top_menu_move_letter_button()
    self.click_inbox_menu_item()
    self.hide_notification()
    
  def move_all_letters_to_trash(self):
    self.select_all_letters()
    self.click_menu_remove_letter_button()
    self.click_confirm_remove_button()
    # Wait a confirmation of moving
    self.is_there_no_letters()
    self.hide_notification()
  
  # Call only while in the trash
  def restore_all_letters_from_trash(self):
    self.select_all_letters()
    self.click_top_menu_move_letter_button()
    self.click_inbox_menu_item()
    # Wait a confirmation of restoring
    self.is_there_no_letters()
    self.hide_notification()
    
  ############################################# 
  #############################################
    
  def click_letter(self):
    elem = self.wait_render(self.first_letter)
    elem.click()
    
  def get_first_letter(self):
    elem = self.wait_render(self.first_letter_subject)
    return elem
  
  def get_first_letter_subject(self):
    subject = self.wait_render(self.first_letter_subject)
    return subject.text
  
  def get_first_letter_text(self):
    content = self.wait_render(self.first_letter_text).text
    # We should obtain only the content we written (not sign)
    text = content.split(' -- ')[0]
    return text
    
  def select_first_letter(self):
    elem = self.wait_render(self.first_letter_avatar)
    ActionChains(self.driver).move_to_element(elem).click(elem).perform()
    
  def click_menu_remove_letter_button(self):
    elem = self.wait_render(self.top_menu_trash)
    elem.click()
    
  def click_top_menu_move_letter_button(self):
    elem = self.wait_render(self.top_menu_move)
    elem.click()
    
  def click_inbox_menu_item(self):
    elem = self.wait_render(self.inbox_menu_item)
    elem.click()
    
  def get_first_letter_read_status(self):
    elem = self.wait_render(self.first_letter_read_status)
    if elem.get_attribute('title') == (u'Пометить прочитанным') or elem.get_attribute('data-title') == (u'Пометить прочитанным'):
      return False
    else:
      return True
    
  def set_first_letter_read_status(self, status):
    elem = self.wait_render(self.first_letter_read_status)
    # Invert status only it's needed
    if self.get_first_letter_read_status() != status:
      elem.click()
      
  def click_send_letter_button(self):
    elem = self.wait_render(self.send_letter_button)
    elem.click()
    
    
  def click_nav_inbox_button(self):
    elem = self.wait_render(self.nav_inbox_button)
    elem.click()
    # Wait for moving to inbox page
    self.wait_redirect(self.INBOX_URL)
    
  def click_nav_trash_button(self):
    elem = self.wait_render(self.nav_trash_button)
    elem.click()
    # Wait for moving to remove page
    self.wait_redirect(self.TRASH_URL)
    
  def click_nav_sent_button(self):
    elem = self.wait_render(self.nav_sent_button)
    elem.click()
    # Wait for moving to remove page
    self.wait_redirect(self.SENT_URL)
    
  def hide_notification(self):
    elem = self.wait_render(self.hide_notification_button)
    ActionChains(self.driver).move_to_element(elem).click(elem).perform()
    self.wait_invisible(self.notify_inline)
    
  def click_signout(self):
    elem = self.wait_render(self.signout_button)
    elem.click()

  def select_all_letters(self):
    elem = self.wait_render(self.all_letters)
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
    
  def is_there_no_letters(self):
    self.wait_render(self.dataset_empty)
    
  