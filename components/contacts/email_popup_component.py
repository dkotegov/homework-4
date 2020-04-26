from components.base_component import Component


class ContactsEmailPopup(Component):
    CONSTANTS = {
        'invalid_email': 'Неправильная почта. Укажите другую.',
    }

    LOCATORS = {'ROOT': '[data-test-id="recovery-inner-popup"]',
                'EMAIL_INPUT': '[data-test-id="recovery-addEmail-emailField-input"]',
                'ADD_BUTTON': '[data-test-id="recovery-addEmail-submit"]',
                'SUCCESS_BUTTON': '[data-test-id="recovery-success-close"]',
                'CANCEL_BUTTON': '[data-test-id="recovery-addEmail-cancel"]',
                'CROSS_BUTTON': '[data-test-id="cross"]',
                'INVALID_EMAIL_SPAN': '[data-test-id="recovery-error-invalidEmail"]',
                }

    def add_email(self):
        self.page.wait_for_clickable_by_selector(self.LOCATORS['ADD_BUTTON'])
        self.page.driver.find_element_by_css_selector(self.LOCATORS['ADD_BUTTON']).click()

    def set_email(self, email):
        self.page.waiting_for_visible_by_selector(self.LOCATORS['EMAIL_INPUT'])
        email_input = self.page.driver.find_element_by_css_selector(self.LOCATORS['EMAIL_INPUT'])
        email_input.click()
        email_input.send_keys(email)

    def check_invalid_email(self):
        self.page.waiting_for_visible_by_selector(self.LOCATORS['INVALID_EMAIL_SPAN'])
        invalid_span = self.page.driver.find_element_by_css_selector(self.LOCATORS['INVALID_EMAIL_SPAN'])
        invalid_span_text = invalid_span.find_element_by_tag_name('span').get_attribute("innerText")
        assert invalid_span_text == self.CONSTANTS['invalid_email']

    def cancel(self):
        self.page.wait_for_clickable_by_selector(self.LOCATORS['CANCEL_BUTTON'])
        self.page.driver.find_element_by_css_selector(self.LOCATORS['CANCEL_BUTTON']).click()

    def success(self):
        self.page.wait_for_clickable_by_selector(self.LOCATORS['SUCCESS_BUTTON'])
        self.page.driver.find_element_by_css_selector(self.LOCATORS['SUCCESS_BUTTON']).click()

    def close(self):
        self.page.wait_for_clickable_by_selector(self.LOCATORS['CROSS_BUTTON'])
        self.page.driver.find_element_by_css_selector(self.LOCATORS['CROSS_BUTTON']).click()

    def wait_for_container(self):
        self.page.waiting_for_visible_by_selector(self.LOCATORS['ROOT'])

    def wait_for_container_close(self):
        self.page.waiting_for_invisible_by_selector(self.LOCATORS['ROOT'])


