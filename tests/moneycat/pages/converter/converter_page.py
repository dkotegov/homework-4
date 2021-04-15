from testutils import Page
from .components import Converter


class ConverterPage(Page):
    base_url = "https://softree.group"

    class Actions:
        @staticmethod
        def enter_first_field(form: Converter, value):
            form.open_converter()
            prev = form.get_second_form_content()
            form.fill_first_field(value)
            return prev

        def enter_second_field(form: Converter, value):
            form.open_converter()
            prev = form.get_first_form_content()
            form.fill_second_field(value)
            return prev

    @property
    def form(self):
        return Converter(self.driver)