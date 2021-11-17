from tests.pages.base import Page


class OrdersPage(Page):
    """
    Стриница заказов
    """

    NAME_RESTAURANT = '//h1[@class="block-restaurant__name "]'
    BUTTON_CHAT = '//button[@class="button block-order-state__chat"]'

    def __init__(self, driver):
        self.PATH = 'profile/orders'
        super(OrdersPage, self).__init__(driver)

    def click_first_restaurant_go_to_chat(self):
        self.driver.find_element_by_xpath(self.BUTTON_CHAT).click()

    def get_first_restaurant_name(self):
        return self.driver.find_element_by_xpath(self.NAME_RESTAURANT).text
