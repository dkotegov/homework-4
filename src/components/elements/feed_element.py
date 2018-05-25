from src.components.base_element import BaseElement


class FeedElement(BaseElement):

    NAV_SIDE = '//div[@class="nav-side __navigation"]'

    def is_exist_nav_side(self):
        return self.existence_of_element_by_xpath(self.NAV_SIDE)
