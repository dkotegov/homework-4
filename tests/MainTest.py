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
    subject = 'Subject_1'
    text = 'Text1'
    self.main_page.enter_subject(subject)
    self.main_page.enter_textbox(text)
    self.main_page.click_send_letter_button()
    self.main_page.close_sent_window()
    actual_subject = self.main_page.get_first_letter_subject()
    actual_text = self.main_page.get_first_letter_text()
    self.assertEqual(subject, actual_subject)
    self.assertEqual(text, actual_text)
    
  def test_unread_status(self):
    self.main_page.write_letter('TPWAO@mail.ru', 'Subject_1', 'Text1')
    self.assertFalse(self.main_page.get_first_letter_read_status())

