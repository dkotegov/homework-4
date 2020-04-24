from components.base_component import Component


class ContactsDeleteEmailPopup(Component):
    LOCATORS = {'ROOT': '[data-test-id="recovery-inner-popup"]',
                'CANCEL_BUTTON': '[data-test-id="recovery-deleteEmail-cancel"]',
                'SUMBIT_BUTTON': '[data-test-id="recovery-deleteEmail-submit"]',
                'CROSS_BUTTON': '[data-test-id="cross"]',
                'DELETE_SUCCESS_SUBMIT': '[data-test-id="recovery-success-close"]'
                }

    def submit(self):
        self.page.wait_for_clickable_by_selector(self.LOCATORS['SUMBIT_BUTTON'])
        self.page.driver.find_element_by_css_selector(self.LOCATORS['SUMBIT_BUTTON']).click()

    def success_submit(self):
        self.page.wait_for_clickable_by_selector(self.LOCATORS['DELETE_SUCCESS_SUBMIT'])
        self.page.driver.find_element_by_css_selector(self.LOCATORS['DELETE_SUCCESS_SUBMIT']).click()

    def cancel(self):
        self.page.wait_for_clickable_by_selector(self.LOCATORS['CANCEL_BUTTON'])
        self.page.driver.find_element_by_css_selector(self.LOCATORS['CANCEL_BUTTON']).click()

    def close(self):
        self.page.wait_for_clickable_by_selector(self.LOCATORS['CROSS_BUTTON'])
        self.page.driver.find_element_by_css_selector(self.LOCATORS['CROSS_BUTTON']).click()

    def wait_for_container(self):
        self.page.waiting_for_visible_by_selector(self.LOCATORS['ROOT'])

    def wait_for_container_close(self):
        self.page.waiting_for_invisible_by_selector(self.LOCATORS['ROOT'])
