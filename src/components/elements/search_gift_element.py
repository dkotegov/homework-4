from src.components.base_element import BaseElement


class SearchGiftElement(BaseElement):

    XPATH_GRID_SEARCH_HAS_DONE = '//div[@class="ugrid __xxxl __search __type-search"]'
    XPATH_GRID_SEARCH_NOT_FOUND = '//div[@class="stub-empty __gifts-search"]'

    def __init__(self, driver):
        super(SearchGiftElement, self).__init__(driver)

    def is_search_done(self):
        return self.existence_of_element_by_xpath(self.XPATH_GRID_SEARCH_HAS_DONE)

    def is_search_not_done(self):
        return self.existence_of_element_by_xpath(self.XPATH_GRID_SEARCH_NOT_FOUND)
