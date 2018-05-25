from src.components.base_element import BaseElement


class VipGiftElement(BaseElement):

    XPATH_GRID = '//div[contains(@class, "ugrid")][contains(@class, "__vipSale")]'

    def __init__(self, driver):
        super(VipGiftElement, self).__init__(driver)

    def is_exists_gird(self):
        return self.existence_of_element_by_xpath(self.XPATH_GRID)
