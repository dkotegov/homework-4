from pages.main_page import MainPage
from tests.base import BaseTest


class MainPageTestSuite(BaseTest):
    def test_movie_page_transition(self):
        main = MainPage(self.driver)
        main.open()
        title = main.get_first_movie_card().get_attribute('data-tooltip')
        main.go_to_first_movie_page()
        self.assertEqual(main.get_movie_title(), title)

    def test_best_movies_transition(self):
        main = MainPage(self.driver)
        main.open()
        main.go_to_best_movies()
        self.assertEqual(main.get_page_title(), 'Лучшие фильмы')

    def test_go_to_genre(self):
        main = MainPage(self.driver)
        main.open()
        genre = 'драма'
        main.select_genre(genre)
        main.go_to_movies_by_genre()
        self.assertEqual(main.get_page_title(), f'По жанрам: {genre}')

    def test_sorted_by_rating(self):
        main = MainPage(self.driver)
        main.open()
        main.go_to_best_movies()
        ratings = list(map(float, main.get_ratings()))
        self.assertEqual(ratings, sorted(ratings, reverse=True))

    def test_movie_page_transition_via_title(self):
        main = MainPage(self.driver)
        main.open()
        main.go_to_best_movies()
        main.go_to_movie_via_title()

    def test_movie_page_transition_via_poster(self):
        main = MainPage(self.driver)
        main.open()
        main.go_to_best_movies()
        main.go_to_movie_via_poster()

    def test_search_actor(self):
        main = MainPage(self.driver)
        main.open()
        main.search('клинт')
        self.assertEqual(main.get_first_search_card_item_type(), 'Актер')
        self.assertEqual(main.get_first_search_card_content(), 'Клинт Иствуд')

    def test_search_movie(self):
        main = MainPage(self.driver)
        main.open()
        main.search('хороший')
        self.assertEqual(main.get_first_search_card_item_type(), 'Фильм')
        self.assertEqual(main.get_first_search_card_content(), 'Хороший, плохой, злой')

    def test_search_user(self):
        main = MainPage(self.driver)
        main.open()
        main.search('zotov')
        self.assertEqual(main.get_first_search_card_item_type(), 'Пользователь')
        self.assertEqual(main.get_first_search_card_content(), 'zotovbackup')
