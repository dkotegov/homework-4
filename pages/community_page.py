import urlparse

from pages.page import Page
from components.community_form import CommunityForm


class CommunityPage(Page):

    PAGE = "community"

    def open_page_by_url(self, path):
        url = urlparse.urljoin(self.BASE_URL, self.PAGE)
        url = urlparse.urljoin(url, path)
        self.driver.get(url)
        self.driver.maximize_window()

    def community_form(self):
        return CommunityForm(self.driver)
