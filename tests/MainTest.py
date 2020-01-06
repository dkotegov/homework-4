from pages.MainPage import MainPage
from BasicTest import BasicTest
import time

class MainTest(BasicTest):
  
  def pre_tests(self):
    self.main_page = MainPage(self.driver)
    self.main_page.open()
    self.auth()
    
  def test_new_letter(self):
    self.main_page.click_write_letter_button()
    self.main_page.enter_email_receiver(self.login)
    self.main_page.enter_subject("Subject_1")
    self.main_page.enter_textbox('Text1')
    self.main_page.click_send_letter_button()
    self.main_page.close_sent_window()
    time.sleep(3)
    self.main_page.click_letter()
    time.sleep(2)
