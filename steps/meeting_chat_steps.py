from pages.meeting_page import MeetingPage
from steps.base_steps import Steps


class MeetingChatSteps(Steps):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = MeetingPage(driver)

    def open_chat(self):
        self.page.chat.move_to_chat_icon()
        self.page.chat.click_toggle_chat_btn()

    def close_chat(self):
        self.page.chat.click_toggle_chat_btn()

    def send_message(self, message):
        self.page.chat.enter_message(message)
        self.page.chat.send_entered_message()

    def reopen_chat(self):
        self.close_chat()
        self.driver.refresh()
        self.open_chat()

    def get_last_sent_message(self):
        sent_messages = self.page.chat.get_sent_messages()
        last_sent = sent_messages[-1]

        cut_to_idx = last_sent.index('\n')
        return last_sent[:cut_to_idx]

    def get_last_sender_name(self):
        received_msgs = self.page.chat.get_received_messages()
        last_received = received_msgs[-1]

        cut_to_idx = last_received.index('\n')
        return last_received[:cut_to_idx]

    def open_last_sender_profile(self):
        sender = self.page.chat.get_message_senders_icons()[-1]
        sender.click()

    def get_chat_user_name(self, position=0):
        users = self.page.chat.get_chat_users()
        if position > len(users) - 1:
            position = 0

        return users[position].text

    def open_chat_user(self, position=0):
        users = self.page.chat.get_chat_users()
        if position > len(users) - 1:
            position = 0

        users[position].click()
