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
    error_line_active = error_line + '[@class="createmessage-error"]'
    message_list = '//div[@id="incomingMessagesList"]'
    chat_element = '.chatroom'
    chat_creator = '.chatroom__creator'
    chat_content = '.chatroom__content'


    def search_user(self, query):
        self.fill_input(self.driver.find_element_by_xpath(self.search_line), query)
        self.driver.find_element_by_xpath(self.search_button).click()

    def get_error(self, timeout=1):
        try:
            self.wait_for_presence(By.XPATH, self.error_line_active, timeout=timeout)
            return self.driver.find_element_by_xpath(self.error_line_active).text
        except:
            return None

    def open_dialog_from_list(self, name):
        self.find_dialog_by_name(name).click()

    def find_dialog_by_name(self, name):
        creators = self.driver.find_elements(By.CSS_SELECTOR, self.chat_creator)
        creator = None
        for val in creators:
            if val.text == name:
                creator = val
                break
        assert creator
        return creator

    def check_dialog(self, name, text):
        dialog = self.find_dialog_by_name(name).find_element_by_xpath("..")
        assert dialog.find_element(By.CSS_SELECTOR, self.chat_content).text == text

    def wait_for_load(self):
        self.wait_for_presence(By.XPATH, self.message_list)


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
    message_content = '.message__content'


    def wait_for_load(self):
        self.wait_for_presence(By.XPATH, self.companion_name)

    def get_companion_name(self):
        return self.driver.find_element_by_xpath(self.companion_name).text

    def send_message(self, text, printer=None, **kwargs):
        if printer:
            printer(text, **kwargs)
        else:
            self.fill_input(self.driver.find_element_by_xpath(self.textarea), text)
        butt = self.driver.find_element_by_xpath(self.submit_button)
        butt.click()

    def get_message(self, index=-1):
        messages = self.driver.find_elements(By.CSS_SELECTOR, self.messages)
        if len(messages) == 0:
            return None
        message = messages[index]
        text = message.find_element(By.CSS_SELECTOR, self.message_content).text
        creator = message.find_element_by_xpath(self.message_creator).text
        return {
            'from_me': creator in ['Вы:', 'You:'],
            'creator': creator,
            'text': text,
        }

    def send_message_confirmed(self, text, timeout=10, **kwargs):
        previous = len(self.driver.find_elements(By.CSS_SELECTOR, self.my_messages))
        self.send_message(text, **kwargs)
        try:
            self.wait_for_count_change(By.CSS_SELECTOR, self.my_messages, previous=previous, timeout=timeout)
        except:
            raise TimeoutError
        message = self.get_message(index=-1)
        if kwargs.get('confirmator'):
            kwargs['confirmator'](message, kwargs['count'])
        else:
            assert message['from_me']
            assert message['text'] == text

    def wait_for_count_change(self, method, key, previous=None, timeout=10):
        if not previous:
            previous = len(self.driver.find_elements(method, key))
        WebDriverWait(self.driver, timeout).until(
            lambda driver: len(driver.find_elements(method, key))-previous != 0
        )


    def enter_smiles(self, text, **kwargs):
        self.driver.find_element(By.XPATH, self.smiles_button).click()

        smiles = self.driver.find_elements(By.XPATH, self.atomic_smile)
        for symb in list(text):
            printed=False
            for button in smiles:
                t = button.text
                if t == symb:
                    button.click()
                    printed = True
                    break
            if not printed:
                self.driver.find_element(By.XPATH, self.textarea).send_keys(symb)
