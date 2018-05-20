from selenium.common.exceptions import TimeoutException

from components.base_component import BaseComponent
from constants import game


class MainUpToolbar(BaseComponent):
    NOTIFICATION_BUTTON = "//div[@class='toolbar_nav_i_tx-w usel-off']"
    NOTIFICATION_BUTTON__GAMES = "//a[@data-category='Games']"
    IMAGE = "//a[@data-l='t,app_ava']"
    NOTIFICATION_HOVER = "//div[contains(@data-l,'notifMarker')]"
    REPORT_NOTIFICATION_BUTTON = "//i[@data-l='t,spam']"
    CONFIRM_REPORT_NOTIFICATION = "//span[@tsid='ntf_unsubscribe']"
    LOGO_IMG = "//div[@class='toolbar_logo_img']"

    def get_notification(self):
        return self.get_elements_by_path(self.NOTIFICATION_BUTTON)[2]

    def get_notification_games(self):
        return self.get_clickable_element(self.NOTIFICATION_BUTTON__GAMES)

    def get_notification_hover(self):
        return self.get_elements_by_path(self.NOTIFICATION_HOVER)[0]

    def get_report_notification_button(self):
        return self.get_clickable_element(self.REPORT_NOTIFICATION_BUTTON)

    def get_confirm_report_notification(self):
        return self.get_clickable_element(self.CONFIRM_REPORT_NOTIFICATION)

    def get_logo_img(self):
        return self.get_element_by_path(self.LOGO_IMG)
