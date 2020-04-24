from components.base_component import Component


class ConfirmPhonePopup(Component):
    CONSTANTS = {
        'header_string': 'Подтвердите номер телефона',
        'invalid_code': 'Неправильный код. Попробуйте другой.',
        'empty_code': 'Укажите код',
    }
    LOCATORS = {'ROOT': '[data-test-id="recovery-inner-popup"]',
                'CHANGE_PHONE_REF': '[data-test-id="recovery-onPreviewBack"]',
                'CODE_INPUT': '[data-test-id="recovery-addvfy-confirm-input"]',
                'CONFIRM_BUTTON': '[data-test-id="recovery-addvfy-confirm-submit"]',
                'CANCEL_BUTTON': '[data-test-id="recovery-addvfy-confirm-cancel"]',
                'CROSS_BUTTON': '[data-test-id="cross"]',
                'HEADER': "//*[text() = '{header}']".format(header=CONSTANTS['header_string']),
                'INVALID_CODE_SPAN': '[data-test-id="recovery-error-invalidCode"]',
                'EMPTY_CODE_SPAN': '[data-test-id="recovery-error-requiredCode"]',
                }

    def confirm_code(self):
        self.page.wait_for_clickable_by_selector(self.LOCATORS['CONFIRM_BUTTON'])
        self.page.driver.find_element_by_css_selector(self.LOCATORS['CONFIRM_BUTTON']).click()

    def set_code(self, code):
        self.page.waiting_for_visible_by_selector(self.LOCATORS['CODE_INPUT'])
        code_input = self.page.driver.find_element_by_css_selector(self.LOCATORS['CODE_INPUT'])
        code_input.click()
        code_input.send_keys(code)

    def change_number(self):
        self.page.waiting_for_visible_by_selector(self.LOCATORS['CHANGE_PHONE_REF'])
        change_phone_ref = self.page.driver.find_element_by_css_selector(self.LOCATORS['CHANGE_PHONE_REF'])
        change_phone_ref.click()

    def check_code_invalid(self, code):
        self.set_code(code)
        self.confirm_code()
        invalid_span = self.page.driver.find_element_by_css_selector(self.LOCATORS['INVALID_CODE_SPAN'])
        invalid_span_text = invalid_span.find_element_by_tag_name('span').get_attribute("innerText")
        assert invalid_span_text == self.CONSTANTS['invalid_code']

    def check_code_empty(self):
        self.confirm_code()
        invalid_span = self.page.driver.find_element_by_css_selector(self.LOCATORS['EMPTY_CODE_SPAN'])
        invalid_span_text = invalid_span.find_element_by_tag_name('span').get_attribute("innerText")
        assert invalid_span_text == self.CONSTANTS['empty_code']

    def cancel(self):
        self.page.wait_for_clickable_by_selector(self.LOCATORS['CANCEL_BUTTON'])
        self.page.driver.find_element_by_css_selector(self.LOCATORS['CANCEL_BUTTON']).click()

    def close(self):
        self.page.wait_for_clickable_by_selector(self.LOCATORS['CROSS_BUTTON'])
        self.page.driver.find_element_by_css_selector(self.LOCATORS['CROSS_BUTTON']).click()

    def wait_for_container(self):
        self.page.waiting_for_visible_by_selector(self.LOCATORS['ROOT'])
        self.page.waiting_for_visible_by_xpath(self.LOCATORS['HEADER'])

    def wait_for_container_close(self):
        self.page.waiting_for_invisible_by_selector(self.LOCATORS['ROOT'])
