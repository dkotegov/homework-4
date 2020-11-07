from selenium.webdriver.support.wait import WebDriverWait

from tests.components.component import Component


class RestaurantBanner(Component):
    def wait_visible(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: restaurant_rate(d).is_displayed()
        )

    def mark(self):
        return len(
            restaurant_rate(self.driver)
                .get_attribute('innerText')
        )


def restaurant_rate(driver):
    return driver.find_element_by_css_selector(
        '.restaurantBanner__rate'
    )
