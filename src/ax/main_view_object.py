from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base_page_object import BasePageObject
from message import Message


class MainViewObject(BasePageObject):

    locators = {
        'messages_list': (By.CLASS_NAME, 'dataset__items')
    }

    def __init__(self, layout, wait, fix_page):
        super(MainViewObject, self).__init__(layout, wait, fix_page)
        

    def get_messages(self):
        data = self.wait.until(EC.presence_of_element_located(self.locators['messages_list']))

        messages = data.find_elements_by_css_selector('.llc_normal')
        messages = list(map(
            lambda msg: Message(msg, self.wait),
            messages
        ))
        return messages, len(messages)
