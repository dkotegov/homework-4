# -*- coding: utf-8 -*-
from tests.pages.BasicPage import BasicPage 
from selenium.webdriver import ActionChains
from LetterSelector import LetterSelector

from selenium.webdriver.common.keys import Keys

class LetterWriter(BasicPage):
  write_letter_button = '.compose-button_white'
  
  email_receiver_field = "input[type='text']"
  subject_field = "input[name='Subject']"
  textbox_field = "div[role='textbox']"
  textbox_first_line = "div[role='textbox'] > div > div:first-child"
  send_letter_button = '.button2__txt:nth-child(1)'
  close_sent_window_button = "span.button2_close[title='Закрыть']"
  banner = "div.layer-window[__mediators='layout-manager']"
  advertisement = 'div.message-sent__wrap'
  
  def __init__(self, driver):
    self.driver = driver
    self.letter_selector = LetterSelector(self.driver)
    
  def click_write_letter_button(self):
    elem = self.wait_render(self.write_letter_button)
    elem.click()

  def enter_email_receiver(self, email):
    elem = self.wait_render(self.email_receiver_field)
    ActionChains(self.driver).click(elem).send_keys(email).perform()
    # It's needed to confirm a receiver
    another_field = self.wait_render(self.subject_field)
    ActionChains(self.driver).click(another_field).perform()
    
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
    self.wait_render(self.advertisement)
    elem = self.wait_render(self.close_sent_window_button)
    ActionChains(self.driver).move_to_element(elem).click(elem).perform()
    # Successful window must be closed before executing other operations
    self.wait_invisible(self.banner)
    
  def select_text(self):
    text_container = self.wait_render(self.textbox_first_line)  
    # select_count = len(text_container.text)
    ActionChains(self.driver).click_and_hold(text_container).send_keys(Keys.CONTROL, Keys.SHIFT, Keys.ARROW_RIGHT).release(text_container).perform()
    # for i in range(select_count):