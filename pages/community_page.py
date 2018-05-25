import urlparse

from pages.page import Page
from components.community_form import CommunityForm


class CommunityPage(Page):

    def __init__(self, driver, url):
        super(CommunityPage, self).__init__(driver)
        self.community_form = CommunityForm(self.driver)
        self.PAGE = "community/" + url

    def community_form(self):
        return CommunityForm(self.driver)
