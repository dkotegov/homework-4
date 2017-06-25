# coding=utf-8
from selenium.webdriver.common.by import By

from base import BaseElement


class ShowTopic(BaseElement):
    def topic_title(self):
        self.locator = (By.XPATH, "//h1[contains(@class, 'topic-title')]")
        return self

    def topic_blog(self):
        self.locator = (By.XPATH, "//div[contains(@class, 'topic-info')]")
        return self

    def delete_topic_button(self):
        self.locator = (By.XPATH, "//a[contains(@class, 'actions-delete')")
        return self

    def topic_add_comment_buton(self):
        self.locator = (By.XPATH, "//a[contains(@class, 'comment-add-link')]")
        return self

    def topic_not_publish(self):
        self.locator = (By.XPATH, "//h1[contains(@class, 'topic-title')]/i")
        return self


class TopicContent(BaseElement):
    locator = (By.XPATH, "//div[contains(@class, 'topic-content')]")

    def h4_header(self):
        self.locator = (By.XPATH, "//div[contains(@class, 'topic-content')]/h4")
        return self

    def h5_header(self):
        self.locator = (By.XPATH, "//div[contains(@class, 'topic-content')]/h5")
        return self

    def h6_header(self):
        self.locator = (By.XPATH, "//div[contains(@class, 'topic-content')]/h6")
        return self

    def strong_content(self):
        self.locator = (By.XPATH, "//div[contains(@class, 'topic-content')]/strong")
        return self

    def italic_content(self):
        self.locator = (By.XPATH, "//div[contains(@class, 'topic-content')]/em")
        return self

    def stroke_content(self):
        self.locator = (By.XPATH, "//div[contains(@class, 'topic-content')]/s")
        return self

    def underline_content(self):
        self.locator = (By.XPATH, "//div[contains(@class, 'topic-content')]/u")
        return self

    def blockqoute_content(self):
        self.locator = (By.XPATH, "//div[contains(@class, 'topic-content')]/blockquote")
        return self

    def code_content(self):
        self.locator = (
            By.XPATH, "//div[contains(@class, 'topic-content')]//code[not(contains(@class,'hljs-line-numbers'))]")
        return self

    def embed_video_content(self):
        self.locator = (By.XPATH, "//div[contains(@class, 'topic-content')]/iframe")
        return self

    def image_content(self):
        self.locator = (By.XPATH, "//div[contains(@class, 'topic-content')]/img")
        return self

    def get_image(self):
        return self.image_content().wait_for_visible().get().get_attribute('src')

    def get_h4(self):
        return self.h4_header().wait_for_visible().get().text

    def get_h5(self):
        return self.h5_header().wait_for_visible().get().text

    def get_h6(self):
        return self.h6_header().wait_for_visible().get().text

    def get_strong(self):
        return self.strong_content().wait_for_visible().get().text

    def get_italic(self):
        return self.italic_content().wait_for_visible().get().text

    def get_stroke(self):
        return self.stroke_content().wait_for_visible().get().text

    def get_underline(self):
        return self.underline_content().wait_for_visible().get().text

    def get_blockquote(self):
        return self.blockqoute_content().wait_for_visible().get().text

    def get_code(self):
        return self.code_content().wait_for_visible().get().text


class TopicPoll(BaseElement):
    locator = (By.XPATH, "//div[contains(@class, 'poll')]")

    class PollTitle(BaseElement):
        locator = (By.XPATH, "//div[contains(@class, 'poll')]/p[contains(@class, 'poll-header')]")

    class PollAnswers(BaseElement):
        locator = (By.XPATH, "//div[contains(@class, 'poll')]//ul[contains(@class, 'poll-vote')]")
        answers_locator = "//div[contains(@class, 'poll')]//ul[contains(@class, 'poll-vote')]//label"

        def get_answers(self):
            self.wait_for_visible()
            answers = self.driver.find_elements(by=By.XPATH, value=self.answers_locator)
            return map(lambda el: el.text, answers)

    def get_title(self):
        return self.PollTitle(self.driver)

    def get_answers(self):
        return self.PollAnswers(self.driver)
