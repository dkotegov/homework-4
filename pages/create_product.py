from helpers import Page, Component
from components import Login


class CreateProductForm(Component):
    SUBMIT_ERROR = "#create-error"

    ERROR = "input-error"
    NAME = "#nameInput"
    PRICE = "#priceInput"
    DESCRIPTION = "#textareaInput"
    ADDRESS = "#addressInput"
    PHOTO = "#file-upload0"
    SUBMIT = "#submitProduct"

    MAP_POINT = ".ymaps-2-1-79-suggest-item-0"

    def input_name_value(self, text):
        self.helpers.clear_input(self.NAME)
        self.helpers.input_value(self.NAME, text)

    def is_error_name(self):
        return self.helpers.is_contains_class(self.NAME, self.ERROR)

    def input_price_value(self, text):
        self.helpers.clear_input(self.PRICE)
        self.helpers.input_value(self.PRICE, text)

    def is_error_price(self):
        return self.helpers.is_contains_class(self.PRICE, self.ERROR)

    def input_description_value(self, text):
        self.helpers.clear_input(self.DESCRIPTION)
        self.helpers.input_value(self.DESCRIPTION, text)

    def is_error_description(self):
        return self.helpers.is_contains_class(self.DESCRIPTION, self.ERROR)

    def input_address_value(self, text):
        self.helpers.clear_input(self.ADDRESS)
        self.helpers.input_value(self.ADDRESS, text)

    def is_error_address(self):
        return self.helpers.is_contains_class(self.ADDRESS, self.ERROR)

    def enter_address(self):
        self.helpers.click_element(self.MAP_POINT)

    def upload_photo(self, path):
        self.helpers.upload_file(self.PHOTO, path)

    def get_submit_error(self):
        return self.helpers.get_element(self.SUBMIT_ERROR).text

    def enter_submit(self):
        self.helpers.click_element(self.SUBMIT)


class CreateProductPage(Page):
    PATH = "/product/create"

    PAGE = ".board"

    def wait_page(self):
        self.__wait_page__(self.PAGE)

    def delete_product(self, product_id):
        url = self.BASE_URL + self.BACK_URL + "/product/delete/{}".format(product_id)
        self.helpers.fetch(url)

    @property
    def form(self):
        return CreateProductForm(self.driver)

    @property
    def login(self):
        return Login(self.driver)
