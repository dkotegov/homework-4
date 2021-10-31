import unittest
from selenium import webdriver

from components import Header, SideBar
from pages import MessagesPage, RegistrationPage, ProductPage


class MessagesTest(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.messages_page = MessagesPage(driver=self.driver)
        self.messages_page.open()

    def testRedirectToRegPage(self):
        """Открытие страницы регистрации при переходе по ссылке неавторизированного пользователя"""
        registration = RegistrationPage(driver=self.driver)

        url = self.driver.current_url
        self.assertTrue(registration.is_compare_url(url), "Не открылась страница регистрации")

    def testRedirectToProductPageByName(self):
        """Меню истории сообщений - верхняя часть. Открытие страницы товара при нажатие на нижнюю надпись красного цвета"""
        self.messages_page.login.auth()
        self.messages_page.open()
        self.messages_page.click_message_card()
        product_url = self.messages_page.click_product_name()
        url = self.driver.current_url
        self.assertEqual(url, product_url, "Не открылась страница товара")

    def testRedirectToProductPageByAvatar(self):
        """Меню истории сообщений - верхняя часть. Открытие объявления при нажатие на аватарку."""
        self.messages_page.login.auth()
        self.messages_page.open()
        self.messages_page.click_message_card()
        product_url = self.messages_page.click_product_avatar()
        url = self.driver.current_url
        self.assertEqual(url, product_url, "Не открылась страница товара")

    def testRedirectToUserPage(self):
        """Меню истории сообщений - верхняя часть. Открытие профиля человека при нажатие на верхнюю надпись черного цвета."""
        self.messages_page.login.auth()
        self.messages_page.open()
        self.messages_page.click_message_card()
        user_url = self.messages_page.click_user_name()
        url = self.driver.current_url
        self.assertEqual(url, user_url, "Не открылась страница пользователя")

    def testSendMessage(self):
        """Меню истории сообщений - нижнее меню. Отправка сообщения по кнопке  “Отправить”"""
        self.messages_page.login.auth()
        self.messages_page.open()
        self.messages_page.click_message_card()
        before_send = self.messages_page.count_messages()
        self.messages_page.send_message("Тест")
        self.messages_page.open()
        self.messages_page.click_message_card()
        self.assertEqual(before_send + 1, self.messages_page.count_messages(), "Количество сообщений не изменилось.")

    def testEmptyMessageError(self):
        """Меню истории сообщений - нижнее меню. При нажатие на кнопку “Отправить” с пустым инпутом ничего не происходит"""
        self.messages_page.login.auth()
        self.messages_page.open()
        self.messages_page.click_message_card()
        before_send = self.messages_page.count_messages()
        self.messages_page.send_message("")
        self.assertEqual(before_send, self.messages_page.count_messages(), "Количество сообщений изменилось.")

    def testOpenMessageHistory(self):
        """Меню выбора сообщений. При нажатии на чат - открытие чата с историей сообщений."""
        self.messages_page.login.auth()
        self.messages_page.open()
        self.messages_page.click_message_card()
        self.assertTrue(self.messages_page.is_chat_opened(), "Не открылся чат пользователя")