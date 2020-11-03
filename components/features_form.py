from .base import Component
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class FeaturesFormLocators:

    def __init__(self):
        self.dropdown = '//div[contains(@data-test-id, "{}")]//div[@class="dropdown-1-2-89"]'

        self.compose = '//div[@data-test-id="more-email"]'
        self.create_event = '//div[@data-test-id="more-create_event"]'

        self.import_btn = '//div[@data-test-id="import_contacts"]'
        self.import_popup = '//form[@data-test-id="addressbook-import-popup"]'
        self.upload_file_input = '//input[@data-test-id="addressbook-import-input-file"]'
        self.import_group_name_input = '//input[@data-test-id="ab-import-group-input"]'
        self.import_error = '//p[@data-test-id="ab-import-error-text"]'
        self.input_error = '//p[@data-test-id="ab-import-input-error-text"]'

        self.export_btn = '//div[@data-test-id="export_contacts"]'
        self.export_popup = '//form[@data-test-id="addressbook-export-popup"]'
        self.group_radio = '//label[@data-test-id="ab-export-group-radio"]'
        self.group_select = '//div[@data-test-id="ab-export-group-name-select"]'
        self.group_option = '//div[@id="react-select-2-option-{}"]'
        self.outlook_radio = '//label[@data-test-id="ab-export-format-outlook"]'
        self.google_radio = '//label[@data-test-id="ab-export-format-google"]'

        self.submit_btn = '//button[@data-test-id="addressbook-notification-popup-submit"]'
        self.cancel_btn = '//button[@data-test-id="addressbook-notification-popup-cancel"]'


class FeaturesForm(Component):

    def __init__(self, driver):
        super(FeaturesForm, self).__init__(driver)

        self.locators = FeaturesFormLocators()

        self.wait = WebDriverWait(self.driver, 10)

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

    def click_import(self):
        element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.import_btn)))
        element.click()

    def upload_file(self, path):
        element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.upload_file_input))
        )
        element.send_keys(path)

    def input_import_group_name(self, text):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.import_group_name_input)))
        element.clear()
        element.send_keys(text)

    def import_error_exists(self):
        try:
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, self.locators.import_error)))
            return True
        except NoSuchElementException:
            return False

    def input_error_exists(self):
        try:
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, self.locators.input_error)))
            return True
        except NoSuchElementException:
            return False

    def click_export(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.export_btn)))
        element.click()

    def click_group_radio(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.group_radio)))
        element.click()

    def click_outlook_radio(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.outlook_radio)))
        element.click()

    def click_google_radio(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.google_radio)))
        element.click()

    def click_submit(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.submit_btn)))
        element.click()

    def click_cancel(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.cancel_btn)))
        element.click()

    def import_popup_exists(self):
        try:
            WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.XPATH, self.locators.import_popup)))
            return True
        except TimeoutException:
            return False

    def export_popup_exists(self):
        try:
            WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.XPATH, self.locators.export_popup)))
            return True
        except TimeoutException:
            return False

    def click_group_select(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.group_select)))
        element.click()

    def click_group_options(self, ids):
        for id in ids:
            element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self.locators.group_option.format(id))))
            element.click()
