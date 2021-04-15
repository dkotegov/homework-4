from components.my_list_films_counter import MyListFilmsCounter
from pages.base import BasePage


class MyListPage(BasePage):
    """
    Страница избранного
    """
    def __init__(self, driver):
        self.PATH = 'mylist'
        self.my_list_films_counter = MyListFilmsCounter(driver)
        super(MyListPage, self).__init__(driver, self.my_list_films_counter.locators.root)
        self.films_number = 0

    def count_films(self):
        self.films_number = 0
        self.films_number = self.my_list_films_counter.count_films()

    def check_films_number_changed(self, is_added):
        films_number = self.my_list_films_counter.count_films()
        if is_added:
            return films_number == self.films_number + 1
        else:
            return films_number == self.films_number - 1
