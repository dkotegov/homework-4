# coding=utf-8
from base import BasePage
from tests.elements.wiki import WikiButtons
import time


class WikiPage(BasePage):
    def __init__(self, driver, username, reponame, wiki):
        self.url = 'https://github.com/' + username + '/' + str(reponame) + '/wiki/' + wiki
        self.wiki_elements = WikiButtons(driver)
        super(WikiPage, self).__init__(driver)

    def create_wiki(self):
        self.wiki_elements.new_wiki_button().wait_for_clickable().get().click()
        self.wiki_elements.create_page().wait_for_visible()

    def set_title(self, tite):
        input_title = self.wiki_elements.title().wait_for_clickable().get()
        input_title.click()
        input_title.clear()
        input_title.send_keys(tite)

    def set_text(self, text):
        text_area = self.wiki_elements.contains().wait_for_clickable().get()
        text_area.click()
        text_area.clear()
        text_area.send_keys(text)

    def submit_create(self, title):
        self.wiki_elements.save().wait_for_clickable().get().click()

        self.wiki_elements.created_wiki(title).wait_for_clickable()
        return self.wiki_elements.created_wiki(title).is_existed() is False

    def edit_wiki(self, title, text):
        self.wiki_elements.edit_button().wait_for_clickable().get().click()
        self.set_title(title)
        self.set_text(text)
        return self.submit_create(title)

    def delete_wiki(self, title):
        self.wiki_elements.edit_button().wait_for_clickable().get().click()
        self.wiki_elements.delete_button().wait_for_clickable().get().click()
        self.driver.switch_to.alert.accept()
        
        return self.wiki_elements.created_wiki(title).is_existed() is False
