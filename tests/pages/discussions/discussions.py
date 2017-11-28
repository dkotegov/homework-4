from tests.elements.discussions.Friends import Friends
from tests.elements.discussions.Grups import Grups
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
        selected = SelectedTab(self)
        element = selected.selected_tab().get()
        return element