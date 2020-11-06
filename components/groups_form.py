from .base import Component
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class GroupsFormLocators:

    def __init__(self):
        self.dropdown = '//div[@data-test-id="create-dropdown"]'
        self.create_group_btn = '//div[@data-test-id="new_group"]'
        self.create_group_btn2 = '//div[@data-test-id="create-new-group"]'

        self.create_group_popup = '//div[@data-test-id="popup-wrapper"]'
        self.create_group_input = '//input[@data-test-id="group-name"]'
        self.create_group_error = '//p[@data-test-id="group-edit-error"]'
        self.create_group_save_btn = '//button[@data-test-id="addressbook-notification-popup-submit"]'
        self.create_group_cancel_btn = '//button[@data-test-id="addressbook-notification-popup-cancel"]'
        self.create_group_cross_btn = '//div[@data-test-id="cross"]'

        self.group_blocks = '//a[contains(@data-test-id, "addressbook-group-id")]'
        self.group_block = '//a[@data-test-id="addressbook-group-id:{}"]'
        self.group_block_name = self.group_block + '/div/p'
        self.group_block_settings = self.group_block + '/div/div'

        self.delete_group_btn = '//button[@data-test-id="addressbook-notification-popup-remove"]'
        self.delete_group_confirm_btn = '//button[@data-test-id="addressbook-notification-popup-submit"]'


class GroupsForm(Component):

    def __init__(self, driver):
        super(GroupsForm, self).__init__(driver)

        self.locators = GroupsFormLocators()

        self.wait = WebDriverWait(self.driver, 5)

    def click_dropdown(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.dropdown)))
        element.click()

    def click_create_group(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_group_btn)))
        element.click()

    def click_create_group_from_contact_page(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_group_btn2)))
        element.click()

    def input_group_name(self, text):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_group_input)))
        element.clear()
        element.send_keys(text)

    def clear_group_name(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_group_input)))
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.BACKSPACE)

    def click_save(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_group_save_btn)))
        element.click()

    def click_cancel(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_group_cancel_btn)))
        element.click()

    def click_cross(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_group_cross_btn)))
        element.click()

    def group_name_exists(self, id, name):
        try:
            self.wait.until(
                EC.text_to_be_present_in_element((By.XPATH, self.locators.group_block_name.format(id)), name))
            return True
        except TimeoutException:
            return False

    def group_exists(self, id):
        try:
            WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.XPATH, self.locators.group_block.format(id))))
            return True
        except TimeoutException:
            return False

    def error_exists(self):
        try:
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, self.locators.create_group_error)))
            return True
        except NoSuchElementException:
            return False

    def click_settings(self, id):
        self.wait.until(
            EC.visibility_of_all_elements_located((By.XPATH, self.locators.group_block.format(id))))

        element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.group_block_settings.format(id))))
        ActionChains(self.driver).move_to_element(element).perform()

        try:
            element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self.locators.group_block_settings.format(id))))
            element.click()
            return True
        except TimeoutException:
            return False

    def delete_group(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.delete_group_btn)))
        element.click()

        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.delete_group_confirm_btn)))
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

    def click_group_block(self, id):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.group_block.format(id))))
        element.click()

    def group_popup_exists(self):
        try:
            WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.XPATH, self.locators.create_group_popup)))
            return True
        except TimeoutException:
            return False
