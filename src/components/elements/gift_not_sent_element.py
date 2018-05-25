from src.components.base_element import BaseElement


class GiftNotSentElement(BaseElement):

    XPATH_GIFT_NOT_SENT = '//div[@class="stub-empty __friends mb-12x"]'

    def __init__(self, driver):
        super(GiftNotSentElement, self).__init__(driver)

    def is_gift_not_sent(self):
        return self.existence_of_element_by_xpath(self.XPATH_GIFT_NOT_SENT)
