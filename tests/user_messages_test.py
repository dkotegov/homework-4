import datetime

from helpers import Test

from pages import UserMessagesPage, MainPage, RegistrationPage


class UserMessagesTest(Test):
    def setUp(self):
        super().setUp()
        self.messages_page = UserMessagesPage(driver=self.driver)

    def __auth__(self):
        main_page = MainPage(driver=self.driver)

        main_page.open()
        main_page.login.auth()
        self.messages_page.open()

    def testRedirectToRegistrationPage(self):
        """Открытие страницы регистрации при переходе по ссылке не авторизированного пользователя"""
        registration_page = RegistrationPage(driver=self.driver)

        self.messages_page.open()

        url = self.driver.current_url
        self.assertTrue(registration_page.is_compare_url(url), "Не открылась страница регистрации")

    def testRedirectToRegistrationPageLogOut(self):
        """Открытие страницы регистрации при после выхода из профиля"""
        registration_page = RegistrationPage(driver=self.driver)

        self.__auth__()
        self.messages_page.login.logout()

        url = self.driver.current_url
        self.assertTrue(registration_page.is_compare_url(url), "Не открылась страница регистрации")

    def testRedirectToProductPageByName(self):
        """Меню истории сообщений - верхняя часть. Открытие страницы товара при нажатие на нижнюю надпись красного цвета"""
        self.__auth__()

        chat_id = self.messages_page.chats_block.get_chat_id()

        self.messages_page.chats_block.click_message_card(chat_id)
        product_url = self.messages_page.chats_block.get_product_name_url()
        self.messages_page.chats_block.click_product_name()

        url = self.driver.current_url
        self.assertEqual(url, product_url, "Не открылась страница товара")

    def testRedirectToProductPageByAvatar(self):
        """Меню истории сообщений - верхняя часть. Открытие объявления при нажатии на аватарку"""
        self.__auth__()

        chat_id = self.messages_page.chats_block.get_chat_id()

        self.messages_page.chats_block.click_message_card(chat_id)
        product_url = self.messages_page.chats_block.get_product_avatar_url()
        self.messages_page.chats_block.click_product_avatar()

        url = self.driver.current_url
        self.assertEqual(url, product_url, "Не открылась страница товара")

    def testRedirectToUserPage(self):
        """Меню истории сообщений - верхняя часть. Открытие профиля человека при нажатие на верхнюю надпись черного цвета"""
        self.__auth__()

        chat_id = self.messages_page.chats_block.get_chat_id()

        self.messages_page.chats_block.click_message_card(chat_id)
        user_url = self.messages_page.chats_block.get_user_name_url()
        self.messages_page.chats_block.click_user_name()

        url = self.driver.current_url
        self.assertEqual(url, user_url, "Не открылась страница пользователя")

    def testSendMessage(self):
        """Меню истории сообщений - нижнее меню. Отправка сообщения по кнопке “Отправить”"""
        message = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.__auth__()

        chat_id = self.messages_page.chats_block.get_chat_id()

        self.messages_page.chats_block.click_message_card(chat_id)
        self.messages_page.chats_block.send_message(message)
        self.messages_page.chats_block.wait_message(message)

        self.assertTrue(self.messages_page.chats_block.is_contains_message(message), "Нет сообщения")

    def testEmptyMessageError(self):
        """Меню истории сообщений - нижнее меню. При нажатие на кнопку “Отправить” с пустым инпутом ничего не происходит"""
        message = ""

        self.__auth__()

        chat_id = self.messages_page.chats_block.get_chat_id()

        self.messages_page.chats_block.click_message_card(chat_id)
        self.messages_page.chats_block.send_message(message)

        # не понятно как тут сделать wait, если сообщение не должно появится
        # для этого делаю перезагрузку страницы, если сообщение добавилось, тогда оно появится
        self.messages_page.open()
        self.messages_page.chats_block.click_message_card(chat_id)

        self.assertFalse(self.messages_page.chats_block.is_contains_message(message), "Есть сообщение")
