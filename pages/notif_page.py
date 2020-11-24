from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.common import Common


class NotificationPage:
    BELL_BUTTON_XPATH = '//span[contains(@class,"pm-uh-notification-i")]'
    NOTIFICATION_LIST_XPATH = '//div[contains(@class,"vue-dropdown-notifications")]'

    def __init__(self, browser):
        self.browser = browser
        self.common = Common(browser)

    def check_notification(self, text):
        self.common.open_page(self.common.MAIN_PAGE)
        WebDriverWait(self.browser, self.common.WAIT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, self.BELL_BUTTON_XPATH)))

        xpath = '//div[contains(text(), "{}")]'.format(text)

        self.browser.find_element_by_xpath(self.BELL_BUTTON_XPATH).click()
        WebDriverWait(self.browser, self.common.WAIT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, self.NOTIFICATION_LIST_XPATH)))

        self.browser.find_element_by_xpath(xpath)
