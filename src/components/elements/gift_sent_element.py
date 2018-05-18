from src.components.base_element import BaseElement


class GiftSentElement(BaseElement):

    XPATH_GIFT_SENT = '//div[@class="portlet_h_name_t"]'
    XPATH_GRID_PERSON_HAS_THIS_GIFT = '//div[@class="stub-empty_t"]'

    def __init__(self, driver):
        super(GiftSentElement, self).__init__(driver)

    def is_gift_sent(self):
        flag = self.existence_of_element_by_xpath(self.XPATH_GIFT_SENT)
        if not flag:
            flag = self.existence_of_element_by_xpath(self.XPATH_GRID_PERSON_HAS_THIS_GIFT)
        return flag
