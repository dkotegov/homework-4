# -*- coding: utf-8 -*-

from BasicPage import BasicPage
class MainPage(BasicPage):
  signout_button = '#PH_logoutLink'
  write_letter_button = '.compose-button__wrapper'
  email_receiver_field = "input[type='text']"
  subject_field = "input[name='Subject']"
  send_letter_button = '.button2__txt:nth-child(1)'
  textbox_field = "div[role='textbox']"
  close_sent_window_button = 'span.button2_close.button2_clean.button2_short'
  first_letter = '.llc:first-of-type > .llc__container'
  first_letter_subject = 'a.llc:first-of-type > .llc__container .llc__subject'
  first_letter_text = 'a.llc:first-of-type > .llc__container .llc__snippet'
  first_letter_unread_status = 'a.llc:first-of-type > .llc__container span.ll-rs.ll-rs_is-active'
  first_letter_read_status = 'a.llc:first-of-type .ll-rs'
  # first_letter_avatar = '.llc:first-of-type ll-av__img'
  
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
    elem = self.wait_render(self.close_sent_window_button)
    elem.click()
    
  # Write a new letter
  def write_letter(self, email, subject, text):
    self.click_write_letter_button()
    self.enter_email_receiver(email)
    self.enter_subject(subject)
    self.enter_textbox(text)
    self.click_send_letter_button()
    self.close_sent_window()
    
  def get_first_letter(self):
    elem = self.wait_render(self.first_letter_subject)
    return elem
  
  def get_first_letter_subject(self):
    subject = self.wait_render(self.first_letter_subject)
    return subject.text
  
  def get_first_letter_text(self):
    content = self.wait_render(self.first_letter_text).text
    # We should obtain only the content we written (not sign)
    text = content.split(' ')[0]
    return text
  
  def click_letter(self):
    elem = self.wait_render(self.first_letter)
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
    
  def click_signout(self):
    elem = self.wait_render(self.signout_button)
    elem.click()
