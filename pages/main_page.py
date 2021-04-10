from components.category_search_form import CategorySearchForm
from components.navbar_form import NavbarForm
from components.profile_form import ProfileForm
from components.search_form import SearchForm
from pages.base_page import BasePage


class MainPage(BasePage):
    """
    Главная Страница
    """

    def __init__(self, driver):
        self.search_form = SearchForm(driver)
        super(MainPage, self).__init__(driver, self.search_form.locators.root)
        self.navbar_form = NavbarForm(self.driver)
        self.profile_form = ProfileForm(self.driver)
        self.category_form = CategorySearchForm(self.driver)

    def search_by_profession(self, profession: str):
        self.search_form.input_profession(profession)
        self.search_form.click_on_search()

    def search_by_place(self, place: str):
        self.search_form.input_place(place)
        self.search_form.click_on_search()

    def search_by_place_and_profession(self, place: str,profession: str):
        self.search_form.input_profession(profession)
        self.search_form.input_place(place)
        self.search_form.click_on_search()

    def click_recommendations(self):
        self.navbar_form.click_on_recommendation()

    def click_vac_list(self):
        self.navbar_form.click_on_vacancies()

    def click_res_list(self):
        self.navbar_form.click_on_resumes()

    def click_comp_list(self):
        self.navbar_form.click_on_companies()

    def click_mainpage(self):
        self.navbar_form.click_on_logo()

    def click_auth_page(self):
        self.navbar_form.click_on_auth()

    def click_registration_page(self):
        self.navbar_form.click_on_registration()

    def click_profile_page(self):
        self.navbar_form.click_on_profile()

    def click_notif_popup(self):
        self.navbar_form.click_on_notification()

    def click_chats_page(self):
        self.navbar_form.click_on_chats()

    def click_logout(self):
        self.navbar_form.click_on_logout()

    def click_on_category(self) -> str:
        return self.category_form.click_on_category()

