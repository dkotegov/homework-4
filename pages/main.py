from pages.default import Page

from utils import wait_for_element_by_selector


class MainPage(Page):
    PATH = ''
    NAVBAR_PROFILE = "a.item__dropdown-profile[href*='/profile']"
    NAVBAR_FAVOURITES = "a.item__dropdown-profile[href*='/favourite']"
    NAVBAR_LOGOUT = 'div.item__dropdown-profile.js-logout-page'
    NAVBAR_DROPDOWN = 'div.dropdown-profile'

    def show_navbar(self):
        wait_for_element_by_selector(self.driver, self.NAVBAR_DROPDOWN)
        self.driver.find_element_by_css_selector(self.NAVBAR_DROPDOWN).click()

    def click_on_navbar(self, selector):
        self.show_navbar()
        wait_for_element_by_selector(self.driver, selector)
        self.driver.find_element_by_css_selector(selector).click()

    def click_on_logout(self):
        self.click_on_navbar(self.NAVBAR_LOGOUT)

    def click_on_profile(self):
        self.click_on_navbar(self.NAVBAR_PROFILE)

    def click_on_favourites(self):
        self.click_on_navbar(self.NAVBAR_FAVOURITES)

    def check_dropdown(self):
        return len(self.driver.find_elements_by_css_selector(self.NAVBAR_DROPDOWN)) == 0
