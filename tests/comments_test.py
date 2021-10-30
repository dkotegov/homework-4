import unittest
from selenium import webdriver

from pages import CommentsPage


class CommentsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.comments_page = CommentsPage(driver=self.driver)
        self.comments_page.open()

    def testRedirectToProductPage(self):
        """Заголовок отзыва. Переход на страницу товара при нажатие на название."""
        product_url = self.comments_page.click_product_name()
        url = self.driver.current_url
        self.assertEqual(url, product_url, "Не открылась страница товара")

    def testRedirectToUserPage(self):
        """Заголовок отзыва. Переход на страницу товара при нажатие на название."""
        user_url = self.comments_page.click_user_name()
        url = self.driver.current_url
        self.assertEqual(url, user_url, "Не открылась страница пользователя")
    
    def testSortByDate(self):
        """Заголовок отзыва. Переход на страницу товара при нажатие на название."""
        self.comments_page.set_sort_by_date()
        self.assertTrue(self.comments_page.check_sort_by_date(), "Неправильная сортировка по дате.")

    def testSortByRating(self):
        """Панель отзывов - заголовок. Сортировка по дате создания при нажатие кнопки сортировать по дате."""
        self.comments_page.set_sort_by_ratting()
        self.assertTrue(self.comments_page.check_sort_by_rating(), "Неправильная сортировка по рейтингу.")