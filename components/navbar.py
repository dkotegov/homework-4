from components.default import Component

from utils import wait_for_element_by_selector
from utils import wait_click_for_element_by_selector


class NavBar(Component):
    PROFILE = "a.item__dropdown-profile[href*='/profile']"
    FAVOURITES = "a.item__dropdown-profile[href*='/favourite']"
    LOGOUT = 'div.item__dropdown-profile.js-logout-page'
    DROPDOWN = 'div.dropdown-profile'
    SERIES = 'header .header-form li a[href*=\"/series\"]'
    MOVIES = 'header .header-form li a[href*=\"/movies\"]'
    MAIN = 'header .header-form li a[href*=\"/\"]'
    LOGO = 'header .header a.header_logo'

    def _show_dropdown(self):
        wait_for_element_by_selector(self.driver, self.DROPDOWN)
        self.driver.find_element_by_css_selector(self.DROPDOWN).click()

    def _click_on_dropdown(self, selector):
        self._show_dropdown()
        wait_click_for_element_by_selector(self.driver, selector)

    def click_on_logout(self):
        self._click_on_dropdown(self.LOGOUT)

    def click_on_profile(self):
        self._click_on_dropdown(self.PROFILE)

    def click_on_favourites(self):
        self._click_on_dropdown(self.FAVOURITES)

    def click_on_movies(self):
        wait_click_for_element_by_selector(self.driver, self.MOVIES)

    def click_on_series(self):
        wait_click_for_element_by_selector(self.driver, self.SERIES)

    def click_on_main(self):
        wait_click_for_element_by_selector(self.driver, self.MAIN)

    def click_on_logo(self):
        wait_click_for_element_by_selector(self.driver, self.LOGO)

    def check_dropdown(self):
        return len(self.driver.find_elements_by_css_selector(self.DROPDOWN)) == 0
