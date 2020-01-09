# -*- coding: utf-8 -*-
from tests.pages.BasicPage import BasicPage

class NavigationManager(BasicPage):
    INBOX_URL = 'https://e.mail.ru/inbox/'
    TRASH_URL = 'https://e.mail.ru/trash/'
    SENT_URL = 'https://e.mail.ru/sent/'
    
    nav_inbox_button = "a.nav__item[title='Входящие']"
    nav_sent_button = "a.nav__item[title='Отправленные']"
    nav_trash_button = "a.nav__item[title='Корзина']"
    
    def click_nav_inbox_button(self):
        elem = self.wait_render(self.nav_inbox_button)
        elem.click()
        # Wait for moving to inbox page
        self.wait_redirect(self.INBOX_URL)
    
    def click_nav_trash_button(self):
        elem = self.wait_render(self.nav_trash_button)
        elem.click()
        # Wait for moving to remove page
        self.wait_redirect(self.TRASH_URL)
        
    def click_nav_sent_button(self):
        elem = self.wait_render(self.nav_sent_button)
        elem.click()
        # Wait for moving to remove page
        self.wait_redirect(self.SENT_URL)