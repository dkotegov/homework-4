from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from nikita.pages.todo.default import Page
from nikita.components.todo.list_edit_modal import ListEditModal
from nikita.utils import wait_for_element_by_selector, wait_for_element_by_xpath, wait_for_element_attribute_change
from nikita.constants import FORBIDDEN_COLORS

class ListPage(Page):
    NAME_EDIT = '.ListTitle_base__1l0yT.ListTitle_editable__1HBI5'
    NAME = '.ListTitle_base__1l0yT.ListTitle_editable__1HBI5 h1'
    NAME_FORMAT = './/div[@class="ListTitle_base__1l0yT ListTitle_editable__1HBI5"]//h1[. = "{}"]'
    DESCRIPTION_EDIT = '.ListDescription_baseEditable__3dD20'
    DESCRIPTION = '.ListDescription_baseEditable__3dD20 p'
    DESCRIPTION_FORMAT = './/div[@class="ListDescription_baseEditable__3dD20"]//p[. = "{}"]'
    COLOR_EDIT = '.Dropdown_base__10MLk.Dropdown_bottomLeft__12Dqz .Color_base__373Wh'
    COLOR_FORMAT = './/div[@class="Dropdown_base__10MLk Dropdown_bottomLeft__12Dqz"]//div[@class="Color_base__373Wh"][@style="{}"]'
    COLORS = '.ColorPicker_colors__3vL92 .ColorRadio_colorRadio__1dLNj'
    SETTINGS = '.ASettingsButton_base__19nsY.ASettingsButton_normal__3ZTNb'
    EDIT = './/button[@class="MenuButton_base__2qd43"]//p[. = "Редактировать"]'
    DELETE = './/button[@class="MenuButton_base__2qd43"]//p[. = "Удалить"]'

    def change_name(self, name):
        wait_for_element_by_selector(self.driver, self.NAME_EDIT).click()
        actionChains = ActionChains(self.driver)
        actionChains.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).key_down(Keys.BACKSPACE).key_up(Keys.BACKSPACE).perform()
        actionChains.send_keys(name + Keys.ENTER).perform()

    def change_name_modal(self, name):
        self.open_modal()
        modal = ListEditModal(self.driver)
        modal.set_name(name)
        modal.save()

    def get_name(self):
        return wait_for_element_by_selector(self.driver, self.NAME).get_attribute('innerText')

    def change_description(self, description):
        wait_for_element_by_selector(self.driver, self.DESCRIPTION_EDIT).click()
        actionChains = ActionChains(self.driver)
        actionChains.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).key_down(Keys.BACKSPACE).key_up(Keys.BACKSPACE).perform()
        actionChains.send_keys(description + Keys.ENTER).perform()

    def change_description_modal(self, description):
        self.open_modal()
        modal = ListEditModal(self.driver)
        modal.set_description(description)
        modal.save()

    def get_description(self):
        return wait_for_element_by_selector(self.driver, self.DESCRIPTION).get_attribute('innerText')

    def change_color(self):
        currentColor = wait_for_element_by_selector(self.driver, self.COLOR_EDIT)
        currentColor.click()
        for color in self.driver.find_elements_by_css_selector(self.COLORS):
            if (color.get_attribute('style') != currentColor.get_attribute('style') and color.get_attribute('style') not in FORBIDDEN_COLORS):
                style = color.get_attribute('style')
                color.click()
                return style

    def change_color_modal(self):
        self.open_modal()
        modal = ListEditModal(self.driver)
        color = modal.change_color()
        modal.save()
        return color

    def delete(self):
        wait_for_element_by_selector(self.driver, self.SETTINGS).click()
        wait_for_element_by_xpath(self.driver, self.DELETE).click()

    def change_all_and_cancel_modal(self, name, description):
        self.open_modal()
        modal = ListEditModal(self.driver)
        modal.set_name(name)
        modal.set_description(description)
        modal.cancel()

    def open_modal(self):
        wait_for_element_by_selector(self.driver, self.SETTINGS).click()
        wait_for_element_by_xpath(self.driver, self.EDIT).click()

    def wait_for_name(self, name):
        wait_for_element_by_xpath(self.driver, self.NAME_FORMAT.format(name))

    def wait_for_description(self, description):
        wait_for_element_by_xpath(self.driver, self.DESCRIPTION_FORMAT.format(description))

    def wait_for_color(self, color):
        wait_for_element_by_xpath(self.driver, self.COLOR_FORMAT.format(color))
