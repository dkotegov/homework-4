from components.search_form import SearchForm
from pages.base_page import BasePage


class MainPage(BasePage):
    """
    Главная Страница
    """
    def __init__(self, driver):
        super(MainPage, self).__init__(driver)

        self.search_form = SearchForm(self.driver)

    def search_by_profession(self, **kwargs):

        self.search_form.input_profession(**kwargs)
        self.search_form.click_on_search()
