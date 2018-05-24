import urlparse

from pages.page import Page
from components.about_form import AboutForm


class AboutPage(Page):

    PAGE = 'about'

    def open_page_by_url(self, path):
        url = urlparse.urljoin(self.BASE_URL, path)
        url = urlparse.urljoin(url, self.PAGE)
        self.driver.get(url)
        self.driver.maximize_window()

    def about_form(self):
        return AboutForm(self.driver)