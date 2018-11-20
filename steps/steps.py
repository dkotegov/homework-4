import os
from pages.pages import AuthPage, MailPage, SettingsPage, CreateFilterPage, WriteMailPage

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

class OpenFilterSettings(Step):

    USEREMAIL = 'it-berries'
    PASSWORD = os.environ['PASSWORD']

    def open(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_mail = auth_page.form
        auth_mail.set_login(self.USEREMAIL)
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

    def check(self, folder, subject):
        mail_page = MailPage(self.driver)
        mail_page.open_folder(folder)
        if not mail_page.open_msg_by_subject(subject):
            return False
        self.driver.close()
        mail_window = self.driver.window_handles[0]
        self.driver.switch_to_window(mail_window)
        mail_page = MailPage(self.driver)
        mail_page.open_settings_page()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to_window(window_after)
        settings_page = SettingsPage(self.driver)
        settings_page.open_filters()
        return True


class WriteLetter(Step):

    def open(self):
        settings_page = SettingsPage(self.driver)
        settings_page.write_letter_click()
        self.form = WriteMailPage(self.driver).form

    def setAddressee(self, mail):
        self.form.setAddressee(mail)

    def setSubject(self, subject):
        self.form.setSubject(subject)

    def setCopies(self, copies):
        self.form.setCopies(copies)
    
    def send(self):
        self.form.send()

class CreateNewFilter(Step):
    
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
        self.create_filter_form.change_condition_vale(id, value)

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

    #Auto reply with message
    def repley_with_mesg(self, message):
        self.create_filter_form.repley_click()
        self.create_filter_form.repley_with_mesg_click()
        self.create_filter_form.repley_mesg_set(message)

    #Automatically reply "There is no such addressee"
    def repley_not_found(self):
        self.create_filter_form.repley_click()
        self.create_filter_form.repley_not_found_click()

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

    def save_filter(self):
        self.create_filter_form.save_filter_click()

    def delete(self):
        settings_page = SettingsPage(self.driver)
        settings_page.delelte_filter()

class ChangeFilter(CreateNewFilter):

    def open(self):
        settings_page = SettingsPage(self.driver)
        settings_page.change_filter()
        self.create_filter_form = CreateFilterPage(self.driver).form