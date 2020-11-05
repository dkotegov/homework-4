from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from nikita.components.default import Component
from nikita.utils import wait_for_element_by_selector, wait_for_element_by_xpath
from nikita.constants import FORBIDDEN_COLORS

class ListEditModal(Component):
    NAME = 'input[name="name"]'
    DESCRIPTION = 'textarea'
    SAVE = './/button/span[. = "Сохранить"]/..'
    CANCEL = './/button/span[. = "Отменить"]/..'
    COLOR_EDIT = '.Dropdown_base__10MLk.Dropdown_bottomLeft__12Dqz .Color_base__373Wh'
    COLORS = '.ColorPicker_colors__3vL92 .ColorRadio_colorRadio__1dLNj'

    def set_name(self, name):
        nameElement = wait_for_element_by_selector(self.driver, self.NAME)
        nameElement.click()
        actionChains = ActionChains(self.driver)
        actionChains.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).key_down(Keys.BACKSPACE).key_up(Keys.BACKSPACE).perform()
        actionChains.send_keys(name + Keys.ENTER).perform()

    def set_description(self, description):
        descriptionElement = wait_for_element_by_selector(self.driver, self.DESCRIPTION)
        descriptionElement.clear()
        descriptionElement.send_keys(description)

    def change_color(self):
        currentColor = wait_for_element_by_selector(self.driver, self.COLOR_EDIT)
        for color in self.driver.find_elements_by_css_selector(self.COLORS):
            if (color.get_attribute('style') != currentColor.get_attribute('style') and color.get_attribute('style') not in FORBIDDEN_COLORS):
                style = color.get_attribute('style')
                color.click()
                return style

    def save(self):
        wait_for_element_by_xpath(self.driver, self.SAVE).click()

    def cancel(self):
        wait_for_element_by_xpath(self.driver, self.CANCEL).click()
