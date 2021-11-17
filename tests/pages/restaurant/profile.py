from tests.pages.profile import ProfilePage


class RestaurantProfilePage(ProfilePage):
    """
    Стриница профиля ресторана
    """

    TITLE = '//input[@name="title"]'
    COST = '//input[@name="deliveryCost"]'
    ADDRESS = '//input[@id="js__map-edit-address"]'
    RADIUS = '//input[@name="radius"]'

    ERROR_TITLE = '//p[@id="titleError"]'
    ERROR_COST = '//p[@id="deliveryCostError"]'
    ERROR_RADIUS = '//p[@id="radiusError"]'

    ERROR_CUR_PASSWORD = '//p[@id="repeatPasswordError"]'
    ERROR_NEW_PASSWORD = '//p[@id="passwordError"]'
    ERROR_REPEAT_PASSWORD = '//p[@id="repeatPasswordError"]'

    def __init__(self, driver):
        self.PATH = 'profile/edits'
        super(ProfilePage, self).__init__(driver)

    def set_cost(self, cost):
        elem = self.driver.find_element_by_xpath(self.COST)
        elem.clear()
        elem.send_keys(cost)

    def set_radius(self, radius):
        elem = self.driver.find_element_by_xpath(self.RADIUS)
        elem.clear()
        elem.send_keys(radius)

    def get_title_error(self):
        return self.driver.find_element_by_xpath(self.ERROR_TITLE).text

    def get_cost_error(self):
        return self.driver.find_element_by_xpath(self.ERROR_COST).text

    def get_radius_error(self):
        return self.driver.find_element_by_xpath(self.ERROR_RADIUS).text
