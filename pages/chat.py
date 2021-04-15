from pages.base_component import Component


class Chat(Component):
    CHAT_ICON = '//div[@id="accordion"]'
    OPEN_CHAT_BTN = '//img[contains(@class, "open-chat-button")]'
    CHAT_INPUT = '//textarea[@name="message"]'
    SEND_BTN = '//button[contains(text(),"Send")]'
    CHAT_POPUP_WINDOW = '//div[@id="chatPopup"]'
    SENT_MESSAGE = '//div[contains(@class, "outgoing_msg")]'
    RECEIVED_MESSAGE = '//div[contains(@class, "received_msg")]'
    MESSAGE_SENDER_ICON = '//img[contains(@class, "message_icon")]'
    CHAT_USER = '//a[contains(@class, "icon-with-text__link")]'

    def move_to_chat_icon(self):
        self._wait_until_clickable(self.CHAT_ICON)
        self._move_to_element(self.CHAT_ICON)

    def click_toggle_chat_btn(self):
        chat_popup = self._find_element(self.CHAT_POPUP_WINDOW)
        displayed = chat_popup.value_of_css_property('display')
        self._wait_until_clickable(self.OPEN_CHAT_BTN).click()

        if displayed != 'none':
            self._wait_until_invisible(self.CHAT_POPUP_WINDOW)
            # time.sleep(0.3)  # this is necessary to wait for the 'api/csrf/' method before sending message

    def enter_message(self, message):
        self._wait_until_clickable(self.CHAT_INPUT)
        self._find_element(self.CHAT_INPUT).send_keys(message)

    def send_entered_message(self):
        self._wait_until_clickable(self.SEND_BTN)
        self._find_element(self.SEND_BTN).click()

    def get_sent_messages(self):
        return [x.text for x in self._find_elements(self.SENT_MESSAGE)]

    def get_received_messages(self):
        return [x.text for x in self._find_elements(self.RECEIVED_MESSAGE)]

    def get_message_senders_icons(self):
        return self._find_elements(self.MESSAGE_SENDER_ICON)

    def get_chat_users(self):
        return self._find_elements(self.CHAT_USER)

