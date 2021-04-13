from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent


class NotificationLocators:
    def __init__(self):
        self.root = '//div[@class="menu-list-block__item menu-list-block__item_note_head"]'

        self.empty_list = '//div[@id="notes-list"]'
        self.recommendation = '//div[@class="menu-list-block__item menu-list-block__item_note"]'
        # self.recommendation = '//a[@href="/recommendations"]'


class Notification(BaseComponent):
    def __init__(self, driver):
        super(Notification, self).__init__(driver)
        self.locators = NotificationLocators()

    def wait_for_open(self):
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.root)))

    def get_text_empty_notif(self):
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.empty_list)))
        return self.get_field(self.locators.empty_list)

    def get_text_recommendations(self):
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.recommendation)))
        return self.get_field(self.locators.recommendation)

    def click_notif_recommendation(self):
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.recommendation)))
        self.click_locator(self.locators.recommendation)
