from components.search_form import SearchForm
from pages.base_page import BasePage


class MainPage(BasePage):
    """
    Главная Страница
    """

    def __init__(self, driver, container='//div[@id="app"]'):
        super(MainPage, self).__init__(driver, container)

        self.search_form = SearchForm(self.driver)

    def search_by_profession(self, profession: str):
        self.search_form.input_profession(profession)
        self.search_form.click_on_search()

    def search_by_place(self, place: str):
        self.search_form.input_place(place)
        self.search_form.click_on_search()
