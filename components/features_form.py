from .base import Component
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class FeaturesFormLocators:

    def __init__(self):
        self.dropdown = '//div[contains(@data-test-id, "{}")]//div[@class="dropdown-1-2-89"]'

        self.compose = '//div[@data-test-id="more-email"]'
        self.create_event = '//div[@data-test-id="more-create_event"]'


class FeaturesForm(Component):

    def __init__(self, driver):
        super(FeaturesForm, self).__init__(driver)

        self.locators = FeaturesFormLocators()

        self.wait = WebDriverWait(self.driver, 15)

    def click_dropdown(self, email):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.dropdown.format(email))))
        element.click()

    def click_compose(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.compose)))
        element.click()

    def click_create_event(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_event)))
        element.click()

    def compose_button_exists(self):
        try:
            WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located((By.XPATH, self.locators.compose)))
            return True
        except TimeoutException:
            return False

    def create_event_button_exists(self):
        try:
            WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located((By.XPATH, self.locators.create_event)))
            return True
        except TimeoutException:
            return False
