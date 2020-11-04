from base_classes.component import Component


class SettingsPopup(Component):
    DELETE_BOARD_BUTTON = '//div[contains(@class, "js-deleteBoard")]'

    def delete_board(self):
        self.driver.find_element_by_xpath(self.DELETE_BOARD_BUTTON).click()
