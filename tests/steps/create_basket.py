from tests.pages.user.restaurant import RestaurantPage


def create_basket_setup(t, restaurant_id):
    restaurant_page = RestaurantPage(t.driver, restaurant_id)
    restaurant_page.open()
    try:
        restaurant_page.add_to_basket_dish(0)
    except:
        pass
    return restaurant_page.get_restaurant_name()
