from tests.pages.page import Page
from tests.components.address_form import AddressForm


class AddressPage(Page):
    PATH = ''

    @property
    def form(self):
        return AddressForm(self.driver)