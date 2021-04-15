from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from components.base_component import BaseComponent
from selenium.common.exceptions import TimeoutException


class MainViewLocators:
    def __init__(self):
        self.search_title = '//div[@class="search-view__title"]'
        self.filters_btn = '//button[@class="genres-btn filter-btn"]'


class MainView(BaseComponent):
    def __init__(self, driver):
        super(MainView, self).__init__(driver)
        self.wait = WebDriverWait(self.driver, 20)
        self.locators = MainViewLocators()
    
    def click_filters_btn(self):
        """
        Кликает на кнопку "Фильтры"
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.filters_btn))
        )
        submit.click()
    
    def check_search_title_appearance(self) -> bool:
        """
        Ождиает пока не появится заголовок страницы поиска
        """
        try:
            element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.locators.search_title)))
        except TimeoutException:
            return False
        return True
