from tests.pages.base import Page
from components.navbar import NavbarComponent


class RestaurantPage(Page):
    """
    Стриница ресторана
    """

    RESTAURANT_NAME = '//span[@class="store-title__name"]'
    DISH_NAME = '//span[@class="card__name"]'
    DISH_ADD = '//button[@data-foodaddbuttonid]'
    DISH_INCREASE = '//button[@data-foodplusbuttonid]'
    DISH_DECREASE = '//button[@data-foodminusbuttonid]'
    DISH_COUNT = '//button[@data-foodnumbuttonid]'
    BASKET_DISH_INFO = '//div[@class="store-basket__food__main-info"]'
    BASKET_DISH_NAME = '//span[@class="store-basket__food-name"]'
    BASKET_DISH_COUNT = '//button[@class="store-basket__food-num"]'

    CLOSE_ADDRESS = '//img[@class="icone-close"]'

    CHECKOUT_BUTTON = '//button[@id="store-basket__order"]'
    COMPARISON_BUTTON = '//button[@id="store-basket__chose"]'

    def __init__(self, driver, restaurant_id):
        self.restaurant_id = restaurant_id
        self.PATH = 'store/' + str(restaurant_id)
        super(RestaurantPage, self).__init__(driver)

    @property
    def navbar(self):
        return NavbarComponent(self.driver)

    def get_restaurant_name(self):
        return self.driver.find_element_by_xpath(self.RESTAURANT_NAME).text

    def get_number_dish_in_menu(self):
        return len(self.driver.find_elements_by_xpath(self.DISH_NAME))

    def get_name_dish(self, number):
        return self.driver.find_elements_by_xpath(self.DISH_NAME)[number].text

    def add_to_basket_dish(self, number):
        self.driver.find_elements_by_xpath(self.DISH_ADD)[number].click()

    def get_basket_dishes(self):
        elements = self.driver.find_elements_by_xpath(self.BASKET_DISH_INFO)
        dishes = []
        for i in range(len(elements)):
            elements = self.driver.find_elements_by_xpath(self.BASKET_DISH_INFO)
            name = elements[i].find_elements_by_xpath(self.BASKET_DISH_NAME)[0].text
            count = elements[i].find_elements_by_xpath(self.BASKET_DISH_COUNT)[0].text
            dishes.append({'name': name, 'count': count})
        return dishes

    def increase_dish(self, number):
        self.driver.find_elements_by_xpath(self.DISH_INCREASE)[number].click()

    def decrease_dish(self, number):
        self.driver.find_elements_by_xpath(self.DISH_DECREASE)[number].click()

    def get_count_dish(self, number):
        return self.driver.find_elements_by_xpath(self.DISH_COUNT)[number].text

    def refresh_page(self):
        self.driver.refresh()

    def go_to_checkout(self):
        self.driver.find_element_by_xpath(self.CHECKOUT_BUTTON).click()

    def go_to_comparison(self):
        self.driver.find_element_by_xpath(self.COMPARISON_BUTTON).click()
