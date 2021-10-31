from helpers import Test

from pages import SellerProductsPage, AchievementsPage, ReviewsPage


class SellerSideBarTest(Test):
    def setUp(self):
        super().setUp()
        self.seller_products = SellerProductsPage(driver=self.driver)
        self.seller_products.open()

    def testClickProduct(self):
        """Кнопка “Все объявления” в боковом меню. Переход на страницу всех объявлений продавца"""
        self.seller_products.side_bar.click_seller_products()

        url = self.driver.current_url
        self.assertTrue(self.seller_products.is_compare_url(url), "Не открылась страница всех объявлений")

    def testClickAchievements(self):
        """Кнопка “Достижения” в боковом меню. Переход на страницу достижений при нажатии"""
        achievements = AchievementsPage(driver=self.driver)
        user_id = "1"

        self.seller_products.side_bar.click_achievements()

        url = self.driver.current_url
        achievements.change_path(user_id)
        self.assertTrue(achievements.is_compare_url(url), "Не открылась страница достижений")

    def testClickReviews(self):
        """Кнопка “Отзывы” в боковом меню. Переход на страницу отзывов при нажатии"""
        reviews = ReviewsPage(driver=self.driver)
        user_id = "1"

        self.seller_products.side_bar.click_reviews()

        url = self.driver.current_url
        reviews.change_path(user_id)
        self.assertTrue(reviews.is_compare_url(url), "Не открылась страница отзывов")
