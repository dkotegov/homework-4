from time import sleep

from selenium.webdriver import ActionChains

from tests.elements.discussions.DeleteCommentAlert import DeleteCommentAlert
from tests.elements.discussions.Discussion import Discussion
from tests.elements.discussions.Friends import Friends
from tests.elements.discussions.Grups import Grups
from tests.elements.discussions.Input import Input
from tests.elements.discussions.Participated import Participated
from tests.elements.discussions.SelectedTab import SelectedTab
from tests.elements.discussions.myPosts import MyPosts
from tests.pages.base import BasePage


class DiscussionsPage(BasePage):
    def __init__(self,driver):
        self.url = "http://ok.ru/discussions"
        super(DiscussionsPage,self).__init__(driver)

    def is_opened(self):
        my_posts_button = MyPosts(self.driver)
        element = my_posts_button.button().wait_for_visible().get()
        return element is not None

    def openParticipatedTab(self):
        participatedTab = Participated(self.driver)
        element = participatedTab.button().wait_for_visible().get().click()
        return element

    def openMyPostsTab(self):
        myPostsTab = MyPosts(self.driver)
        element = myPostsTab.button().wait_for_visible().get().click()
        return element

    def openFriendsTab(self):
        friendsTab = Friends(self.driver)
        element = friendsTab.button().wait_for_visible().get().click()
        return element

    def openGrupsTab(self):
        grupsTab = Grups(self.driver)
        element = grupsTab.button().wait_for_visible().get().click()
        return element

    def selectedTab(self):
        selected = SelectedTab(self.driver)
        element = selected.selected_tab().get()
        return element

    @staticmethod
    def setComment(self,text):
        input = Input(self.driver)
        # input.input().wait_for_visible().get().click()
        text_edit = input.div().wait_for_visible().get()
        text_edit.click()
        text_edit.clear()

        text_edit.send_keys(unicode(text,"utf-8"))

        button = input.button_send().wait_for_visible().get()
        button.click()


    @staticmethod
    def getCurrentDiscussionTitle(self):
        discussion = Discussion(self.driver)
        title = discussion.title().wait_for_visible().get()
        return title.text

    @staticmethod
    def getLastCommentInCurrentDiscussion(self):
        discussion = Discussion(self.driver)
        comment = discussion.get_last_comment()
        if comment is None:
            return None
        return comment.get().text

    @staticmethod
    def getLastEditedCommentInCurrentDiscussion(self):
        discussion = Discussion(self.driver)
        comment = discussion.get_last_edited_comment()
        if comment is None:
            return None
        return comment.get().text

    @staticmethod
    def deleteLastCommentInCurrentDiscussion(self):
        discussion = Discussion(self.driver)
        delete = discussion.get_last_comment_delete_button().get()
        action = ActionChains(self.driver)
        action.move_to_element(delete)
        action.click().perform()
        deleteCommentAlert = DeleteCommentAlert(self.driver)
        button_ok = deleteCommentAlert.ok_button().wait_for_visible().get()
        button_ok.click()

    @staticmethod
    def changeLastCommentInCurrentDiscussion(self,text):
        discussion = Discussion(self.driver)
        change = discussion.get_last_comment_change_button().get()
        action = ActionChains(self.driver)
        action.move_to_element(change)
        action.click().perform()

        input = Input(self.driver)
        text_edit = input.div_not_empty().wait_for_visible().get()
        text_edit.click()
        text_edit.clear()
        text_edit.send_keys(unicode(text,"utf-8"))
        button = input.button_edit_send().wait_for_visible().get()
        button.click()
