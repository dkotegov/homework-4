from selenium.webdriver.remote.webelement import WebElement

from components.base_component import Component


class ContactsPhonePopup(Component):
    CONSTANTS = {
        'header_string': 'Добавление номера телефона',
        'invalid_phone_number': "Неправильный номер. Укажите другой.",
        'country_name': 'Украина',
        'country_code': '+380'
    }

    LOCATORS = {'ROOT': '[data-test-id="recovery-inner-popup"]',
                'PHONE_INPUT': '[data-test-id="phone-input"]',
                'COUNTRY_INPUT': '[data-test-id="country-select"]',
                'COUNTRY_OPTION_UKRAINE': "//*[text() = '{country}']".format(country=CONSTANTS['country_name']),
                'ADD_BUTTON': '[data-test-id="recovery-addPhone-submit"]',
                'CANCEL_BUTTON': '[data-test-id="recovery-addPhone-cancel"]',
                'CROSS_BUTTON': '[data-test-id="cross"]',
                'HEADER': "//*[text() = '{header}']".format(header=CONSTANTS['header_string']),
                'INVALID_PHONE_SPAN': '[data-test-id="recovery-error-invalidPhone"]'
                }

    def add_phone(self):
        self.page.wait_for_clickable_by_selector(self.LOCATORS['ADD_BUTTON'])
        self.page.driver.find_element_by_css_selector(self.LOCATORS['ADD_BUTTON']).click()

    def check_invalid(self):
        self.page.waiting_for_visible_by_selector(self.LOCATORS['INVALID_PHONE_SPAN'])
        invalid_span = self.page.driver.find_element_by_css_selector(self.LOCATORS['INVALID_PHONE_SPAN'])
        invalid_span_text = invalid_span.find_element_by_tag_name('span').get_attribute("innerText")
        assert invalid_span_text == self.CONSTANTS['invalid_phone_number']

    def set_phone(self, phone):
        self.page.waiting_for_visible_by_selector(self.LOCATORS['PHONE_INPUT'])
        phone_input = self.page.driver.find_element_by_css_selector(self.LOCATORS['PHONE_INPUT'])
        phone_input.click()
        phone_input.clear()
        phone_input.send_keys(phone)

    def change_country(self):
        self.page.wait_for_clickable_by_selector(self.LOCATORS['COUNTRY_INPUT'])
        self.page.driver.find_element_by_css_selector(self.LOCATORS['COUNTRY_INPUT']).click()
        self.page.waiting_for_visible_by_xpath(self.LOCATORS['COUNTRY_OPTION_UKRAINE'])
        self.page.driver.find_element_by_xpath(self.LOCATORS['COUNTRY_OPTION_UKRAINE']).click()
        phone_input = self.page.driver.find_element_by_css_selector(self.LOCATORS['PHONE_INPUT'])
        phone_input_value = phone_input.get_attribute('value')
        assert phone_input_value == self.CONSTANTS['country_code']

    def cancel(self):
        self.page.wait_for_clickable_by_selector(self.LOCATORS['CANCEL_BUTTON'])
        self.page.driver.find_element_by_css_selector(self.LOCATORS['CANCEL_BUTTON']).click()

    def close(self):
        self.page.wait_for_clickable_by_selector(self.LOCATORS['CROSS_BUTTON'])
        self.page.driver.find_element_by_css_selector(self.LOCATORS['CROSS_BUTTON']).click()

    def wait_for_container(self):
        self.page.waiting_for_visible_by_xpath(self.LOCATORS['HEADER'])
        self.page.waiting_for_visible_by_selector(self.LOCATORS['ROOT'])

    def wait_for_container_close(self):
        self.page.waiting_for_invisible_by_selector(self.LOCATORS['ROOT'])
