# coding=utf-8
from selenium.webdriver.common.by import By

from base import BaseElement


class WikiButtons(BaseElement):

    def new_wiki_button(self):
        self.locator = (By.XPATH, "//a[contains(text(), 'Create the first page')]")
        return self

    def create_page(self):
        self.locator = (By.XPATH, "//h1[contains(text(), 'Create new page')]")
        return self

    def title(self):
        self.locator = (By.XPATH, "//input[@name='wiki[name]']")
        return self

    def contains(self):
        self.locator = (By.XPATH, "//textarea[@name='wiki[body]']")
        return self

    def save(self):
        self.locator = (By.XPATH, "//button[@id='gollum-editor-submit']")
        return self

    def created_wiki(self, wiki):
        self.locator = (By.XPATH, "//a[contains(text(), '{0}')]".format(wiki))
        return self

    def edit_button(self):
        self.locator = (By.XPATH, "//a[contains(text(), 'Edit')]")
        return self

    def delete_button(self):
        self.locator = (By.XPATH, "//button[text()[contains(.,'Delete Page')]]")
        return self
