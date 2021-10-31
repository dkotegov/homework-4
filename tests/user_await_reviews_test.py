from helpers import Test

from pages import UserAwaitReviewsPage, RegistrationPage


class UserAwaitReviewsTest(Test):
    def setUp(self):
        super().setUp()
        self.await_reviews = UserAwaitReviewsPage(driver=self.driver)
        self.await_reviews.open()

    def testRedirectToRegPage(self):
        """Открытие страницы регистрации при переходе по ссылке не авторизированного пользователя"""
        registration = RegistrationPage(driver=self.driver)

        url = self.driver.current_url
        self.assertTrue(registration.is_compare_url(url), "Не открылась страница регистрации")

    def testOpeningPopup(self):
        """Плитка с ожидающим отзывом. Открытие попапа оценки пользователя при выборе продавца для оценки"""
        self.await_reviews.login.auth()
        self.await_reviews.open()

        self.await_reviews.await_review_block.click_card()
        self.assertTrue(self.await_reviews.review_popup.is_popup_opened(), "Не открылся попап")

    def testClosePopupCorrect(self):
        """Попап для отзыва. Возможность оставить отзыв не пропадет при закрытии попапа"""
        self.await_reviews.login.auth()
        self.await_reviews.open()

        before_click = self.await_reviews.await_review_block.count_cards()

        self.await_reviews.await_review_block.click_card()
        self.await_reviews.review_popup.click_close()
        self.assertEqual(before_click, self.await_reviews.await_review_block.count_cards(), "Товар пропал")

    def testSkipButton(self):
        """Попап для отзывов. Закрытие попапа при нажатии кнопки “Пропустить”"""
        self.await_reviews.login.auth()
        self.await_reviews.open()

        self.await_reviews.await_review_block.click_card()
        self.await_reviews.review_popup.click_skip()
        self.assertFalse(self.await_reviews.review_popup.is_popup_opened(), "Не закрылся попап")

    def testRateWithoutRating(self):
        """Попап для отзыва. Ошибка, если не поставить оценку и нажать кнопку “Оценить”"""
        self.await_reviews.login.auth()
        self.await_reviews.open()

        self.await_reviews.await_review_block.click_card()
        self.await_reviews.review_popup.click_rate()
        self.assertTrue(self.await_reviews.review_popup.is_error(), "Нет ошибки")
