from components.auth_form import AuthForm
from components.main_view import MainView
from pages.base import BasePage


class SearchPage(BasePage):
    """
    Страница поиска
    """

    def __init__(self, driver):
        self.PATH = 'browse'
        self.auth_form = AuthForm(driver)
        super(SearchPage, self).__init__(driver, self.auth_form.locators.root)
        self.main_view = MainView(self.driver)
    
    def check_appearance(self) -> bool:
        return self.main_view.check_search_title_appearance()
