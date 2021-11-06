from helpers import Page, Component
from components import Login


class CreateProductForm(Component):
    SUBMIT_ERROR = "#create-error"

    ERROR = "input-error"
    NAME = "#nameInput"
    PRICE = "#priceInput"
    DESCRIPTION = "#textareaInput"
    ADDRESS = "#addressInput"

    SUBMIT = "#submitProduct"

    PHOTO = "#file-upload0"
    MAP_POINT = ".ymaps-2-1-79-suggest-item-0"

    def enter_address(self):
        self.helpers.click_element(self.MAP_POINT)

    def upload_photo(self, path):
        photo = self.helpers.get_element(self.PHOTO)
        photo.send_keys(path)

    def input_name_value(self, text):
        self.helpers.input_value(self.NAME, text)

    def clear_name_value(self):
        self.helpers.clear_input(self.NAME)

    def is_error_name(self):
        return self.helpers.is_contains_class(self.NAME, self.ERROR)

    def input_price_value(self, text):
        self.helpers.input_value(self.PRICE, text)

    def clear_price_value(self):
        self.helpers.clear_input(self.PRICE)

    def is_error_price(self):
        return self.helpers.is_contains_class(self.PRICE, self.ERROR)

    def input_description_value(self, text):
        self.helpers.input_value(self.DESCRIPTION, text)

    def clear_description_value(self):
        self.helpers.clear_input(self.DESCRIPTION)

    def is_error_description(self):
        return self.helpers.is_contains_class(self.DESCRIPTION, self.ERROR)

    def input_address_value(self, text):
        self.helpers.input_value(self.ADDRESS, text)

    def clear_address_value(self):
        self.helpers.clear_input(self.ADDRESS)

    def is_error_address(self):
        return self.helpers.is_contains_class(self.ADDRESS, self.ERROR)

    def get_submit_error(self):
        return self.helpers.get_element(self.SUBMIT_ERROR).text

    def enter_submit(self):
        self.helpers.click_element(self.SUBMIT)


class CreateProductPage(Page):
    PATH = "/product/create"

    @property
    def form(self):
        return CreateProductForm(self.driver)

    @property
    def login(self):
        return Login(self.driver)
