from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base_page_object import BasePageObject

from selenium.common.exceptions import NoSuchElementException

TRY_COUNT = 3

class Message(BasePageObject):

    css_selectors = {
        'read_status': 'button[class~=ll-rs]',
        'flag_status': 'button[class~=ll-fs]',
        'attach_status': 'div[data-test-id="attachment-button"]',
        'author': 'span[class="ll-crpt"]'

    }

    def __init__(self, layout, wait, fix_page=lambda x: log("no fix page to " + x)):
        super(Message, self).__init__(layout, wait, fix_page)
    
    def is_unread(self):
        rs = self.layout.find_element_by_css_selector(self.css_selectors['read_status'])
        status = rs.get_attribute('data-qa-id')
        return status == "unread:true"
            
    def is_flagged(self):
        rs = self.layout.find_element_by_css_selector(self.css_selectors['flag_status'])
        status = rs.get_attribute('data-qa-id')
        return status == "flagged:true"

    def has_attach(self):
        try:
            self.layout.find_element_by_css_selector(self.css_selectors['attach_status'])
            return True
        except NoSuchElementException:
            return False

    def get_author(self):
        try_count = TRY_COUNT
        while try_count:
            try:
                author = self.layout.find_element_by_css_selector(self.css_selectors['author'])
                return author.text.encode('utf-8').strip()
            except NoSuchElementException:
                try_count -= 1
            
        return "NAME_NOT_FOUND"

    def __str__(self):
        return 'M[author={:20}; unread={}; flagged={}, attach={}]'.format(
            self.get_author(),
            self.is_unread(),
            self.is_flagged(),
            self.has_attach()
        )

    def __repr__(self):
        return self.__str__()