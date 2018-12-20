# -*- coding: utf-8 -*-

import os
from pages.pages import AuthPage, MailPage, SettingsPage, CreateFilterPage, WriteMailPage
from selenium.common.exceptions import TimeoutException

class Rule():
    field_from = 'From'
    field_to = 'To'
    field_subject = 'Subject'
    field_copy = 'Cc'
    field_redirected_from = 'Resent-From'
    field_redirected_to = 'Resent-To'
    size_KB = 'Size'

class Step(object):

    def __init__(self, driver):
        self.driver = driver

class LogOut(Step):

    def log_out(self):
        #log out of the mailbox

        self.driver.close()
        mail_window = self.driver.window_handles[0]
        self.driver.switch_to_window(mail_window)
        mail_page = MailPage(self.driver)
        mail_page.log_out()

class OpenFilterSettings(Step):
    #enter your mailbox and open the filter settings page

    PASSWORD = os.environ['PASSWORD']

    def open(self, usermail):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_mail = auth_page.form
        auth_mail.set_login(usermail)
        auth_mail.set_password(self.PASSWORD)
        auth_mail.submit()

        mail_page = MailPage(self.driver)
        mail_page.open_settings_menu()
        mail_page.open_settings_page()

        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        settings_page = SettingsPage(self.driver)
        settings_page.open_filters()

class CheckFilterWork(Step):

    def check_if_letter_exists_and_open_it(self, folder, subject):
        #check that the message is in the folder and open it

        mail_page = MailPage(self.driver)
        mail_page.open_folder(folder)
        mail_page.open_msg_by_subject(subject)
        mail_page.check_if_letter_is_open(subject)
        return True

    def get_number_of_letters(self):
        mail_page = MailPage(self.driver)
        return mail_page.get_number_of_letters()

    def check_if_letter_not_exists(self, folder, was_n_letters):
        #check that the message is in the folder and open it

        mail_page = MailPage(self.driver)
        mail_page.open_folder(folder)
        print('before result')
        result = mail_page.get_number_of_letters()
        print('after get number of letters')
        print(was_n_letters)
        print(result)
        if result == was_n_letters:
            return True
        else:
            return False

    def check_if_letter_have_flag(self, folder, subject):
        #find a message the a topic with a flag

        mail_page = MailPage(self.driver)
        mail_page.open_folder(folder)
        result = mail_page.find_msg_by_subject_with_flag(subject)
        return result

    def check_if_letter_already_read(self, folder, subject):
        mail_page = MailPage(self.driver)
        mail_page.open_folder(folder)
        result = mail_page.find_msg_by_subject_which_read(subject)
        return result
        
    def delete_letter(self, subject):
        mail_page = MailPage(self.driver)
        mail_page.check_if_letter_is_open(subject)
        mail_page.delete_letter()

    def open_filters_page_in_new_window(self):
        mail_window = self.driver.window_handles[1]
        self.driver.switch_to_window(mail_window)
        self.driver.close()
        mail_window = self.driver.window_handles[0]
        self.driver.switch_to_window(mail_window)
        mail_page = MailPage(self.driver)
        mail_page.open_settings_menu()
        mail_page.open_settings_page()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        settings_page = SettingsPage(self.driver)
        settings_page.open_filters()

class WriteLetter(Step):

    #send message by parameters
    def send_letter(self, addressee, subject):
        self.open()
        self.setAddressee(addressee)
        self.setSubject(subject)
        self.send()

    #open a new message window
    def open(self):
        settings_page = SettingsPage(self.driver)
        settings_page.write_letter_click()
        self.form = WriteMailPage(self.driver).form

    #set the addressee
    def setAddressee(self, mail):
        self.form.setAddressee(mail)

    #set the subject of the message
    def setSubject(self, subject):
        self.form.setSubject(subject)

    #set the subject of the message
    def setCopies(self, copies):
        self.form.setCopies(copies)
    
    #send message
    def send(self):
        self.form.send()

class CreateNewFilter(Step):
    
    PASSWORD = os.environ['PASSWORD']
    
    #Opens the creation of a filter from the settings page (https://e.mail.ru/settings/filters?octaviusMode=1).
    def open(self):
        settings_page = SettingsPage(self.driver)
        settings_page.create_new_filter()
        self.create_filter_form = CreateFilterPage(self.driver).form
    
    #Changes the filter condition parameter
    def change_condition(self, condition, id):
        self.create_filter_form.change_condition_open(id)
        self.create_filter_form.set_condition_property(id, condition)
    
    #Sets the reverse for the condition
    def change_condition_effect(self, id):
        self.create_filter_form.change_value_effect(id)

    def change_condition_value(self, id, value):
        self.create_filter_form.change_condition_value(id, value)

    def add_condition(self):
        self.create_filter_form.add_condition()
    
    #Switch logical operator for filter condition
    def switch_interaction_conditions(self):
        self.create_filter_form.switch_interaction_conditions_click()

    #Set the filter to move messages that meet the conditions in the folder
    def move_to_folder(self, folder):
        self.create_filter_form.move_to_checkbox_click()
        self.create_filter_form.move_to_folder_open()
        self.create_filter_form.set_move_to_folder(folder)

    #Mark messages as read
    def as_read(self):
        self.create_filter_form.move_to_checkbox_click()
        self.create_filter_form.as_read_checkbox_click()
    
    #Flag messages
    def action_flag(self):
        self.create_filter_form.move_to_checkbox_click()
        self.create_filter_form.action_flag_checkbox_click()

    def delete_message(self):
        self.create_filter_form.delete_checkbox_click()

    #Open advanced settings
    def show_other_actions(self):
        self.create_filter_form.other_actions_click()

    #Forward messages to mail
    def forward_to(self, mail):
        self.create_filter_form.forward_checkbox_click()
        self.create_filter_form.forward_set_mail(mail)
    
    #Switch between "copy" and "notification"
    def forward_change_contex(self):
        self.create_filter_form.forward_change_contex()

    #Auto reply switch
    def reply_switch(self):
        self.create_filter_form.reply_click()

    #Auto reply with message
    def reply_with_mesg(self, message):
        self.create_filter_form.reply_click()
        self.create_filter_form.reply_with_mesg_click()
        self.create_filter_form.reply_mesg_set(message)

    #Automatically reply "There is no such addressee"
    def reply_not_found(self):
        self.create_filter_form.reply_click()
        self.create_filter_form.reply_not_found_click()

    #After this filter triggers, apply other filters.
    def continue_to_filter(self):
        self.create_filter_form.move_to_checkbox_click()
        self.create_filter_form.continue_to_filter_click()
    
    #Apply filter to spam
    def spam_on(self):
        self.create_filter_form.spam_click()

    #Apply filter to folders
    def folders_apply(self, folder):
        self.create_filter_form.folders_apply_click()
        self.create_filter_form.filters_folders_open()
        self.create_filter_form.filter_folder_click(folder)

    #Save filter
    def save_filter(self):
        self.create_filter_form.save_filter_click()

    def get_alert(self):
        return self.create_filter_form.get_alert_message()
   
    def get_pop_up_alert(self):
        return self.create_filter_form.get_alert_pop_up_message()

    def set_value_contains_form(self, text):
        self.create_filter_form.set_value_to_contains_form(text)

    def confirm_password(self):
        self.create_filter_form.confirm_form_set_password(self.PASSWORD)
        self.create_filter_form.confirm_form_submit_password('Продолжить')

    #delete last filter
    def delete(self):
        settings_page = SettingsPage(self.driver)
        settings_page.delete_filter()

    #delete all filters
    def delete_all(self):
        settings_page = SettingsPage(self.driver)
        settings_page.delete_all_filters()
    
    #check if filter list exists
    def check_if_filter_list_exists(self):
        settings_page = SettingsPage(self.driver)
        settings_page.check_if_filter_list_exists()

    #Save new filter
    def save(self, confirm_password = False):
        self.save_filter()
        if confirm_password:
            self.confirm_password()
        self.check_if_filter_list_exists()

    #open the settings of the filters of another mailbox
    def switch_mail_box(self, usermail):
        log_out = LogOut(self.driver)
        log_out.log_out()
        open_filter_settings = OpenFilterSettings(self.driver)
        open_filter_settings.open(usermail)

class ChangeFilter(CreateNewFilter):

    #change filter
    def open(self):
        settings_page = SettingsPage(self.driver)
        settings_page.change_filter()
        self.create_filter_form = CreateFilterPage(self.driver).form
    
    def delete(self):
        settings_page = SettingsPage(self.driver)
        settings_page.delete_filter()

    def confirm_password(self):
        self.create_filter_form.confirm_form_set_password(self.PASSWORD)
        self.create_filter_form.confirm_form_submit_password('Принять')

    #base filter change
    def change_filter_default(self, rule, condition, index,  add = False):
        self.open()
        if add:
            self.add_condition()
        self.change_condition(rule, index)
        self.change_condition_value(index, condition)

class Cleaner(Step):
    def delete_all_letters(self):
        mail_window = self.driver.window_handles[0]
        self.driver.switch_to_window(mail_window)
        self.driver.get("https://octavius.mail.ru/inbox/")
        mail_page = MailPage(self.driver)

        mail_page.clear_folders()