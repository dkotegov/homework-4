from tests.pages.base import Page


class RestaurantPage(Page):
    """
    Стриница ресторана
    """

    DISH_LIST = '//div[@class="card-food"]'

    def __init__(self, driver, restaurant_id):
        self.restaurant_id = restaurant_id
        self.PATH = 'store/' + str(restaurant_id)
        super(RestaurantPage, self).__init__(driver)

    def get_dishes(self):
        return self.driver.find_elements_by_xpath(self.DISH_LIST)
    