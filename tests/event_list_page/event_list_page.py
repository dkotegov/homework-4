# -*- coding: utf-8 -*-

from tests.utils import Page, Component, Header


class EventListPage(Page):
    PATH = 'blog/view/33/'
    UNIQUE = '//h2[@class="page-header" and text()="Мероприятия"]'
    HEADER_TEXT = u'Мероприятия'

    @property
    def header(self):
        return Header(self.driver)

    @property
    def event(self):
        return Event(self.driver)

    @property
    def blog_menu(self):
        return BlogMenu(self.driver)


class BlogMenu(Component):
    CREATE_BUTTON_PATH = '//div[@id="blog-mini-header"]/a'

    def create(self):
        self._wait_for_xpath(self.CREATE_BUTTON_PATH)
        self.driver.find_element_by_xpath(self.CREATE_BUTTON_PATH).click()

    @staticmethod
    def get_create_page_url():
        return 'https://park.mail.ru/blog/33/topic/create/'


class Event(Component):
    HEADER_PATH = '//h1[@class="topic-title"]/a'
    SUBHEADER_PATH = '//a[@class="topic-blog"]'
    SUBMIT_BUTTON_PATH = '//button[text()="Регистрация закрыта"]'
    READ_FURTHER_PATH = '//a[@title="Читать дальше"]'

    def open_event(self):
        self._clicker(self.HEADER_PATH)

    def open_blog(self):
        self._clicker(self.SUBHEADER_PATH)

    def participate(self):
        self._clicker(self.SUBMIT_BUTTON_PATH)

    def is_button_clickable(self):
        return self._wait_for_xpath(self.SUBMIT_BUTTON_PATH).is_enabled()

    def read_further(self):
        self._clicker(self.READ_FURTHER_PATH)

    def get_button_text(self):
        return self._wait_for_xpath(self.SUBMIT_BUTTON_PATH).text

    def get_button_color(self):
        return self._wait_for_xpath(self.SUBMIT_BUTTON_PATH).value_of_css_property('background-color')
