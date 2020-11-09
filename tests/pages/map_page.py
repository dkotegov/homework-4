from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.page import Page


class MapPage(Page):
    PATH = 'map'

    def wait_visible(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_css_selector(
                'ymaps'
            ).is_displayed()
        )

    def click_to_center_pointer(self):
        cont_size = container(self.driver).size
        height = cont_size['height']
        width = cont_size['width']

        ActionChains(self.driver)\
            .move_by_offset(width, height)\
            .click()\
            .perform()

    def wait_rest_button_visible(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: rest_button(d).is_displayed()
        )

    def click_rest_button(self):
        rest_button(self.driver).click()


def rest_button(driver):
    return driver.find_element_by_css_selector(
        'button[class^="neon-button"]',
    )

def container(driver):
    return driver.find_element_by_css_selector(
        '#view'
    )