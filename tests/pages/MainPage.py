from BasicPage import BasicPage

class MainPage(BasicPage):
  signout_button = '#PH_logoutLink'
  write_letter_button = '.compose-button__wrapper'
  email_receiver_field = "input[type='text']"
  subject_field = "input[name='Subject']"
  send_letter_button = '.button2__txt:nth-child(1)'
  textbox_field = "div[role='textbox']"
  close_sent_window_button = 'span.button2_close'
  letter = 'a.llc:nth-child(1) div.llc__container'
  
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
    
  
  
  def click_letter(self):
    elem = self.wait_render(self.letter)
    elem.click()
    
    
  def click_send_letter_button(self):
    elem = self.wait_render(self.send_letter_button)
    elem.click()
    
  def click_signout(self):
    elem = self.wait_render(self.signout_button)
    elem.click()
