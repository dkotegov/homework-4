from components.auth_form import AuthForm
from components.main_view import MainView
from components.filter import Filter
from pages.base import BasePage


class ContentPage(BasePage):
    """
    Страница контента (бесплатное / последнее)
    """

    def __init__(self, driver):
        self.PATH = 'free'
        self.auth_form = AuthForm(driver)
        super(ContentPage, self).__init__(driver, self.auth_form.locators.root)
        self.main_view = MainView(self.driver)
        self.filters = Filter(self.driver)
    
    def open_filters(self):
        self.main_view.click_filters_btn()
    
    def select_filters(self):
        self.open_filters()
        self.filters.click_genre_filter()
        self.filters.click_year_filter()
        self.filters.click_country_filter()
    
    def select_genre_filter(self):
        self.open_filters()
        self.filters.click_genre_filter()
    
    def clear_all(self):
        self.filters.click_basket_btn()
    
    def check_filters_appearance(self) -> bool:
        return self.filters.check_appearance()
    
    def check_filters_all_clear(self) -> bool:
        return self.filters.check_filters_all_clear()
    
    def check_selected_filters(self) -> bool:
        return self.filters.check_selected_filters()
