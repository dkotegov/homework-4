from src.components.base_element import BaseElement
from src.components.elements.gift_sent_element import GiftSentElement
from src.components.elements.vip_gift_element import VipGiftElement


class VipGiftPage(BaseElement):

    def __init__(self, driver):
        super(VipGiftPage, self).__init__(driver)
        self._url = 'https://ok.ru/gifts/vipSale'
        self._element = VipGiftElement(driver)
        self._gift_sent_element = GiftSentElement(driver)

    def is_loaded(self):
        return self._element.is_exists_gird()

    def is_gift_sent(self):
        return self._gift_sent_element.is_gift_sent()
