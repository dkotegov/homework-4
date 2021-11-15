from components.component import Component


class AddressPopupComponent(Component):
    ADDRESS_INPUT = '//input[@id="js__map-add-address"]'
    SUBMIT_BUTTON = '//button[@id="js__add-new-address__btn"]'
    CLOSE_ICON = '//img[@class="icone-close"]'

    def set_address(self, address):
        self.driver.find_element_by_xpath(self.ADDRESS_INPUT).send_keys(address)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT_BUTTON).click()

    def close_popup(self):
        self.driver.find_element_by_xpath(self.CLOSE_ICON).click()
