# coding=utf-8
import re

from selenium.webdriver.common.alert import Alert

from base import *
from tests.elements.create_topic import *


class CreateTopicPage(BasePage):
    url = 'http://ftest.tech-mail.ru/blog/topic/create/'

    def choose_blog(self, blog_title):
        BlogSelect(self.driver).wait_for_visible().get().click()
        BlogTitle(self.driver, blog_title).wait_for_presence().get().click()
        return self

    def set_title(self, topic_title):
        TopicTitleInput(self.driver).wait_for_visible().get().send_keys(topic_title)
        return self

    def add_text(self, text, modifier=None):
        topic_text_area = TopicTextArea(self.driver).wait_for_visible().get()

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
        CreateButton(self.driver).wait_for_visible().get().click()
        TopicCreatedNotice(self.driver).wait_for_presence()

        url = self.driver.current_url
        match = re.search('topic/view/(\d+)/', url)
        return match.group(1)

    def click_create_button(self):
        CreateButton(self.driver).wait_for_visible().get().click()
        return self

    def check_error_notice(self):
        TopicErrorNotice(self.driver).wait_for_presence()

    def add_h4(self):
        H4Font(self.driver).wait_for_visible().get().click()

    def add_h5(self):
        H5Font(self.driver).wait_for_visible().get().click()

    def add_h6(self):
        H6Font(self.driver).wait_for_visible().get().click()

    def add_bold(self):
        BoldFont(self.driver).wait_for_visible().get().click()

    def add_italic(self):
        ItalicFont(self.driver).wait_for_visible().get().click()

    def add_underline(self):
        UnderlineFont(self.driver).wait_for_visible().get().click()

    def add_stroke(self):
        StrokeFont(self.driver).wait_for_visible().get().click()

    def add_quote(self):
        QuoteFont(self.driver).wait_for_visible().get().click()

    def add_code(self):
        EditorCodeFont(self.driver).wait_for_visible().get().click()
        InsertCodeButton(self.driver).wait_for_visible().get().click()

    def add_ul(self):
        UlList(self.driver).wait_for_visible().get().click()

    def add_ol(self):
        OlList(self.driver).wait_for_visible().get().click()

    def add_link(self):
        LinkButton(self.driver).wait_for_visible().get().click()
        LinkInput(self.driver).wait_for_visible().get().send_keys('#')
        LinkConfirmButton(self.driver).wait_for_visible().get().click()

    def add_picture(self, address):
        PictureButton(self.driver).wait_for_visible().get().click()
        PicureFromInternet(self.driver).wait_for_visible().get().click()
        PictureInputAddress(self.driver).wait_for_visible().get().clear()
        PictureInputAddress(self.driver).wait_for_visible().get().send_keys(address)
        PictureCreateButton(self.driver).wait_for_visible().get().click()
        return self

    def add_video(self, address):
        VideoButton(self.driver).wait_for_visible().get().click()
        alert = Alert.wait_for_alert(self.driver)
        alert.send_keys(address)
        alert.accept()
        return self

    def disable_comments(self):
        DisableCommentButton(self.driver).wait_for_visible().get().click()
        return self

    def get_value(self):
        return TopicTextArea(self.driver).wait_for_visible().get_value()

    def add_poll(self, header, first_answer, second_answer):
        AddPollButton(self.driver).wait_for_visible().get().click()
        create_poll_block = CreatePollBlock(self.driver).wait_for_visible()
        create_poll_block.get_header_input().send_keys(header)
        create_poll_block.get_answer_input(0).send_keys(first_answer)
        create_poll_block.get_answer_input(1).send_keys(second_answer)
        return self
