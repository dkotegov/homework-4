from selenium.webdriver.remote.webelement import WebElement

from components.base_component import Component


class ContactsMainBlock(Component):
    CONSTANTS = {
        'recovery_string': 'Будет доступен для восстановления и уведомления ',
    }

    LOCATORS = {'ADD_PHONE_BUTTON': '[data-test-id="recovery-addPhone-button"]',
                'ADD_EMAIL_BUTTON': '[data-test-id="recovery-addEmail-button"]',
                'DELETE_PHONE_BUTTON': '[data-test-id="recovery-delete-phone-button"]',
                'DELETE_EMAIL_BUTTON': '[data-test-id="recovery-delete-email-button"]',
                'PHONE_ITEM_SPAN': '[data-test-id="recovery-phone-list-item-wrapper"]',
                'PHONE_ITEM_RECOVERY_SPAN': "//span[text()='{recovery_string}']/ancestor::div["
                                            "@data-test-id='recovery-phone-list-item'] ".format(recovery_string=CONSTANTS['recovery_string']),

                'WHEN_ACCESSIBLE_PHONE_SPAN': '[data-test-id="recovery-phone-list-item-status_secondary"]',
                'WHEN_ACCESSIBLE_EMAIL_SPAN': '[data-test-id="recovery-email-list-item-status_secondary"]',
                'EMAIL_BLOCK': '[data-test-id="recovery-emails-list-block"]',
                'EMAIL_NAME': '[data-test-id="recovery-email-list-item-value"]',
                'USER_BLOCK_DROPDOWN': 'PH_authMenu',
                }

    def open_popup_phone(self):
        self.page.wait_for_clickable_by_selector(self.LOCATORS['ADD_PHONE_BUTTON'])
        self.page.driver.find_element_by_css_selector(self.LOCATORS['ADD_PHONE_BUTTON']).click()
        pop_up_phone = self.page.pop_up_phone
        pop_up_phone.wait_for_container()

    def add_phone(self, phone):
        self.open_popup_phone()
        pop_up_phone = self.page.pop_up_phone
        pop_up_phone.set_phone(phone)
        pop_up_phone.add_phone()

    def add_invalid_phone(self, phone):
        self.add_phone(phone)
        pop_up_phone = self.page.pop_up_phone
        pop_up_phone.check_invalid()

    def add_valid_phone(self, phone):
        self.add_phone(phone)
        pop_up_confirm_phone = self.page.pop_up_confirm_phone
        pop_up_confirm_phone.wait_for_container()

    def open_popup_email(self):
        self.page.wait_for_clickable_by_selector(self.LOCATORS['ADD_EMAIL_BUTTON'])
        self.page.driver.find_element_by_css_selector(self.LOCATORS['ADD_EMAIL_BUTTON']).click()
        pop_up_email = self.page.pop_up_email
        pop_up_email.wait_for_container()

    def add_email(self, email):
        self.open_popup_email()
        pop_up_email = self.page.pop_up_email
        pop_up_email.set_email(email)

    def add_invalid_email(self, email):
        self.add_email(email)
        pop_up_email = self.page.pop_up_email
        pop_up_email.add_email()

    def add_valid_email(self, email):
        self.add_email(email)
        pop_up_email = self.page.pop_up_email
        pop_up_email.add_email()
        pop_up_email.success()
        pop_up_email.wait_for_container_close()

    def check_email(self, email):
        self.page.waiting_for_visible_by_selector(self.LOCATORS['EMAIL_BLOCK'])
        emails = self.page.driver.find_elements_by_css_selector(self.LOCATORS['EMAIL_NAME'])
        found = False
        for e in emails:
            if e.find_element_by_tag_name('p').get_attribute("innerText") == email:
                found = True
                break
        assert found == True

    def add_email_check(self, email):
        self.add_valid_email(email)
        self.check_email(email)

    def delete_phone(self):
        self.page.waiting_for_visible_by_selector(self.LOCATORS['PHONE_ITEM_SPAN'])
        phone_help_span = self.page.driver.find_element_by_css_selector(self.LOCATORS['PHONE_ITEM_SPAN'])
        phone_help_text = phone_help_span.find_element_by_tag_name('span').get_attribute("innerText")
        phone_help_span.find_element_by_css_selector(self.LOCATORS['DELETE_PHONE_BUTTON']).click()
        pop_up_delete_phone = self.page.pop_up_delete_phone
        pop_up_delete_phone.wait_for_container()
        pop_up_delete_phone.no_access_submit()
        pop_up_delete_phone.success_submit()
        pop_up_delete_phone.wait_for_container_close()
        self.page.waiting_for_invisible_by_text(phone_help_text)

    def delete_phone_reserved(self):
        self.page.waiting_for_visible_by_xpath(self.LOCATORS['PHONE_ITEM_RECOVERY_SPAN'])
        phone_help_span = self.page.driver.find_element_by_xpath(self.LOCATORS['PHONE_ITEM_RECOVERY_SPAN'])
        phone_help_time = phone_help_span.find_elements_by_tag_name('span')[1].get_attribute("innerText")
        phone_help_span.find_element_by_css_selector(self.LOCATORS['DELETE_PHONE_BUTTON']).click()
        pop_up_delete_phone = self.page.pop_up_delete_phone
        pop_up_delete_phone.wait_for_container()
        pop_up_delete_phone.submit()
        pop_up_delete_phone.success_submit()
        pop_up_delete_phone.wait_for_container_close()
        self.page.waiting_for_invisible_by_text(phone_help_time)

    def delete_email(self):
        self.page.waiting_for_visible_by_selector(self.LOCATORS['WHEN_ACCESSIBLE_EMAIL_SPAN'])
        email_help_span = self.page.driver.find_element_by_css_selector(self.LOCATORS['WHEN_ACCESSIBLE_EMAIL_SPAN'])
        email_help_time = email_help_span.find_elements_by_tag_name('span')[1].get_attribute("innerText")
        self.page.wait_for_clickable_by_selector(self.LOCATORS['DELETE_EMAIL_BUTTON'])
        self.page.driver.find_element_by_css_selector(self.LOCATORS['DELETE_EMAIL_BUTTON']).click()
        pop_up_delete_email = self.page.pop_up_delete_email
        pop_up_delete_email.wait_for_container()
        pop_up_delete_email.submit()
        pop_up_delete_email.success_submit()
        pop_up_delete_email.wait_for_container_close()
        self.page.waiting_for_invisible_by_text(email_help_time)
