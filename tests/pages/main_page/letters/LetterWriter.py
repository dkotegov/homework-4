# -*- coding: utf-8 -*-
from tests.pages.BasicPage import BasicPage 
from selenium.webdriver import ActionChains

class LetterWriter(BasicPage):
  write_letter_button = '.compose-button_white'
  
  email_receiver_field = "input[type='text']"
  subject_field = "input[name='Subject']"
  textbox_field = "div[role='textbox']"
  send_letter_button = '.button2__txt:nth-child(1)'
  close_sent_window_button = "span.button2_close[title='Закрыть']"
  
  banner = "div.layer-window[__mediators='layout-manager']"
    
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
    
  def click_send_letter_button(self):
    elem = self.wait_render(self.send_letter_button)
    elem.click()
    
  def close_sent_window(self):
    self.wait_render(self.banner)
    elem = self.wait_render(self.close_sent_window_button)
    ActionChains(self.driver).move_to_element(elem).click(elem).perform()
    # Successful window must be closed before executing other operations
    self.wait_invisible(self.banner)