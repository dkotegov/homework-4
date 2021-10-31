from helpers import Test

from pages import AwaitReviewsPage, RegistrationPage


class UserAwaitReviewsTest(Test):
    def setUp(self):
        super().setUp()
        self.await_reviews_page = AwaitReviewsPage(driver=self.driver)
        self.await_reviews_page.open()

    def testRedirectToRegPage(self):
        """Открытие страницы регистрации при переходе по ссылке не авторизированного пользователя"""
        registration = RegistrationPage(driver=self.driver)

        url = self.driver.current_url
        self.assertTrue(registration.is_compare_url(url), "Не открылась страница регистрации")

    def testOpeningPopup(self):
        """Плитка с ожидающим отзывом. Открытие попапа оценки пользователя при выборе продавца для оценки"""
        self.await_reviews_page.login.auth()
        self.await_reviews_page.open()

        self.await_reviews_page.click_card()
        self.assertTrue(self.await_reviews_page.is_popup_opened(), "Не открылся попап")

    def testClosePopupCorrect(self):
        """Попап для отзыва. Возможность оставить отзыв не пропадет при закрытии попапа"""
        self.await_reviews_page.login.auth()
        self.await_reviews_page.open()

        before_click = self.await_reviews_page.count_cards()

        self.await_reviews_page.click_card()
        self.await_reviews_page.click_close()
        self.assertEqual(before_click, self.await_reviews_page.count_cards(), "Товар пропал")

    def testSkipButton(self):
        """Попап для отзывов. Закрытие попапа при нажатии кнопки “Пропустить”"""
        self.await_reviews_page.login.auth()
        self.await_reviews_page.open()

        self.await_reviews_page.click_card()
        self.await_reviews_page.click_skip()
        self.assertFalse(self.await_reviews_page.is_popup_opened(), "Не закрылся попап")

    def testRateWithoutRating(self):
        """Попап для отзыва. Ошибка, если не поставить оценку и нажать кнопку “Оценить”"""
        self.await_reviews_page.login.auth()
        self.await_reviews_page.open()

        self.await_reviews_page.click_card()
        self.await_reviews_page.click_rate()
        self.assertTrue(self.await_reviews_page.is_error(), "Нет ошибки")
