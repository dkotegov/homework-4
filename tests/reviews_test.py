from helpers import Test

from pages import ReviewsPage


class ReviewsTest(Test):
    def setUp(self):
        super().setUp()
        self.reviews_page = ReviewsPage(driver=self.driver)
        self.reviews_page.open()

    def testRedirectToProductPage(self):
        """Заголовок отзыва. Переход на страницу товара при нажатии на название"""
        review_id = self.reviews_page.review_block.get_review_id()

        product_url = self.reviews_page.review_block.get_product_name_url(review_id)
        self.reviews_page.review_block.click_product_name(review_id)

        url = self.driver.current_url
        self.assertEqual(url, product_url, "Не открылась страница товара")

    def testRedirectToUserPage(self):
        """Заголовок отзыва. Переход на страницу пользователя при нажатии на название"""
        review_id = self.reviews_page.review_block.get_review_id()

        user_url = self.reviews_page.review_block.get_user_name_url(review_id)
        self.reviews_page.review_block.click_user_name(review_id)

        url = self.driver.current_url
        self.assertEqual(url, user_url, "Не открылась страница пользователя")
    
    def testSortByDate(self):
        """Панель отзывов - заголовок. Сортировка по дате создания при нажатии кнопки сортировать по дате"""
        self.reviews_page.review_block.set_sort_by_ratting()
        self.reviews_page.review_block.set_sort_by_date()
        self.assertTrue(self.reviews_page.review_block.check_sort_by_date(), "Неправильная сортировка по дате")

    def testSortByRating(self):
        """Панель отзывов - заголовок. Сортировка по рейтингу при нажатии кнопки сортировать по рейтингу"""
        self.reviews_page.review_block.set_sort_by_ratting()
        self.assertTrue(self.reviews_page.review_block.check_sort_by_rating(), "Неправильная сортировка по рейтингу")
