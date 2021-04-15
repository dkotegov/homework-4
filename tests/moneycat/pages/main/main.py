import testutils
from .components import SellForm
from .components import CurrencyList
from .components import HeaderForm


class MainPage(testutils.Page):
    base_url = "https://softree.group"

    @property
    def currency_list(self):
        return CurrencyList(self.driver)

    @property
    def header(self):
        return HeaderForm(self.driver)

    @property
    def sell_form(self):
        return SellForm(self.driver)
