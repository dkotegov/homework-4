# coding=utf-8
from selenium.webdriver.common.by import By

from base import *


class TopicTitle(BaseElement):
    locator = (By.XPATH, "//h1[contains(@class, 'topic-title')]")


class TopicBlog(BaseElement):
    locator = (By.XPATH, "//div[contains(@class, 'topic-info')]")


class DeleteTopicButton(BaseElement):
    locator = (By.XPATH, "//a[contains(@class, 'actions-delete')")


class TopicAddCommentButton(BaseElement):
    locator = (By.XPATH, "//a[contains(@class, 'comment-add-link')]")


class TopicContent(BaseElement):
    locator = (By.XPATH, "//div[contains(@class, 'topic-content')]")

    class HeaderH4(BaseElement):
        locator = (By.XPATH, "//div[contains(@class, 'topic-content')]/h4")

    class HeaderH5(BaseElement):
        locator = (By.XPATH, "//div[contains(@class, 'topic-content')]/h5")

    class HeaderH6(BaseElement):
        locator = (By.XPATH, "//div[contains(@class, 'topic-content')]/h6")

    class StrongContent(BaseElement):
        locator = (By.XPATH, "//div[contains(@class, 'topic-content')]/strong")

    class ItalicContent(BaseElement):
        locator = (By.XPATH, "//div[contains(@class, 'topic-content')]/em")

    class StrokeContent(BaseElement):
        locator = (By.XPATH, "//div[contains(@class, 'topic-content')]/s")

    class UnderlineContent(BaseElement):
        locator = (By.XPATH, "//div[contains(@class, 'topic-content')]/u")

    class UnorderedListContent(BaseElement):
        locator = (By.XPATH, "//div[contains(@class, 'topic-content')]/ul")

    class OrderedListContent(BaseElement):
        locator = (By.XPATH, "//div[contains(@class, 'topic-content')]/ol")

    class BlockquoteContent(BaseElement):
        locator = (By.XPATH, "//div[contains(@class, 'topic-content')]/blockquote")

    class CodeContent(BaseElement):
        locator = (
            By.XPATH, "//div[contains(@class, 'topic-content')]//code[not(contains(@class,'hljs-line-numbers'))]")

    class LinkContent(BaseElement):
        locator = (
            By.XPATH, "//div[contains(@class, 'topic-content')]/a")

    class EmbedVideoContent(BaseElement):
        locator = (
            By.XPATH, "//div[contains(@class, 'topic-content')]/iframe")

    class ImageContent(BaseElement):
        locator = (
            By.XPATH, "//div[contains(@class, 'topic-content')]/img")

    def get_link(self):
        return self.LinkContent(self.driver).wait_for_visible().get().text

    def get_embed_video(self):
        return self.EmbedVideoContent(self.driver).wait_for_visible().get().get_attribute('src')

    def get_image(self):
        return self.ImageContent(self.driver).wait_for_visible().get().get_attribute('src')

    def get_h4(self):
        return self.HeaderH4(self.driver).wait_for_visible().get().text

    def get_h5(self):
        return self.HeaderH5(self.driver).wait_for_visible().get().text

    def get_h6(self):
        return self.HeaderH6(self.driver).wait_for_visible().get().text

    def get_strong(self):
        return self.StrongContent(self.driver).wait_for_visible().get().text

    def get_italic(self):
        return self.ItalicContent(self.driver).wait_for_visible().get().text

    def get_stroke(self):
        return self.StrokeContent(self.driver).wait_for_visible().get().text

    def get_underline(self):
        return self.UnderlineContent(self.driver).wait_for_visible().get().text

    def get_unordered_list(self):
        return self.UnorderedListContent(self.driver).wait_for_visible().get().text

    def get_ordered_list(self):
        return self.OrderedListContent(self.driver).wait_for_visible().get().text

    def get_blockquote(self):
        return self.BlockquoteContent(self.driver).wait_for_visible().get().text

    def get_code(self):
        return self.CodeContent(self.driver).wait_for_visible().get().text


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
