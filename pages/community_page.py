from components.page import Page
from components.community_form import CommunityForm


class CommunityPage(Page):

    def community_form(self):
        return CommunityForm(self.driver)
