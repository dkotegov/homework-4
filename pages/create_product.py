from pages.default_page import DefaultPage


class CreateProductPage(DefaultPage):
    PATH = "product/create"

    SUBMIT_ERROR = "#create-error"

    ERROR = "input-error"
    NAME = "#nameInput"
    PRICE = "#priceInput"
    DESCRIPTION = "#textareaInput"
    ADDRESS = "#addressInput"

    SUBMIT = "#submitProduct"

    def input_name_value(self, text):
        self.__input_value__(self.NAME, text)

    def clear_name_value(self):
        self.__clear_input__(self.NAME)

    def is_error_name(self):
        return self.__element_contains_class__(self.NAME, self.ERROR)

    def input_price_value(self, text):
        self.__input_value__(self.PRICE, text)

    def clear_price_value(self):
        self.__clear_input__(self.PRICE)

    def is_error_price(self):
        return self.__element_contains_class__(self.PRICE, self.ERROR)

    def input_description_value(self, text):
        self.__input_value__(self.DESCRIPTION, text)

    def clear_description_value(self):
        self.__clear_input__(self.DESCRIPTION)

    def is_error_description(self):
        return self.__element_contains_class__(self.DESCRIPTION, self.ERROR)

    def input_address_value(self, text):
        self.__input_value__(self.ADDRESS, text)

    def clear_address_value(self):
        self.__clear_input__(self.ADDRESS)

    def is_error_address(self):
        return self.__element_contains_class__(self.ADDRESS, self.ERROR)

    def get_submit_error(self):
        return self.__get_element__(self.SUBMIT_ERROR).text

    def enter_submit(self):
        self.__click_button__(self.SUBMIT)
        