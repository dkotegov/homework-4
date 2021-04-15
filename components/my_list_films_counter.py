from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from components.base_component import BaseComponent


class MyListFilmsCounterLocators:
    def __init__(self):
        self.root = '//div[@class="content__info-block-wrapper"]'
        self.film_button = '//button[@class="item__card"]'


class MyListFilmsCounter(BaseComponent):
    def __init__(self, driver):
        super(MyListFilmsCounter, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = MyListFilmsCounterLocators()

    def count_films(self) -> int:
        """
        Счатает количество фильмов
        """
        films = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.film_button))
        )
        return len(films)
