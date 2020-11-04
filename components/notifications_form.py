from base_classes.component import Component
from selenium.webdriver.remote.webdriver import WebDriver

header_button_classname = 'header-notifications-controls__button--selected'


class LocalStorage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get(self, key):
        return self.driver.execute_script("window.localStorage.getItem(arguments[0]);", key)


class Notifications(Component):
    CONTAINER = '//div[@class = "header-notifications"]'

    READ_BUTTON = '//div[contains(@class, "js-readNotifications")]'
    DELETE_BUTTON = '//div[contains(@class, "js-deleteNotifications")]'

    SOUND_BUTTON = '//div[contains(@class, "js-toggleSound")]'
    NOTIFICATIONS_BUTTON = '//div[contains(@class, "js-toggleNotifications")]'
    # SOUND_BUTTON_SELECTED = '//div[contains(@class, "js-toggleSound ' + header_button_classname + '")'
    # NOTIFICATIONS_BUTTON_SELECTED = '//div[contains(@class, "js-toggleNotifications ' + header_button_classname + '")'

    def is_notifications_enabled(self):
        return LocalStorage(self.driver).get('enableNotifications') == 'true'

    def is_sound_enabled(self):
        return LocalStorage(self.driver).get('enableNotificationsSound') == 'true'

    def toggle_notifications(self):
        button = self.driver.find_element_by_xpath(self.NOTIFICATIONS_BUTTON)
        print(button.get_attribute('class'))
        button.click()

    def toggle_sound(self):
        self.driver.find_element_by_xpath(self.SOUND_BUTTON).click()

    def read_notifications(self):
        self.driver.find_element_by_xpath(self.READ_BUTTON).click()

    def delete_notifications(self):
        self.driver.find_element_by_xpath(self.DELETE_BUTTON).click()
