from time import sleep

from selenium.webdriver import ActionChains

from tests.elements.discussions.delete_comment_alert import DeleteCommentAlert
from tests.elements.discussions.discussion import Discussion
from tests.elements.discussions.friends import Friends
from tests.elements.discussions.groups import Groups
from tests.elements.discussions.input import Input
from tests.elements.discussions.participated import Participated
from tests.elements.discussions.selected_tab import SelectedTab
from tests.elements.discussions.my_posts import MyPosts
from tests.pages.base import BasePage


class DiscussionsPage(BasePage):
    def __init__(self, driver):
        self.url = "http://ok.ru/discussions"
        super(DiscussionsPage, self).__init__(driver)

    def is_opened(self):
        my_posts_button = MyPosts(self.driver)
        element = my_posts_button.button().wait_for_visible().get()
        return element is not None

    def open_participated_tab(self):
        participated_tab = Participated(self.driver)
        element = participated_tab.button().wait_for_visible().get().click()
        return element

    def open_my_posts_tab(self):
        my_posts_tab = MyPosts(self.driver)
        element = my_posts_tab.button().wait_for_visible().get().click()
        return element

    def open_friends_tab(self):
        friends_tab = Friends(self.driver)
        element = friends_tab.button().wait_for_visible().get().click()
        return element

    def open_groups_tab(self):
        groups_tab = Groups(self.driver)
        element = groups_tab.button().wait_for_visible().get().click()
        return element

    def selected_tab(self):
        selected = SelectedTab(self.driver)
        element = selected.selected_tab().get()
        return element

    @staticmethod
    def set_comment(self, text):
        input_element = Input(self.driver)
        # input_element.input_element().wait_for_visible().get().click()
        text_edit = input_element.div().wait_for_visible().get()
        text_edit.click()
        text_edit.clear()

        text_edit.send_keys(unicode(text, "utf-8"))

        button = input_element.button_send().wait_for_visible().get()
        button.click()

    @staticmethod
    def get_current_discussion_title(self):
        discussion = Discussion(self.driver)
        title = discussion.title().wait_for_visible().get()
        return title.text

    @staticmethod
    def get_last_comment_in_current_discussion(self):
        discussion = Discussion(self.driver)
        comment = discussion.get_last_comment()
        if comment is None:
            return None
        return comment.get().text

    @staticmethod
    def get_last_edited_comment_in_current_discussion(self):
        discussion = Discussion(self.driver)
        comment = discussion.get_last_edited_comment()
        if comment is None:
            return None
        return comment.get().text

    @staticmethod
    def delete_last_comment_in_current_discussion(self):
        discussion = Discussion(self.driver)
        delete = discussion.get_last_comment_delete_button().get()
        action = ActionChains(self.driver)
        action.move_to_element(delete)
        action.click().perform()
        delete_comment_alert = DeleteCommentAlert(self.driver)
        button_ok = delete_comment_alert.ok_button().wait_for_visible().get()
        button_ok.click()

    @staticmethod
    def change_last_comment_in_current_discussion(self, text):
        discussion = Discussion(self.driver)
        change = discussion.get_last_comment_change_button().get()
        action = ActionChains(self.driver)
        action.move_to_element(change)
        action.click().perform()

        input_element = Input(self.driver)
        text_edit = input_element.div_not_empty().wait_for_visible().get()
        text_edit.click()
        text_edit.clear()
        text_edit.send_keys(unicode(text, "utf-8"))
        button = input_element.button_edit_send().wait_for_visible().get()
        button.click()
