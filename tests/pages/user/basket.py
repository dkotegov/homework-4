from tests.pages.base import Page
from selenium.common.exceptions import NoSuchElementException


class BasketPage(Page):
    """
    Корзина
    """

    NOT_BASKETS = '//div[@class="basket-empty"]'
    DELETE_BASKET_BUTTON = '//button[@id="deleteButton{}"]'
    GO_TO_RESTAURANT_BUTTON = '//button[@id="goToStore{}"]'
    GO_TO_ORDER_PAGE_BUTTON = '//button[@id="orderButton{}"]'
    RESTAURANT_ID = '//td[@data-deleteid]'
    SWITCH_TABLE = '//span[@id="js__chose-table"]'
    SWITCH_LIST = '//span[@id="js__chose-list"]'

    def __init__(self, driver):
        self.PATH = 'chose/comparison'
        super(BasketPage, self).__init__(driver)

    def check_is_baskets(self):
        try:
            self.driver.find_elemen_by_xpath(self.NOT_BASKETS)
        except NoSuchElementException:
            return False
        return True

    def get_all_baskets(self):
        elements = self.driver.find_elements_by_xpath(self.RESTAURANT_ID)
        baskets = {}
        for i in range(len(elements)):
            elements = self.driver.find_elements_by_xpath(self.RESTAURANT_ID)  # need to become stable
            restaurant_name = elements[i].text
            basket_id = elements[i].get_attribute("data-deleteid")
            baskets[restaurant_name] = basket_id
        return baskets

    def delete_basket(self, basket_id):
        self.driver.find_element_by_xpath(self.DELETE_BASKET_BUTTON.format(basket_id)).click()

    def go_to_restaurant(self, basket_id):
        self.driver.find_element_by_xpath(self.GO_TO_RESTAURANT_BUTTON.format(basket_id)).click()

    def go_to_order_page(self, basket_id):
        self.driver.find_element_by_xpath(self.GO_TO_ORDER_PAGE_BUTTON.format(basket_id)).click()

    def switch_to_list(self):
        self.driver.find_element_by_xpath(self.SWITCH_LIST).click()

    def switch_to_table(self):
        self.driver.find_element_by_xpath(self.SWITCH_TABLE).click()
