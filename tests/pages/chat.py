from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.base import Page
from tests.pages.component import FormComponent


class ChatPage(Page):
    PATH = '/dialog'

    ROOT = {
        'method': By.XPATH,
        'key': Page.get_xpath_visible('//div[@id="dialogview-page"]')
    }

    def __init__(self, driver):
        Page.__init__(self, driver)
        self.open()

    @property
    def form_list(self):
        return FindCompanyForm(self.driver)

    @property
    def form_concrete(self):
        return ConcreteUserMessagesForm(self.driver)


class FindCompanyForm(FormComponent):
    search_line = '//input[@name="username"]'
    search_button = '//input[@id="newMessageButton"]'
    error_line = '//div[@id="createMessageError"]'
    message_list = '//div[@id="incomingMessagesList"]'

    def search_user(self, query):
        self.fill_input(self.driver.find_element_by_xpath(self.search_line), query)
        self.driver.find_element_by_xpath(self.search_button).click()

    def get_error(self):
        return self.driver.find_element_by_xpath(self.error_line).text


class ConcreteUserMessagesForm(FormComponent):
    companion_name = '//a[@id="chatUser"]'
    messages_list = '//div[@id="MessagesList"]'
    textarea = '//textarea[@id="dialogTextArea"]'
    submit_button = '//form[@id="createMessageData"]/input[@type="submit"]'
    smiles_button = '//img[@id="openSmile"]'
    smiles_pane = '//div[@class="message-form__smile-view"]'
    atomic_smile = '//div[@class="smile__style"]'
    messages = '.message'
    my_messages = '.your-message_background'
    # companion_message = messages + '[@class="'
    message_creator = '//div[@class="message__creator"]'
    message_content = '//div[@class="message__content message__context_margin"]'

    def wait_for_load(self):
        self.wait_for_presence(By.XPATH, self.companion_name)

    def get_companion_name(self):
        return self.driver.find_element_by_xpath(self.companion_name).text

    def send_message(self, text):
        self.fill_input(self.driver.find_element_by_xpath(self.textarea), text)
        butt = self.driver.find_element_by_xpath(self.submit_button)
        butt.click()
        # self.wait_for_presence(By.XPATH, )

    def get_message(self, index=-1):
        messages = self.driver.find_elements(By.CSS_SELECTOR, self.messages)
        if len(messages) == 0:
            return None
        message = messages[index]
        text = message.find_element_by_xpath(self.message_content).text
        creator = message.find_element_by_xpath(self.message_creator).text
        print(creator)
        return {
            'from_me': creator in ['Вы:', 'You:'],
            'creator': creator,
            'text': text,
        }

    def send_message_confirmed(self, text):
        previous = len(self.driver.find_elements(By.CSS_SELECTOR, self.my_messages))
        self.send_message(text)
        self.wait_for_count_change(By.CSS_SELECTOR, self.my_messages, previous=previous)
        message = self.get_message(index=-1)
        assert message['from_me']
        assert message['text'] == text

    # def wait_for_my_message(self):
    #     self.wait_for_count_change(By.CSS_SELECTOR, self.my_messages)

    def wait_for_count_change(self, method, key, previous=None, timeout=10):
        if not previous:
            previous = len(self.driver.find_elements(method, key))
        WebDriverWait(self.driver, timeout).until(
            lambda driver: len(driver.find_elements(method, key))-previous != 0
        )
