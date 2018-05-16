from src.components.elements.main_element import MainElement
from src.pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)
        self.main_element = MainElement(self.driver)

    def open_gifts(self):
        button = self.main_element.get_gifts_button()
        button.click()
        return button
