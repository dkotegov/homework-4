from steps.BaseSteps import BaseSteps


class SecuritySteps(BaseSteps):
    devices_page = '//*[@data-test-id="garage-page"]'
    devices_link = '//*[@data-test-id="device-and-apps-item"]'

    services_link = '//*[@data-test-id="external-services-item"]'
    services_page = '//*[@data-test-id="oauth-applications"]'

    history_link = '//*[@data-test-id="actions-history-item"]'
    history_page = '//*[@data-test-id="settings-actions"]'

    setpassword_button = '//*[@data-test-id="password-action"]'
    setpassword_page = '//*[@data-test-id="popup-wrapper"]'


    keys_page_title = '//*[@data-test-id="caption"]'
    keys_link = '//*[@data-test-id="electronic-keys-item"]'

    twofact_link = '//*[@data-test-id="twofa-item"]'
    password_more_link = '//*[@data-test-id="password-item"]//*[@data-test-id="item-details"]'
    keys_more_link = '//*[@data-test-id="electronic-keys-item"]//*[@data-test-id="item-details"]'
    twofact_more_link = '//*[@data-test-id="twofa-item"]//*[@data-test-id="item-details"]'

    def click_devices_link(self):
        self.wait_until_and_get_elem_by_xpath(self.devices_link).click()

    def get_device_page(self):
        return self.wait_until_and_get_elem_by_xpath(self.devices_page)

    def click_services_link(self):
        self.wait_until_and_get_elem_by_xpath(self.services_link).click()

    def get_service_page(self):
        return self.wait_until_and_get_elem_by_xpath(self.services_page)

    def click_history_link(self):
        self.wait_until_and_get_elem_by_xpath(self.history_link).click()

    def get_history_page(self):
        self.driver.switch_to_window(self.driver.window_handles[1])
        element = self.wait_until_and_get_elem_by_xpath(self.history_page)
        return element

    def click_password_more_link(self):
        self.wait_until_and_get_elem_by_xpath(self.password_more_link).click()
        self.driver.switch_to_window(self.driver.window_handles[1])

    def click_2fact_more_link(self):
        self.wait_until_and_get_elem_by_xpath(self.twofact_more_link).click()


    def click_keys_more_link(self):
        self.wait_until_and_get_elem_by_xpath(self.keys_more_link).click()

    def click_set_password_link(self):
        self.wait_until_and_get_elem_by_xpath(self.setpassword_button).click()

    def get_set_password_popup(self):
        return self.wait_until_and_get_elem_by_xpath(self.setpassword_page)

    def click_keys_link(self):
        self.wait_until_and_get_elem_by_xpath(self.keys_link).click()

    def click_2fact_link(self):
        self.wait_until_and_get_elem_by_xpath(self.twofact_link).click()

