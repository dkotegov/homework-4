# -*- coding: utf-8 -*-

from tests.utils import Page, Component

class CreatePage(Page):
    PATH = 'blog/33/topic/create/'
    UNIQUE = '//h2[@class="page-header" and contains(text(), "Создание топика")]'

    @property
    def blog_description_column(self):
        return BlogDescriptionColumn(self.driver)

    @property
    def topic_options(self):
        return TopicOptions(self.driver)


class BlogDescriptionColumn(Component):
    BLOG_DESCRIPTION_PATH = '//p[@id="block_blog_info"]'

    def get_blog_description(self):
        self._wait_for_xpath(self.BLOG_DESCRIPTION_PATH)
        return self.driver.find_element_by_xpath(self.BLOG_DESCRIPTION_PATH).text

class TopicOptions(Component):
    ADD_POLL_PATH = '//input[@name="add_poll"]'
    POLL_OPTIONS_PATH = '//div[@class="poll-create"]'
    ADD_POLL_ANSWER_PATH = '//a[text()="Добавить вариант"]'
    POLL_ANSWER_PATH = '//input[@type="text" and starts-with(@name, "form-") and contains(@name, "answer")]'
    TITLE = '//input[@name="title"]'
    SHORT_TEXT = '//textarea[@name="text_short"]'
    MAIN_TEXT = '//textarea[@id="id_text"]'
    CREATE_BUTTON = '//button[contains(text(),"Создать")]'

    def add_poll(self):
        self._clicker(self.ADD_POLL_PATH)

    def is_poll_visible(self):
        self._wait_for_xpath(self.POLL_OPTIONS_PATH)
        return self.driver.find_element_by_xpath(self.POLL_OPTIONS_PATH).is_displayed()

    def add_poll_answer(self):
        self._clicker(self.ADD_POLL_ANSWER_PATH)

    def count_answers(self):
        answers = self.driver.find_elements_by_xpath(self.POLL_ANSWER_PATH)
        return len(answers)

    def set_title(self, title):
        self.driver.find_element_by_xpath(self.TITLE).send_keys(title)

    def set_short_text(self, short_text):
        self.driver.find_element_by_xpath(self.SHORT_TEXT).send_keys(short_text)

    def set_main_text(self, main_text):
        self.driver.find_element_by_xpath(self.MAIN_TEXT).send_keys(main_text)

    def submit(self):
        self.driver.find_element_by_xpath(self.CREATE_BUTTON).click()
