
from LetterWriter import LetterWriter
from LetterSelector import LetterSelector
from tests.pages.main_page.notifications.NotificationManager import NotificationManager
from tests.pages.main_page.menu.top_menu.TopMenuManager import TopMenuManager
from tests.pages.main_page.confirmationers.RemoveConfirmationer import RemoveConfirmationer
from selenium.webdriver import ActionChains

class LetterManager():
  
  def __init__(self, driver):
      self.driver = driver
      self.letter_writer = LetterWriter(self.driver)
      self.letter_selector = LetterSelector(self.driver)
      self.notification_manager = NotificationManager(self.driver)
      self.top_menu_manager = TopMenuManager(self.driver)
      self.remove_confirmationer = RemoveConfirmationer(self.driver)
       
  def write_letter(self, email, subject, text):
    self.letter_writer.click_write_letter_button()
    self.letter_writer.enter_email_receiver(email)
    self.letter_writer.enter_subject(subject)
    self.letter_writer.enter_textbox(text)
    self.letter_writer.click_send_letter_button()
    self.letter_writer.close_sent_window()
    
  def remove_first_letter(self): 
    self.letter_selector.select_first_letter()
    self.top_menu_manager.remove_letter_from_menu()
    self.notification_manager.hide_notification()
    
  # Call only while in the recycle bin
  def restore_first_letter(self):
    self.letter_selector.select_first_letter()
    self.top_menu_manager.click_top_menu_move_letter_button()
    self.top_menu_manager.click_inbox_menu_item()
    self.notification_manager.hide_notification()
    
  def move_all_letters_to_trash(self):
    self.letter_selector.select_all_letters()
    self.top_menu_manager.remove_letter_from_menu()
    self.remove_confirmationer.confirm()
    # Wait a confirmation of moving
    self.letter_selector.is_there_no_letters()
    self.notification_manager.hide_notification()
  
  # Call only while in the trash
  def restore_all_letters_from_trash(self):
    self.letter_selector.select_all_letters()
    self.top_menu_manager.click_top_menu_move_letter_button()
    self.top_menu_manager.click_inbox_menu_item()
    # Wait a confirmation of restoring
    self.letter_selector.is_there_no_letters()
    self.notification_manager.hide_notification()