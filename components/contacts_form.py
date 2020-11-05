import sys
import time

from selenium.webdriver.common.keys import Keys

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

        self.create_contact_firstname_input = '//input[@name="contacts[0].name.first"]'
        self.create_contact_lastname_input = '//input[@name="contacts[0].name.last"]'

        self.create_contact_nick_input = '//input[@name="contacts[0].nick"]'

        self.create_contact_company_input = '//input[@name="contacts[0].company"]'

        self.create_contact_email_input = '//input[@name="contacts[0].emails[{}]"]'

        self.create_contact_phone_input = '//input[@name="contacts[0].phones[0].phone"]'

        self.create_contact_comment_input = '//textarea[@name="contacts[0].comment"]'

        self.create_contact_job_title_input = '//input[@name="contacts[0].job_title"]'

        self.create_contact_boss_input = '//input[@name="contacts[0].boss"]'

        self.create_contact_address_input = '//textarea[@name="contacts[0].address"]'

        self.create_contact_day_of_birth = '//input[@name="contacts[0].birthday.day"]'
        self.create_contact_month_of_birth = '//input[@name="contacts[0].birthday.month"]'
        self.create_contact_year_of_birth = '//input[@name="contacts[0].birthday.year"]'

        self.create_contact_save_btn = '//button[@data-test-id="submit"]'

        self.contact_fullname = '//h3[@data-test-id="fullname"]'

        self.contact_return_btn = '//button[@data-test-id="addressbook-back"]'

        self.contact_to_group_btn = '//button[@data-test-id="group-picker-button"]'
        self.contact_to_group_group = '//div[@data-test-id="group-{}"]'
        self.contact_to_group_apply_btn = '//button[@data-test-id="group-picker-submit"]'

        self.edit_contact_error = '//small[@data-test-id="edit-contact-error"]'
        self.validation_invalid = '//div[@data-test-id="error-footer-text"]'

        self.add_new_email_button = '//span[@data-test-id="add-new-field"]'

        self.first_contact_button = '//div[@data-test-id="addressbook-user-item"]'

        self.click_edit_button = '//button[@data-test-id="addressbook-edit"]'


class ContactsForm(Component):

    def __init__(self, driver):
        super(ContactsForm, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)

        self.locators = ContactsFormLocators()

    def click_on_contact(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.first_contact_button)))
        element.click()

    def click_edit_contact(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.click_edit_button)))
        element.click()

    def click_create_contact(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_contact_btn)))
        element.click()

    def delete_all(self, element):
        if sys.platform == 'darwin':
            element.send_keys(Keys.COMMAND, 'a')
        else:
            element.send_keys(Keys.CONTROL, 'a')

        element.send_keys(Keys.BACKSPACE)
        return element

    def input_firstname(self, new_text):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_contact_firstname_input)))
        element.clear()
        element = self.delete_all(element)
        element.send_keys(new_text)

    def input_lastname(self, text):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_contact_lastname_input)))
        element.clear()
        element = self.delete_all(element)
        element.send_keys(text)

    def input_nick(self, text):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_contact_nick_input)))
        element.clear()
        element = self.delete_all(element)
        element.send_keys(text)

    def input_company(self, text):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_contact_company_input)))
        element.clear()
        element = self.delete_all(element)
        element.send_keys(text)

    def input_email(self, text, email_num=0):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_contact_email_input.format(email_num))))
        element.clear()
        element = self.delete_all(element)
        element.send_keys(text)

    def input_emails(self, emails):
        for i, email in enumerate(emails):
            element = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self.locators.add_new_email_button)))
            element.click()
            self.input_email(email, i)

    def input_phone(self, text):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_contact_phone_input)))
        element.clear()
        element = self.delete_all(element)
        element.send_keys(text)

    def input_comment(self, text):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_contact_comment_input)))
        element.clear()
        element = self.delete_all(element)
        element.send_keys(text)

    def input_job_title(self, text):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_contact_job_title_input)))
        element.clear()
        element = self.delete_all(element)
        element.send_keys(text)

    def input_boss(self, text):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_contact_boss_input)))
        element.clear()
        element = self.delete_all(element)
        element.send_keys(text)

    def input_address(self, text):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_contact_address_input)))
        element.clear()
        element = self.delete_all(element)
        element.send_keys(text)

    def input_day_of_birth(self, day):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_contact_day_of_birth)))
        element.click()
        element.clear()
        element.send_keys(day)

    def input_month_of_birth(self, month):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_contact_month_of_birth)))
        element.clear()
        element.send_keys(month)

    def input_year_of_birth(self, year):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.create_contact_year_of_birth)))
        element.clear()
        element.send_keys(year)

    def input_date_of_birth(self, date):
        day = date["day"]
        self.input_day_of_birth(day)

        month = date["month"]
        self.input_month_of_birth(month)

        year = date["year"]
        self.input_year_of_birth(year)

    def fill_form(self, **data):
        for key, value in data.items():
            if key == "firstname":
                self.input_firstname(value)
            elif key == "lastname":
                self.input_lastname(value)
            elif key == "nick":
                self.input_nick(value)
            elif key == "company":
                self.input_company(value)
            elif key == "email":
                if len(value) == 1:
                    self.input_email(value)
                else:
                    self.input_emails(value)
            elif key == "phone":
                self.input_phone(value)
            elif key == "comment":
                self.input_comment(value)
            elif key == "job_title":
                self.input_job_title(value)
            elif key == "boss":
                self.input_boss(value)
            elif key == "address":
                self.input_address(value)
            else:
                raise ValueError("Unexpected key: " + key)

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

    def delete_contacts_if_needed(self):
        try:
            select_all = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self.locators.select_all_btn)))
            select_all.click()
        except TimeoutException:
            return

        self.delete_contacts()

    def contacts_exists(self, emails):
        for email in emails:
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, self.locators.contact_block.format(email))))
            except TimeoutException:
                return False
        return True

    def contact_exists_in_source(self, email):
        return email in self.driver.page_source

    def check_edit_error(self):
        try:
            WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.XPATH, self.locators.edit_contact_error)))
        except TimeoutException:
            return False
        return True

    def check_validation_error(self):
        try:
            WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.XPATH, self.locators.validation_invalid)))
        except TimeoutException:
            return False
        return True
