from helpers import Test

from pages import UserMessagesPage, RegistrationPage


class UserMessagesTest(Test):
    def setUp(self):
        super().setUp()
        self.messages = UserMessagesPage(driver=self.driver)
        self.messages.open()

    def testRedirectToRegPage(self):
        """Открытие страницы регистрации при переходе по ссылке не авторизированного пользователя"""
        registration = RegistrationPage(driver=self.driver)

        url = self.driver.current_url
        self.assertTrue(registration.is_compare_url(url), "Не открылась страница регистрации")

    def testRedirectToProductPageByName(self):
        """Меню истории сообщений - верхняя часть. Открытие страницы товара при нажатие на нижнюю надпись красного цвета"""
        self.messages.login.auth()
        self.messages.open()

        self.messages.chats_block.click_message_card()
        product_url = self.messages.chats_block.click_product_name()

        url = self.driver.current_url
        self.assertEqual(url, product_url, "Не открылась страница товара")

    def testRedirectToProductPageByAvatar(self):
        """Меню истории сообщений - верхняя часть. Открытие объявления при нажатии на аватарку"""
        self.messages.login.auth()
        self.messages.open()

        self.messages.chats_block.click_message_card()
        product_url = self.messages.chats_block.click_product_avatar()

        url = self.driver.current_url
        self.assertEqual(url, product_url, "Не открылась страница товара")

    def testRedirectToUserPage(self):
        """Меню истории сообщений - верхняя часть. Открытие профиля человека при нажатие на верхнюю надпись черного цвета"""
        self.messages.login.auth()
        self.messages.open()

        self.messages.chats_block.click_message_card()
        user_url = self.messages.chats_block.click_user_name()

        url = self.driver.current_url
        self.assertEqual(url, user_url, "Не открылась страница пользователя")

    def testSendMessage(self):
        """Меню истории сообщений - нижнее меню. Отправка сообщения по кнопке “Отправить”"""
        message = "Тест"

        self.messages.login.auth()
        self.messages.open()
        self.messages.chats_block.click_message_card()

        before_send = self.messages.chats_block.count_messages()
        self.messages.chats_block.send_message(message)

        self.messages.open()
        self.messages.chats_block.click_message_card()
        after_send = self.messages.chats_block.count_messages()
        self.assertEqual(before_send + 1, after_send, "Количество сообщений не изменилось")

    def testEmptyMessageError(self):
        """Меню истории сообщений - нижнее меню. При нажатие на кнопку “Отправить” с пустым инпутом ничего не происходит"""
        message = ""

        self.messages.login.auth()
        self.messages.open()
        self.messages.chats_block.click_message_card()

        before_send = self.messages.chats_block.count_messages()
        self.messages.chats_block.send_message(message)

        after_send = self.messages.chats_block.count_messages()
        self.assertEqual(before_send, after_send, "Количество сообщений изменилось")

    def testOpenMessageHistory(self):
        """Меню выбора сообщений. При нажатии на чат - открытие чата с историей сообщений"""
        self.messages.login.auth()
        self.messages.open()

        self.messages.chats_block.click_message_card()
        self.assertTrue(self.messages.chats_block.is_chat_opened(), "Не открылся чат пользователя")
