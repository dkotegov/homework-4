from .base import Component
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class ContactsFormLocators:

    def __init__(self):
        self.dropdown = '//div[@data-test-id="create-dropdown"]'
        self.create_group = '//div[@data-test-id="new_group"]'

        self.group_name = '//input[@data-test-id="group-name"]'
        self.error = '//p[@data-test-id="group-edit-error"]'
        self.save_button = '//button[@data-test-id="addressbook-notification-popup-submit"]'
        self.cancel_button = '//button[@data-test-id="addressbook-notification-popup-cancel"]'

        self.group_block = '//a[@data-test-id="addressbook-group-id:{}"]'
        self.group = self.group_block + '/div/p'
        self.settings = self.group_block + '/div/div'

        self.group_blocks = '//a[contains(@data-test-id, "addressbook-group-id")]'

        self.delete = '//button[@data-test-id="addressbook-notification-popup-remove"]'
        self.delete_confirm = '//button[@data-test-id="addressbook-notification-popup-submit"]'


class ContactsForm(Component):

    def __init__(self, driver):
        super(ContactsForm, self).__init__(driver)

        self.locators = ContactsFormLocators()

        self.wait = WebDriverWait(self.driver, 10)

    def click_dropdown(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.dropdown)))
        element.click()

    def create_group(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_group)))
        element.click()

    def input_group_name(self, text):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.group_name)))
        element.clear()
        element.send_keys(text)

    def clear_group_name_input(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.group_name)))
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.BACKSPACE)

    def click_save(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.save_button)))
        element.click()

    def check_group_name(self, id, name):
        try:
            self.wait.until(
                EC.text_to_be_present_in_element((By.XPATH, self.locators.group.format(id)), name))
            return True
        except TimeoutException:
            return False

    def check_group(self, id):
        try:
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, self.locators.group_block.format(id))))
            return True
        except NoSuchElementException:
            return False

    def error_exists(self):
        try:
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, self.locators.error)))
            return True
        except NoSuchElementException:
            return False

    def click_settings(self, id):
        element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.settings.format(id))))
        
        ActionChains(self.driver).move_to_element(element).perform()

        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.settings.format(id))))
        element.click()

    def delete(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.delete)))
        element.click()

        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.delete_confirm)))
        element.click()

    def click_cancel(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.cancel_button)))
        element.click()

    def get_group_ids(self):
        ids = []

        elements = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.group_blocks)))
        for element in elements[3:]:
            data_test_id = element.get_attribute('data-test-id')
            id = data_test_id.split(':')[-1]
            ids.append(int(id))

        return ids
