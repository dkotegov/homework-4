from Base import Page
from Recommend.RecommendComponents import Recommendations


class RecommendationsPage(Page):
    PATH = 'recommend/'

    @property
    def recommendations(self):
        return Recommendations(self.driver)
