# coding=utf-8
import time
import unittest
from datetime import datetime

from pages.contact_adding_page import ContactAddingPage
from setup.default_setup import default_setup


class AddContactTest(unittest.TestCase):

    def setUp(self):
        default_setup(self)

        self.page = ContactAddingPage(self.driver)

        self.page.open()

        self.dmitry_contact = {
            "firstname": "Дмитрий".decode('utf-8'),
            "lastname": "Болдин".decode('utf-8'),
            "nick": "stalin",
            "company": "Mail.ru Group",
            "email": "d.boldin@corp.mail.ru",
            "phone": "какой-то телефон(проверяем что нет валидации)".decode('utf-8'),
            "comment": "Это комментарий".decode('utf-8'),
            "job_title": "Стажер".decode('utf-8'),
            "boss": "Иван Чашкин".decode('utf-8'),
            "address": "Где-то в москве".decode('utf-8'),
            "date_of_birth": {
                "day": 21,
                "month": "июнь".decode('utf-8'),
                "year": 2000,
            },
        }

        self.invalid_emails = [
            "это_имейл@mail.ru".decode('utf-8'),
            "email@email",
            "email.ru",
        ]

    def tearDown(self):
        self.page.open()

        self.page.delete_all_contacts()
        time.sleep(0.01)
        self.driver.quit()

    def test_adding_empty_contact(self):
        """
        Ошибка при добавлении контакта с пустыми полями
        """
        self.page.try_to_create_empty_contact()

        self.assertTrue(self.page.has_error())

    def test_invalid_email(self):
        """
         Ошибка при вводе невалидной почты
        """
        for email in self.invalid_emails:
            self.page.create_contact(email=email)
            self.assertTrue(self.page.has_validation_errors())
            self.page.return_back()

    # def test_time_from_future(self):
    #     """
    #     Ошибка при вводе даты из будущего
    #     """
    #     today = datetime.today()
    #
    #     # тогда дату из бущуего поставить невозможно
    #     if today.day == 31 and today.month == 12:
    #         pass
    #
    #     future_contact = self.dmitry_contact
    #     future_contact["date_of_birth"] = {
    #         "day": 31,
    #         "month": "декабрь".decode('utf-8'),
    #         "year": today.year,
    #     }
    #
    #     self.page.create_contact(**future_contact)
    #     self.assertTrue(self.page.has_validation_errors())

    def test_contact_adding(self):
        """
        Проврека успешного создания контакта
        """

        self.page.create_contact(**self.dmitry_contact)
        self.page.open()

        self.assertTrue(self.page.contact_exists(self.dmitry_contact['email']))

    def test_only_name(self):
        """
        Проверка создания контакта только с именем
        """

        self.page.create_contact(firstname=self.dmitry_contact["firstname"])
        self.page.open()

        self.assertFalse(self.page.has_any_error())

    def test_only_email(self):
        """
        Проверка создания контакта только с email
        """

        self.page.create_contact(email=self.dmitry_contact["email"])
        self.assertFalse(self.page.has_any_error())

    def test_latin(self):
        """
        Проверка создания контакта только с латинскими символами в имени
        """

        self.page.create_contact(nick="Some name")
        self.assertFalse(self.page.has_any_error())

    def test_unicode(self):
        """
        Проверка создания контакта с нетипичными unicode символами
        """

        self.page.create_contact(nick="ђћ∆".decode("utf-8"))
        self.assertFalse(self.page.has_any_error())

