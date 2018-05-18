from src.components.base_element import BaseElement


class InventoriesElement(BaseElement):

    XPATH_GRID = '//div[@class="ugrid_cnt"]'

    def is_exists_grid(self):
        """
        Check for the existence of marked friends item in nav bar
        :return: Bool
        """
        return self.existence_of_element_by_xpath(self.XPATH_GRID)
