import os
from base_page import BasePage
from forms.dialog_form import DialogForm
from forms.attach_form import AttachForm
from forms.message_form import MessageForm
from forms.dialog_menu_form import DialogMenuForm
from delete_message_confirm import DeleteMessageConfirmPage
from confirm import ConfirmPage

from selenium.webdriver.common.action_chains import ActionChains

class DialogPage(BasePage):
    
    def __init__(self, driver):
        super(DialogPage, self).__init__(driver)
        self.dialog_form = DialogForm(self.driver)
        self.attach_form = AttachForm(self.driver)
        self.message_form = MessageForm(self.driver)
        self.dialog_menu_form = DialogMenuForm(self.driver)

    def open_menu(self): 
        self.dialog_form.get_menu_button().click()

    def send_message_button_exists(self):
        return self.dialog_form.get_send_message_button_exists()

    def no_messages_text_exists(self):
        return self.dialog_form.get_no_messages_text_exists() 
    
    def send_sticker(self):
        self.dialog_form.get_sticker_button().click()
        self.dialog_form.get_sticker_list_button().click()
        self.dialog_form.get_unsmile_sticker().click()
    
    def message_with_sticker_exists(self):
        return self.dialog_form.get_message_with_sticker()

    def sent_message_exists(self):
        return self.dialog_form.get_sent_message()

    def send_music(self):
        self.dialog_form.get_attach_button().click()
        self.attach_form.get_music_button().click()
        self.attach_form.get_song().click()
        self.attach_form.get_send_song_button().click()

    def send_document(self):
        self.dialog_form.get_attach_button().click()
        self.attach_form.get_document_input().send_keys(os.getcwd()+"/tests/static/awd.txt")

    def send_photo(self):
        self.dialog_form.get_attach_button().click()
        self.attach_form.get_photo_input().send_keys(os.getcwd()+"/tests/static/sabaton.jpg")
        if(self.attach_form.get_loader()):
            self.dialog_form.get_send_message_button().click()
        
    def send_video(self):
        self.dialog_form.get_attach_button().click()
        self.attach_form.get_video_button().click()
        self.attach_form.get_video_input().send_keys(os.getcwd()+"/tests/static/sabaton.mp4")
        if(self.attach_form.get_loader()):
            self.dialog_form.get_send_message_button().click()

    def wait_for_loader(self):
        self.dialog_form.wait_dialog_loader()

    def find_dialog(self):
        name = self.dialog_form.get_companion_name()
        self.message_form.get_find_dialog_input().send_keys(name)
        return name

    def send_message(self, msg):
        self.dialog_form.get_message_input().send_keys(msg)
        self.dialog_form.get_send_message_button().click()

    def block_user(self):
        self.open_menu()
        self.dialog_menu_form.get_block_unblock_user_button().click()
        block_confirm_page = ConfirmPage(self.driver)
        block_confirm_page.confirm()
    
    def unblock_user(self):
        self.open_menu()
        self.dialog_menu_form.get_block_unblock_user_button().click()
        self.open_menu()

    #Nick112
    
    def edit_and_send_message(self, message_text):
        edit_message_button = self.dialog_form.get_edit_message_button()
        ActionChains(self.driver).move_to_element(edit_message_button).perform()
        edit_message_button.click()   
        self.send_message(message_text)
    
    def get_sent_message_text(self):
        return self.dialog_form.get_sent_message_text()

    def delete_message(self):  
        delete_message_button = self.dialog_form.get_delete_message_button()
        ActionChains(self.driver).move_to_element(delete_message_button).perform()
        delete_message_button.click()  
        delete_message_confirm_page = DeleteMessageConfirmPage(self.driver)
        delete_message_confirm_page.delete_message()

    def answer_message(self, answer_text):
        answer_message_button = self.dialog_form.get_answer_message_button()
        ActionChains(self.driver).move_to_element(answer_message_button).perform()
        answer_message_button.click()  
        self.send_message(answer_text)

    def forward_message(self):
        forward_message_button = self.dialog_form.get_forward_message()
        ActionChains(self.driver).move_to_element(forward_message_button).perform()
        forward_message_button.click()  
        
    
    def get_exsistance_of_answered_message(self):
        return self.dialog_form.get_answered_message()

    def get_exsistance_of_forwarded_message(self):
        return self.dialog_form.get_forward_message_title()

    def find_message(self, msg):
        self.message_form.get_find_dialog_input().send_keys(msg)
    
    def add_user_to_chat(self):
        self.dialog_form.get_add_companion_button().click()
        self.dialog_menu_form.get_companion_button().click()
        self.dialog_menu_form.get_add_companion_confirm_button().click()

    def delete_user_from_chat(self):
        self.dialog_form.get_control_users_button().click()
        delete_companion_button = self.dialog_menu_form.get_delete_companion_button()
        ActionChains(self.driver).move_to_element(delete_companion_button).perform()
        delete_companion_button.click()

    def get_exsistance_of_created_group_dialog(self):
        return self.dialog_form.get_group_chat_created_title()

    def get_exsistance_of_delte_companion(self):
        return self.dialog_form.get_group_chat_delete_title()
    
    def pin_message(self):
        pin_message_button = self.dialog_form.get_pin_button()
        ActionChains(self.driver).move_to_element(pin_message_button).perform()
        pin_message_button.click()  
        pin_message_confirm_page = ConfirmPage(self.driver)
        pin_message_confirm_page.confirm()
    
    def exsistance_of_pinned_message(self):
        return self.dialog_form.get_pinned_message()

    def unpin_message(self):
        self.dialog_form.get_unpin_button().click()
        pin_message_confirm_page = ConfirmPage(self.driver)
        pin_message_confirm_page.confirm()
 