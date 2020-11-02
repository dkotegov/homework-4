from tests.pages.page import Page
from tests.components.add_restaurant_form import AddRestaurantForm


class AddRestaurantPage(Page):
    PATH = '/admin/restaurants/add'

    @property
    def add_form(self):
        return AddRestaurantForm(self.driver)

    def add_restaurant(self, title, address, radius, photo_path, description=""):
        form = AddRestaurantForm(self.driver)

        if description is "":
            description = "Это ресторан {}".format(title)

        form.wait_open()
        form.set_address(address)
        form.set_title(title)
        form.set_description(description)
        form.set_radius(radius)
        form.set_photo(photo_path)
        
        form.submit()

    