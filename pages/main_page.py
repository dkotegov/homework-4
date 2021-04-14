from components.category_search_form import CategorySearchForm
from components.navbar_form import NavbarForm
from components.profile_form import ProfileForm
from components.search_form import SearchForm
from components.popular import PopularCategories
from components.notification import Notification
from pages.base_page import BasePage


class MainPage(BasePage):
    """
    Главная Страница
    """

    def __init__(self, driver):
        self.search_form = SearchForm(driver)
        self.navbar_form = NavbarForm(driver)
        super(MainPage, self).__init__(driver, self.navbar_form.locators.root)
        self.profile_form = ProfileForm(self.driver)
        self.category_form = CategorySearchForm(self.driver)
        self.popular_category = PopularCategories(self.driver)
        self.notification = Notification(self.driver)

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

    def click_create_vacancy(self):
        self.navbar_form.click_create_vacancy()

    def click_create_company(self):
        self.navbar_form.click_create_company()

    def click_create_resume(self):
        self.navbar_form.click_create_resume()

    def click_on_sphere(self, sphere):
        self.popular_category.click_category(sphere)

    def click_footer_btn(self):
        return self.popular_category.click_footer_btn()

    def get_text_empty_notif(self):
        return self.notification.get_text_empty_notif()

    def wait_notif_open(self):
        return self.notification.wait_for_open()

    def check_response(self):
        return self.notification.check_response()

    def delete_response(self):
        self.notification.delete_response()

    def check_notif_recommendations(self):
        text = self.notification.get_text_recommendations()
        return 'Подобрано' in text and 'рекомендуемая вакансия' in text

    def get_text_recommendation(self):
        return self.notification.get_text_recommendations()

    def click_notif_recommendation(self):
        self.notification.click_notif_recommendation()