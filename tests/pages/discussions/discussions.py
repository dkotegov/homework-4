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