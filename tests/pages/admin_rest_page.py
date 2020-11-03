from tests.pages.page import Page

from tests.components.add_point_form import AddPointForm
from tests.helpers.database import DatabaseFiller

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class AdminRestaurantsPage(Page):
    PATH = '/admin/restaurants'
    LIST = '//main[@class="restaurants-list-view"]'
    ADD_POINT_BUTTON = '//a[@id="{}_geo-point-href"]'
    REST_ELEMENT = '//div[@id="{}"]'
    MESSAGE_FIELD = '//div[contains(@class, "restaurant-list-view__message")]'

    @property
    def add_point_form(self):
        return AddPointForm(self.driver)

    def wait_visible(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LIST).is_displayed()
        )

    def message(self):
        return self.driver.find_element_by_xpath(self.MESSAGE_FIELD).text

    def add_point(self, rest_id, address, radius):
        rest_element = self.driver.find_element_by_xpath(self.REST_ELEMENT.format(rest_id))
        ActionChains(self.driver).move_to_element(rest_element)
        rest_element.click()

        WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.ADD_POINT_BUTTON.format(rest_id)).is_displayed()
        )

        add_point_button = self.driver.find_element_by_xpath(self.ADD_POINT_BUTTON.format(rest_id))
        add_point_button.click()

        point_form = AddPointForm(self.driver)
        point_form.wait_visible()

        point_form.set_address(address)
        point_form.set_radius(radius)

        point_form.submit()

