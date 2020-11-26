
from pages.defaultPage import Page, Component

from tests.chat.commonUtils import get_last_msg_from_chat_history
from selenium.webdriver.support.ui import WebDriverWait


class Chat(Page):
    PATH = 'chats'

    @property
    def contacts(self):
        return Contacts(self.driver)

    @property
    def messages(self):
        return Messages(self.driver)


class Contacts(Component):
    CHAT_SUP_BTN = '//*[@id="chat_support_btn"]'
    LOGIN = '//*[@id="loginUser"]'
    PASSWORD = '//*[@id="passUser"]'
    SUBMIT = '//*[@id="sendLogin"]'
    LOGIN_HELLO_MSG = '//*[@id="closeInfo"]'
    CHAT_CONTACTS_LIST = '//*[@id="chat_user_list"]'
    CHAT_CONTACTS_LABEL = '//*[@class="chat_contacts_title"]'
    CHAT_CONTACTS_LIST_WITH_MSG = '//*[@class="chat_people_list"]'

    def go_support(self):
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CHAT_SUP_BTN)
        )
        self.driver.find_element_by_xpath(self.CHAT_SUP_BTN).click()

    def get_contact_list(self):
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CHAT_CONTACTS_LIST)
        )
        html_contacts = self.driver.find_element_by_xpath(self.CHAT_CONTACTS_LIST).get_attribute('innerHTML')
        contacts = []
        while len(html_contacts.split('<li')) > 1:
            after_separator = html_contacts.split('<li')[1]
            html_contacts = after_separator
            one_contact = after_separator.split('class="name">')[-1].split('</div>')[0]
            contacts.append(one_contact)
        return contacts

    def get_contacts_label(self):
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CHAT_CONTACTS_LABEL)
        )
        return self.driver.find_element_by_xpath(self.CHAT_CONTACTS_LABEL).text

    def get_contacts_html(self):
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CHAT_CONTACTS_LIST_WITH_MSG)
        )
        return self.driver.find_element_by_xpath(self.CHAT_CONTACTS_LIST_WITH_MSG).get_attribute('innerHTML')


class Messages(Component):
    CHAT_SEND_MSG_BTN = '//*[@id="chat_send_message_btn"]'
    CHAT_SEND_MSG_TEXT = '//*[@id="message_to_send"]'

    CHAT_EMG_SHOW_BTN = '//*[@id="chat_emoji_img"]'
    CHAT_EMG_MENU = '//*[@id="emoji_selector_menu"]'
    CHAT_EMG_PIZZA = '//*[@id="emojiId_7"]'

    CHAT_STICKER_MENU_BTN = '//*[@id="chat_send_sticker"]'
    CHAT_STICKER_MENU = '//*[@id="sticker_select"]'
    CHAT_FIRST_STICKER = '//*[@class="one_sticker"]'

    CHAT_BACK_TO_CONTACTS_IMG = '//*[@id="chat_show_contacts_img"]'

    CHAT_CHAT_WITH_DIV = '//*[@class="chat_with"]'
    CHAT_HISTORY = '//*[@id="chat_history"]'
    CHAT_LAST_MSG = '//*[@class="chat_clearfix chat_li chat_message chat_float-right  "]:last-child'

    def get_companion_name(self):
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CHAT_CHAT_WITH_DIV)
        )
        return self.driver.find_element_by_xpath(self.CHAT_CHAT_WITH_DIV).text

    def set_msg(self, msg):
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CHAT_SEND_MSG_TEXT)
        )
        self.driver.find_element_by_xpath(self.CHAT_SEND_MSG_TEXT).send_keys(msg)

    def send_msg(self):
        self.driver.find_element_by_xpath(self.CHAT_SEND_MSG_BTN).click()

    def get_msg_count(self):
        html_history = self.driver.find_element_by_xpath(self.CHAT_HISTORY).get_attribute('innerHTML')
        return len(html_history.split('<li class=')) - 1

    def wait_new_msg(self, msg_number):
        x_path_selector = self.CHAT_HISTORY + '/div['+str(msg_number)+']/li'
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(x_path_selector)
        )

    def get_last_msg(self):
        history_html = self.driver.find_element_by_xpath(self.CHAT_HISTORY).get_attribute('innerHTML')
        last_msg = get_last_msg_from_chat_history(history_html)
        return last_msg

    def get_last_msg_date(self):
        history_html = self.driver.find_element_by_xpath(self.CHAT_HISTORY).get_attribute('innerHTML')
        last_msg = get_last_msg_from_chat_history(history_html)
        return last_msg

    def open_emoji_menu(self):
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CHAT_SEND_MSG_TEXT)
        )
        self.driver.find_element_by_xpath(self.CHAT_EMG_SHOW_BTN).click()
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CHAT_EMG_MENU)
        )

    def click_emoji_pizza(self):
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CHAT_EMG_PIZZA)
        )
        self.driver.find_element_by_xpath(self.CHAT_EMG_PIZZA).click()

    def open_sticker_menu(self):
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CHAT_STICKER_MENU_BTN)
        )
        self.driver.find_element_by_xpath(self.CHAT_STICKER_MENU_BTN).click()
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CHAT_STICKER_MENU)
        )

    def click_first_sticker(self):
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CHAT_FIRST_STICKER)
        )
        self.driver.find_element_by_xpath(self.CHAT_FIRST_STICKER).click()

    def get_sticker_path(self):
        history_html = self.driver.find_element_by_xpath(self.CHAT_HISTORY).get_attribute('innerHTML')
        sticker_file_name = history_html.split('/stickers/')[-1].split('"></li>')[0]
        return sticker_file_name

    def back_to_contacts(self):
        WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CHAT_BACK_TO_CONTACTS_IMG)
        )
        self.driver.find_element_by_xpath(self.CHAT_BACK_TO_CONTACTS_IMG).click()
