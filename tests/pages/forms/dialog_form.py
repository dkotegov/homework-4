# -*- coding: utf-8 -*-
from base_element import BaseElement

class DialogForm(BaseElement):
    MENU_BUTTON = '//div[@data-additional-button="js-open-menu"]'
    SEND_MESSAGE_BUTTON = '//button[@title="Отправить"]'
    NO_MESSAGES_TEXT = '//div[contains(@class,"stub-empty_t")]'
    MESSAGE_INPUT = '//div[@name="st.txt"]'
    STICKER_BUTTON = '//span[contains(@class, " emoji-m")]'
    STICKER_LIST_BUTTON = '//a[contains(@data-l, "stickersTab")]'
    USMILE_STICKER = '//div[@data-code="#u9b43ee364as#"]'
    ATTACH_BUTTON = "//div[contains(@class, 'comments_attach')]"
    MESSAGE_WITH_STICKER = '//div[contains(@class, "msg_sticker ")]'
    SENT_MESSAGE = '//div[contains(@class,"msg_tx")]'

    SENT_MESSAGE_TEXT = '//div[contains(@class, "msg_tx")]/div[2]/div[1]/span[1]/span[1]'

    DIALOG_LOADER = '//div[contains(@class, "chat_loader")]'

    COMPANION_NAME = '//span[contains(@data-l,"menu_opponent_name")]'

    MESSAGE_INPUT = '//div[contains(@name, "st.txt")]'

    DELETE_MESSAGE_BUTTON =  "//a[contains(@data-l, 'deleteMsg')]"
    PIN_MESSAGE_BUTTON =  "//a[contains(@data-l, 'pinMsg')]"
    EDIT_MESSAGE_BUTTON = "//a[contains(@data-l, 'editMsg')]"
    ANSWER_MESSAGE_BUTTON = "//span[contains(@data-l, 'replyToMsg')]"
    ANSWERED_MESSAGE = '//div[contains(@class,"msg_reply")]'
    FORWARD_MESSAGE = "//span[contains(@data-l, 't,forward')]"
    FORWARDED_MESSAGE_TITLE = '//div[contains(@class,"msg_forward_title")]'
    ADD_COMPANION_BUTTON = '//span[contains(@class, " ic_add-user")]'
    CONTROL_USERS_BUTTON = '//span[contains(@class, " ic_ffriend")]'
    GROUP_CHAT_CREATED_TITLE = '//a[contains(@data-l,"user1FromSysMsg")]'

    GROUP_CHAT_REMOVED_TITLE = '//a[contains(@data-l,"removedUserFromSysMsg")]'

    PINNED_MESSAGE = '//div[contains(@class, "chat_pinned_text")]'
    UNPIN_MESSAGE_BUTTON = "//a[contains(@class,'chat_pinned_close')]"

    def get_menu_button(self):
        return self.get_button_by_xpath(self.MENU_BUTTON)

    def get_send_message_button(self):
        return self.get_button_by_xpath(self.SEND_MESSAGE_BUTTON)
    
    def get_send_message_button_exists(self):
        return self.existance_of_element_by_xpath(self.SEND_MESSAGE_BUTTON)

    def get_no_messages_text_exists(self):
        return self.existance_of_element_by_xpath(self.NO_MESSAGES_TEXT)

    def get_message_input(self):
        return self.get_field_by_xpath(self.MESSAGE_INPUT)
    
    def get_sticker_button(self):
        return self.get_button_by_xpath(self.STICKER_BUTTON)

    def get_sticker_list_button(self):
        return self.get_button_by_xpath(self.STICKER_LIST_BUTTON)

    def get_unsmile_sticker(self):
        return self.get_button_by_xpath(self.USMILE_STICKER)
    
    def get_attach_button(self):
        return self.get_button_by_xpath(self.ATTACH_BUTTON)

    def get_message_with_sticker(self):
        return self.existance_of_element_by_xpath(self.MESSAGE_WITH_STICKER)

    def get_sent_message(self):
        return self.existance_of_element_by_xpath(self.SENT_MESSAGE)
    
    def wait_dialog_loader(self):
        self.existance_of_element_by_xpath(self.DIALOG_LOADER)
        self.invisibility_of_element_by_xpath(self.DIALOG_LOADER)

    def get_companion_name(self):
        return self.get_field_by_xpath(self.COMPANION_NAME).get_attribute('innerHTML')

    def get_message_input(self):
        return self.get_field_by_xpath(self.MESSAGE_INPUT)

    #Nick112

    def get_edit_message_button(self):
        return self.get_hidden_input_by_xpath(self.EDIT_MESSAGE_BUTTON)

    def get_delete_message_button(self):
        return self.get_hidden_input_by_xpath(self.DELETE_MESSAGE_BUTTON)
    
    def get_answer_message_button(self):
        return self.get_hidden_input_by_xpath(self.ANSWER_MESSAGE_BUTTON)

    def get_sent_message_text(self):
        return self.get_button_by_xpath(self.SENT_MESSAGE_TEXT).get_attribute("innerHTML")

    def get_answered_message(self):
        return self.existance_of_element_by_xpath(self.ANSWERED_MESSAGE)

    def get_forward_message(self):
        return self.get_hidden_input_by_xpath(self.FORWARD_MESSAGE)

    def get_forward_message_title(self):
        return self.existance_of_element_by_xpath(self.FORWARDED_MESSAGE_TITLE)
    
    def get_add_companion_button(self):
        return self.get_button_by_xpath(self.ADD_COMPANION_BUTTON)
    
    def get_group_chat_created_title(self):
        return self.existance_of_element_by_xpath(self.GROUP_CHAT_CREATED_TITLE)

    def get_group_chat_delete_title(self):
        return self.existance_of_element_by_xpath(self.GROUP_CHAT_REMOVED_TITLE)
    
    def get_control_users_button(self):
        return self.get_button_by_xpath(self.CONTROL_USERS_BUTTON)
    
    def get_pin_button(self):
        return self.get_hidden_input_by_xpath(self.PIN_MESSAGE_BUTTON)
    
    def get_pinned_message(self):
        return self.existance_of_element_by_xpath(self.PINNED_MESSAGE)

    def get_unpin_button(self):
        return self.get_button_by_xpath(self.UNPIN_MESSAGE_BUTTON)