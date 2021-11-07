from helpers import Test

from pages import UserAwaitReviewsPage, MainPage, RegistrationPage


class UserAwaitReviewsTest(Test):
    def setUp(self):
        super().setUp()
        self.await_reviews_page = UserAwaitReviewsPage(driver=self.driver)

    def __auth__(self):
        main = MainPage(driver=self.driver)

        main.open()
        main.login.auth()
        self.await_reviews_page.open()

    def testRedirectToRegistrationPage(self):
        """Открытие страницы регистрации при переходе по ссылке не авторизированного пользователя"""
        registration = RegistrationPage(driver=self.driver)

        self.await_reviews_page.open(wait=False)

        url = self.driver.current_url
        self.assertTrue(registration.is_compare_url(url), "Не открылась страница регистрации")

    def testRedirectToRegistrationPageLogOut(self):
        """Открытие страницы регистрации при после выхода из профиля"""
        registration_page = RegistrationPage(driver=self.driver)

        self.__auth__()
        self.await_reviews_page.login.logout()

        url = self.driver.current_url
        self.assertTrue(registration_page.is_compare_url(url), "Не открылась страница регистрации")

    def testClosePopupCorrect(self):
        """Попап для отзыва. Возможность оставить отзыв не пропадет при закрытии попапа"""
        self.__auth__()

        card_id = self.await_reviews_page.await_review_block.get_card_id()

        self.await_reviews_page.await_review_block.click_card(card_id)
        self.await_reviews_page.review_popup.click_close()

        self.assertTrue(self.await_reviews_page.await_review_block.is_contains_card(card_id), "Пользователь пропал")

    def testSkipButton(self):
        """Попап для отзывов. Закрытие попапа при нажатии кнопки “Пропустить”"""
        self.__auth__()

        card_id = self.await_reviews_page.await_review_block.get_card_id()

        self.await_reviews_page.await_review_block.click_card(card_id)
        self.await_reviews_page.review_popup.click_skip()

        self.assertFalse(self.await_reviews_page.review_popup.is_popup_opened(), "Не закрылся попап")

    def testRateWithoutRating(self):
        """Попап для отзыва. Ошибка, если не поставить оценку и нажать кнопку “Оценить”"""
        self.__auth__()

        card_id = self.await_reviews_page.await_review_block.get_card_id()

        self.await_reviews_page.await_review_block.click_card(card_id)
        self.await_reviews_page.review_popup.click_rate()

        self.assertTrue(self.await_reviews_page.review_popup.is_error_form(), "Нет ошибки")
