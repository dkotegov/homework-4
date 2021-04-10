from components.navbar_form import NavbarForm
from components.search_form import SearchForm
from pages.base_page import BasePage


class MainPage(BasePage):
    """
    Главная Страница
    """

    def __init__(self, driver):
        super(MainPage, self).__init__(driver)

        self.search_form = SearchForm(self.driver)
        self.navbar_form = NavbarForm(self.driver)

    def search_by_profession(self, profession: str):
        self.search_form.input_profession(profession)
        self.search_form.click_on_search()

    def search_by_place(self, place: str):
        self.search_form.input_place(place)
        self.search_form.click_on_search()

    def check_open_vac_list(self):
        self.navbar_form.click_on_vacancies()

    def check_open_res_list(self):
        self.navbar_form.click_on_resumes()

    def check_open_comp_list(self):
        self.navbar_form.click_on_companies()

    def check_open_mainpage(self):
        self.navbar_form.click_on_logo()
