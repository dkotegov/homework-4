from library.ok import OkPage
from library.ok.components import RepostForm


class FeedPage(OkPage):
    PATH = '/feed'

    @property
    def repost_form(self):
        return RepostForm(self.driver)
