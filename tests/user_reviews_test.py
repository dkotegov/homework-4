from helpers import Test

from pages import ReviewsPage


class UserReviewsTest(Test):
    def setUp(self):
        super().setUp()
        self.reviews = ReviewsPage(driver=self.driver)
        self.reviews.open()

    def testRedirectToProductPage(self):
        """Заголовок отзыва. Переход на страницу товара при нажатии на название"""
        product_url = self.reviews.review_block.click_product_name()

        url = self.driver.current_url
        self.assertEqual(url, product_url, "Не открылась страница товара")

    def testRedirectToUserPage(self):
        """Заголовок отзыва. Переход на страницу товара при нажатии на название"""
        user_url = self.reviews.review_block.click_user_name()

        url = self.driver.current_url
        self.assertEqual(url, user_url, "Не открылась страница пользователя")
    
    def testSortByDate(self):
        """Заголовок отзыва. Переход на страницу товара при нажатии на название"""
        self.reviews.review_block.set_sort_by_date()
        self.assertTrue(self.reviews.review_block.check_sort_by_date(), "Неправильная сортировка по дате")

    def testSortByRating(self):
        """Панель отзывов - заголовок. Сортировка по дате создания при нажатии кнопки сортировать по дате"""
        self.reviews.review_block.set_sort_by_ratting()
        self.assertTrue(self.reviews.review_block.check_sort_by_rating(), "Неправильная сортировка по рейтингу")
