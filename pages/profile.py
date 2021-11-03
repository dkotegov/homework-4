import constants
from pages.default import Page
from utils import wait_for_element_by_selector, wait_for_url


class ProfilePage(Page):
    PATH = 'profile/'
    TITLE = '.title-wrapper__title'
    SUBSCRIPTION_BTN = '.subscription__button'

    def get_title_of_page(self):
        return wait_for_element_by_selector(self.driver, self.TITLE).text

    def click_on_subscription_btn(self):
        wait_for_element_by_selector(self.driver, self.SUBSCRIPTION_BTN).click()

    def is_umoney_url(self):
        try:
            wait_for_url(self.driver, constants.UMONEY_URL)
            return True
        except:
            return False
