from selenium.common.exceptions import TimeoutException

from components.base_component import BaseComponent


class MainUpToolbar(BaseComponent):
    # POPUP_NOTIFICATION_BUTTON = "//a[contains(@data-l, 'growl_link')]"
    NOTIFICATION_BUTTON = "//div[@class='toolbar_nav_i_tx-w usel-off']"
    NOTIFICATION_BUTTON__GAMES = "//a[@data-category='Games']"
    IMAGE = "//a[@data-l='t,app_ava']"

    def get_notification(self):
        return self.driver.find_elements_by_xpath(self.NOTIFICATION_BUTTON)[2]

    def get_notification_games(self):
        return self.get_clickable_element(self.NOTIFICATION_BUTTON__GAMES)

    def get_image_element(self):
        try:
            el = self.get_element_by_path(self.IMAGE)
        except TimeoutException:
            return False
        return el
