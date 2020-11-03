from .base import Component
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, WebDriverException


class ContactsFormLocators:

    def __init__(self):
        self.create_contact_btn = '//button[@data-test-id="add-contact"]'
        self.contact_block = '//div[contains(@data-test-id, "{}")]/a'
        self.contact_block_avatar = self.contact_block + '/div[@data-test-id="addressbook-item-avatar"]'

        self.select_all_btn = '//button[@data-test-id="addressbook-select-all-users"]'
        self.delete_contacts_btn = '//button[@data-test-id="addressbook-delete-users"]'
        self.delete_contacts_confirm_btn = '//button[@data-test-id="addressbook-notification-popup-submit"]'

        self.create_contact_email_input = '//input[@name="contacts[0].emails[0]"]'
        self.create_contact_firstname_input = '//input[@name="contacts[0].name.first"]'
        self.create_contact_save_btn = '//button[@data-test-id="submit"]'

        self.contact_fullname = '//h3[@data-test-id="fullname"]'

        self.contact_return_btn = '//button[@data-test-id="addressbook-back"]'

        self.contact_to_group_btn = '//button[@data-test-id="group-picker-button"]'
        self.contact_to_group_group = '//div[@data-test-id="group-{}"]'
        self.contact_to_group_apply_btn = '//button[@data-test-id="group-picker-submit"]'


class ContactsForm(Component):

    def __init__(self, driver):
        super(ContactsForm, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 15)

        self.locators = ContactsFormLocators()

    def click_create_contact(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_contact_btn)))
        element.click()

    def input_email(self, text):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_contact_email_input)))
        element.clear()
        element.send_keys(text)

    def input_firstname(self, text):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_contact_firstname_input)))
        element.clear()
        element.send_keys(text)

    def click_save(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_contact_save_btn)))
        element.click()

    def click_to_group(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.contact_to_group_btn)))
        element.click()

    def select_groups(self, ids):
        for id in ids:
            element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self.locators.contact_to_group_group.format(id))))
            element.click()

    def click_apply(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.contact_to_group_apply_btn)))
        element.click()

    def wait_for_applying(self):
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.contact_fullname)))

    def click_return_if_exists(self):
        try:
            element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self.locators.contact_return_btn)))
            element.click()
        except (TimeoutException, StaleElementReferenceException):
            pass

    def click_contact_block(self, email):
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.contact_block.format(email))))

        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.contact_block.format(email))))
        element.click()

    def click_select_all(self):
        try:
            element = WebDriverWait(self.driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, self.locators.select_all_btn)))
            element.click()
            return True
        except TimeoutException:
            return False

    def select_contacts(self, emails):
        for email in emails:
            element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self.locators.contact_block_avatar.format(email))))
            element.click()

    def delete_contacts(self):
        delete = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.delete_contacts_btn)))
        delete.click()

        delete_confirm = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.delete_contacts_confirm_btn)))
        delete_confirm.click()

    def contacts_exists(self, emails):
        for email in emails:
            try:
                WebDriverWait(self.driver, 1).until(
                    EC.presence_of_element_located((By.XPATH, self.locators.contact_block.format(email))))
            except TimeoutException:
                return False
        return True
