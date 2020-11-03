from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.common import Common


class NotificationPage:
    bell_button_xpath = '//*[@id="portal-menu__toolbar"]/div[1]/div/div[2]/div/span/span[2]/span[6]/span[1]/span[3]/span/span/span'
    notification_list_xpath = '//*[@id="portal-menu__toolbar"]/div[1]/div/div[2]/div/span/span[2]/span[6]/span[2]'

    def __init__(self, browser):
        self.browser = browser
        self.common = Common(browser)

    def check_notification(self, text):
        self.common.open_page(self.common.main_page)
        WebDriverWait(self.browser, self.common.wait_timeout).until(
            EC.presence_of_element_located((By.XPATH, self.bell_button_xpath)))

        xpath = '//*[contains(text(), "{}")]'.format(text)

        self.browser.find_element_by_xpath(self.bell_button_xpath).click()
        self.browser.find_element_by_xpath(self.notification_list_xpath)
        self.browser.find_element_by_xpath(xpath)
