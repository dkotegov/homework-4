from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from components.base_component import BaseComponent
from selenium.common.exceptions import TimeoutException


class FilterLocators:
    def __init__(self):
        self.root = '//div[@class="content__info-block-wrapper"]'
        self.genres_button = '//button[@class="genres-btn"]'
        self.genres_refs = '//div[@class="sub-menu__list"]/a'
        self.filters = '//div[@class="filters"]'
        self.genre_filter = '//div[@class="filters__item filters__genre-item"]'
        self.year_filter = '//div[@class="filters__item filters__year-item"]'
        self.country_filter = '//div[@class="filters__item filters__country-item"]'
        self.basket_btn = '//img[@class="filters__delete"]'
        self.selected_filters = '//div[@style="color: var(--shadow); background-color: var(--low-transparent-white);"]'


class Filter(BaseComponent):
    def __init__(self, driver):
        super(Filter, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = FilterLocators()

    def click_genres_button(self):
        """
        Нажимает на кнопку "Фильтр"
        """
        films = WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.locators.genres_button))
        )
        films.click()

    def get_genres_refs(self):
        """
        Получает элементы всех жанров
        """
        genres = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.genres_refs))
        )
        return genres

    def click_genre(self, genre):
        """
        Нажимает на один из жанров
        """
        genre.click()
    
    def click_genre_filter(self):
        """
        Кликает на фильтр жанра
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.genre_filter))
        )
        submit.click()
    
    def click_year_filter(self):
        """
        Кликает на фильтр года
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.year_filter))
        )
        submit.click()
    
    def click_country_filter(self):
        """
        Кликает на фильтр страны
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.country_filter))
        )
        submit.click()
    

    def click_basket_btn(self):
        """
        Кликает на кнопку "Корзина"
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.basket_btn))
        )
        submit.click()
    
    def check_appearance(self) -> bool:
        """
        Ождиает пока не появятся фильтры
        """
        try:
            element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.locators.filters)))
        except TimeoutException:
            return False
        return True
    
    def check_filters_all_clear(self) -> bool:
        """
        Ождиает пока не пропадут выбранные фильтры
        """
        try:
            element = self.wait.until(
                EC.invisibility_of_element_located((By.XPATH, self.locators.selected_filters)))
        except TimeoutException:
            return False
        return True
    
    def check_selected_filters(self) -> bool:
        """
        Ождиает пока не появятся выбранные фильтры
        """
        try:
            element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.locators.selected_filters)))
        except TimeoutException:
            return False
        return True
