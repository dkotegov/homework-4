from src.pages.base_page import BasePage
from src.components.elements.inventories_element import InventoriesElement


class InventoriesPage(BasePage):

    def __init__(self, driver):
        super(InventoriesPage, self).__init__(driver)
        self.element = InventoriesElement(self.driver)

    def is_loaded(self):
        # TODO here you can add a search for other items
        is_exists_grid = self.element.is_exists_grid()
        return is_exists_grid
