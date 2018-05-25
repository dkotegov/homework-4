from tests.Components.FeedPageComponents.FeedLeftBar import FeedLeftBar
from tests.pages.primaryPhotoSection.Page import Page


class FeedPage(Page):
    PATH = ''

    @property
    def left_bar(self):
        return FeedLeftBar(self.driver)
