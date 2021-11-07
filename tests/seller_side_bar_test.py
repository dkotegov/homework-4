from consts import SELLER_USER
from helpers import Test

from pages import SellerProductsPage, AchievementsPage, ReviewsPage


class SellerSideBarTest(Test):
    def setUp(self):
        super().setUp()
        self.seller_products_page = SellerProductsPage(driver=self.driver)
        self.seller_products_page.open()

    def testClickProduct(self):
        """Кнопка “Все объявления” в боковом меню. Переход на страницу всех объявлений продавца"""
        achievements_page = AchievementsPage(driver=self.driver)
        achievements_page.change_path(SELLER_USER)

        achievements_page.open()
        achievements_page.side_bar.click_products()

        self.seller_products_page.wait_page()
        url = self.driver.current_url
        self.assertTrue(self.seller_products_page.is_compare_url(url), "Не открылась страница всех объявлений")

    def testClickAchievements(self):
        """Кнопка “Достижения” в боковом меню. Переход на страницу достижений при нажатии"""
        achievements_page = AchievementsPage(driver=self.driver)

        self.seller_products_page.side_bar.click_achievements()

        achievements_page.wait_page()
        url = self.driver.current_url
        achievements_page.change_path(SELLER_USER)
        self.assertTrue(achievements_page.is_compare_url(url), "Не открылась страница достижений")

    def testClickReviews(self):
        """Кнопка “Отзывы” в боковом меню. Переход на страницу отзывов при нажатии"""
        reviews_page = ReviewsPage(driver=self.driver)

        self.seller_products_page.side_bar.click_reviews()

        reviews_page.wait_page()
        url = self.driver.current_url
        reviews_page.change_path(SELLER_USER)
        self.assertTrue(reviews_page.is_compare_url(url), "Не открылась страница отзывов")
