from pages.default import Page
from utils import wait_for_element_by_selector, wait_for_url


class SignupPage(Page):
    PATH = 'signup/'
    TITLE_OF_PAGE = '.content__title'
    LOGIN_PAGE_LINK = '.have-acc__href'

    def get_title_of_page(self):
        return wait_for_element_by_selector(self.driver, self.TITLE_OF_PAGE).text

    def click_on_login_page_link(self):
        wait_for_element_by_selector(self.driver, self.LOGIN_PAGE_LINK).click()

    def wait_for_url_signup(self):
        wait_for_url(self.driver, self.BASE_URL + self.PATH)
