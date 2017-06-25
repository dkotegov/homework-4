# coding=utf-8
import re

from base import BasePage
from tests.elements.create_topic import CreateTopicPage as CreateTopicPageElements, CreatePollBlock


class CreateTopicPage(BasePage):
    url = 'http://ftest.tech-mail.ru/blog/topic/create/'

    def __init__(self, driver):
        self.driver = driver
        self.create_topic_elements = CreateTopicPageElements(driver)
        super(BasePage, self).__init__()


    def choose_blog(self, blog_title):
        self.create_topic_elements.block_select().wait_for_visible().get().click()
        self.create_topic_elements.block_title(blog_title).wait_for_presence().get().click()
        return self

    def set_title(self, topic_title):
        self.create_topic_elements.topic_title_input().wait_for_visible().get().send_keys(topic_title)
        return self

    def add_text(self, text, modifier=None):
        topic_text_area = self.create_topic_elements.topic_text_area().wait_for_visible().get()

        old_value = self.get_value()

        topic_text_area.clear()

        if modifier is not None:
            method_name = 'add_' + str(modifier)
            method = getattr(self, method_name)
            method()

        topic_text_area.send_keys(text)

        add_value = self.get_value()
        new_value = (old_value + '\n' + add_value) if (old_value != '') else add_value

        topic_text_area.clear()
        topic_text_area.send_keys(new_value)

        return self

    def create(self):
        self.create_topic_elements.create_button().wait_for_visible().get().click()
        self.create_topic_elements.topic_created_notice().wait_for_presence()

        url = self.driver.current_url
        match = re.search('topic/view/(\d+)/', url)
        return match.group(1)

    def click_create_button(self):
        self.create_topic_elements.create_button().wait_for_visible().get().click()
        return self

    def check_error_notice(self):
        self.create_topic_elements.topic_error_notice().wait_for_presence()

    def add_h4(self):
        self.create_topic_elements.h4_font_button().wait_for_visible().get().click()

    def add_h5(self):
        self.create_topic_elements.h5_font_button().wait_for_visible().get().click()

    def add_h6(self):
        self.create_topic_elements.h6_font_button().wait_for_visible().get().click()

    def add_bold(self):
        self.create_topic_elements.bold_font_button().wait_for_visible().get().click()

    def add_italic(self):
        self.create_topic_elements.italic_font_button().wait_for_visible().get().click()

    def add_underline(self):
        self.create_topic_elements.underline_font_button().wait_for_visible().get().click()

    def add_stroke(self):
        self.create_topic_elements.stroke_font_button().wait_for_visible().get().click()

    def add_quote(self):
        self.create_topic_elements.quote_font_button().wait_for_visible().get().click()

    def add_code(self):
        self.create_topic_elements.editor_code_font_button().wait_for_visible().get().click()
        self.create_topic_elements.insert_code_button().wait_for_visible().get().click()

    def add_picture(self, address):
        self.create_topic_elements.picture_button().wait_for_visible().get().click()
        self.create_topic_elements.picture_from_internet_button().wait_for_visible().get().click()
        self.create_topic_elements.picture_address_input().wait_for_visible().get().clear()
        self.create_topic_elements.picture_address_input().wait_for_visible().get().send_keys(address)
        self.create_topic_elements.picture_create_button().wait_for_visible().get().click()
        return self

    def disable_comments(self):
        self.create_topic_elements.disable_comment_button().wait_for_visible().get().click()
        return self

    def get_value(self):
        return self.create_topic_elements.topic_text_area().wait_for_visible().get_value()

    def add_poll(self, header, first_answer, second_answer):
        self.create_topic_elements.add_poll_button().wait_for_visible().get().click()
        create_poll_block = CreatePollBlock(self.driver).wait_for_visible()
        create_poll_block.get_header_input().send_keys(header)
        create_poll_block.get_answer_input(0).send_keys(first_answer)
        create_poll_block.get_answer_input(1).send_keys(second_answer)
        return self

    def disable_publish(self):
        self.create_topic_elements.disable_publish_button().wait_for_visible().get().click()
        return self
