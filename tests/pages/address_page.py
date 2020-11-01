from tests.pages.page import Page
from tests.components.address_form import AddressForm


class AddressPage(Page):
    PATH = ''

    @property
    def form(self):
        return AddressForm(self.driver)

    def start_address(self, address):
        addr_form = AddressForm(self.driver)

        addr_form.wait_open()
        addr_form.set_address(address)
        addr_form.submit()