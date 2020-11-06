# coding=utf-8
import time
import unittest

from pages.contact_adding_page import ContactAddingPage
from pages.contact_edit_page import ContactEditPage
from setup.default_setup import default_setup


class DeleteContactsTest(unittest.TestCase):

    def setUp(self):
        default_setup(self)

        self.add_page = ContactAddingPage(self.driver)
        self.edit_page = ContactEditPage(self.driver)

        self.add_page.open()

        self.dmitry_contact = {
            "firstname": "Дмитрий".decode('utf-8'),
            "lastname": "Болдин".decode('utf-8'),
            "nick": "stalin",
            "company": "Mail.ru Group",
            "email": ["d.boldin@corp.mail.ru"],
            "phone": "какой-то телефон(проверяем что нет валидации)".decode('utf-8'),
            "comment": "Это комментарий".decode('utf-8'),
            "job_title": "Стажер".decode('utf-8'),
            "boss": "Иван Чашкин".decode('utf-8'),
            "address": "Где-то в москве".decode('utf-8'),
        }
        self.dmitry_contact1 = {
            "firstname": "Дмитрий".decode('utf-8'),
            "lastname": "Болдин".decode('utf-8'),
            "nick": "stalin",
            "company": "Mail.ru Group",
            "email": ["d.boldin1@corp.mail.ru"],
            "phone": "какой-то телефон(проверяем что нет валидации)".decode('utf-8'),
            "comment": "Это комментарий".decode('utf-8'),
            "job_title": "Стажер".decode('utf-8'),
            "boss": "Иван Чашкин".decode('utf-8'),
            "address": "Где-то в москве".decode('utf-8'),
        }
        self.dmitry_contact2 = {
            "firstname": "Дмитрий".decode('utf-8'),
            "lastname": "Болдин".decode('utf-8'),
            "nick": "stalin",
            "company": "Mail.ru Group",
            "email": ["d.boldin2@corp.mail.ru"],
            "phone": "какой-то телефон(проверяем что нет валидации)".decode('utf-8'),
            "comment": "Это комментарий".decode('utf-8'),
            "job_title": "Стажер".decode('utf-8'),
            "boss": "Иван Чашкин".decode('utf-8'),
            "address": "Где-то в москве".decode('utf-8'),
        }

    def tearDown(self):
        self.add_page.open()

        self.add_page.delete_all_contacts()
        self.driver.quit()

    def test_delete_contact_from_page(self):
        """
        Удаление контакта со страницы просмотра контакта
        """
        self.add_page.create_contact(**self.dmitry_contact)
        self.add_page.open_contact_page("d.boldin@corp.mail.ru")
        self.edit_page.delete_contact()
        self.assertFalse(self.add_page.contact_exists("d.boldin@corp.mail.ru"), "Ошибка, контакт существует")

    def test_delete_contact_on_select(self):
        """
        Удаление контакта путем выделения(нажатия на фотографию) из списка контактов
        """
        self.add_page.create_contact(**self.dmitry_contact)
        self.assertTrue(self.add_page.contact_exists("d.boldin@corp.mail.ru"), "Ошибка, контакт не существует")
        self.add_page.contact_form.select_contacts(["d.boldin@corp.mail.ru"])
        self.add_page.contact_form.delete_contacts()
        self.driver.refresh()
        self.assertFalse(self.add_page.contact_exists("d.boldin@corp.mail.ru"), "Ошибка, контакт существует")

    def test_delete_several_contacts_from_page(self):
        """
        Удаление нескольких контактов с помощью выделения
        """
        self.add_page.create_contact(**self.dmitry_contact)

        self.add_page.create_contact(**self.dmitry_contact1)

        self.add_page.create_contact(**self.dmitry_contact2)

        self.assertTrue(self.add_page.contacts_exist(["d.boldin@corp.mail.ru", "d.boldin1@corp.mail.ru",
                                                      "d.boldin2@corp.mail.ru"]), "Ошибка, контакты не существуют")

        self.add_page.contact_form.select_contacts(["d.boldin@corp.mail.ru", "d.boldin1@corp.mail.ru"])
        self.add_page.contact_form.delete_contacts()
        self.driver.refresh()
        self.assertFalse(self.add_page.contacts_exist(["d.boldin@corp.mail.ru", "d.boldin1@corp.mail.ru"]),
                         "Ошибка, контакты существуют")

        self.assertTrue(self.add_page.contacts_exist(["d.boldin2@corp.mail.ru"]), "Ошибка, контакт не существует")

    def test_delete_all_contacts_from_page(self):
        """
        Удаление нескольких контактов с помощью выделения
        """
        self.add_page.create_contact(**self.dmitry_contact)

        self.add_page.create_contact(**self.dmitry_contact1)

        self.add_page.create_contact(**self.dmitry_contact2)

        self.assertTrue(self.add_page.contacts_exist(["d.boldin@corp.mail.ru", "d.boldin1@corp.mail.ru",
                                                      "d.boldin2@corp.mail.ru"]), "Ошибка, контакты не существуют")

        self.add_page.delete_all_contacts()
        self.driver.refresh()
        self.assertFalse(self.add_page.contacts_exist(["d.boldin@corp.mail.ru", "d.boldin1@corp.mail.ru",
                                                       "d.boldin2@corp.mail.ru"]), "Ошибка, контакты существуют")

    def test_delete_after_switching_page(self):
        """
        Удаление контакта после выделения и перехода на другую страницу
        """
        self.add_page.create_contact(**self.dmitry_contact)
        self.add_page.contact_form.select_contacts(["d.boldin@corp.mail.ru"])

        self.add_page.contact_form.open_personal_contacts()
        self.add_page.contact_form.delete_contacts()
        self.driver.refresh()
        self.assertFalse(self.add_page.contacts_exist(["d.boldin@corp.mail.ru"]), "Ошибка, контакт существует")

    def test_delete_with_dots(self):
        """
        Удаление контакта через контекстное меню(три точки)
        """
        self.add_page.create_contact(**self.dmitry_contact)
        self.assertTrue(self.add_page.contact_exists("d.boldin@corp.mail.ru"), "Ошибка, контакт не существует")

        self.add_page.contact_form.click_contact_dropdown("d.boldin@corp.mail.ru")
        self.add_page.contact_form.click_delete_in_dropdown()
        self.edit_page.removal_form.confirm_removal()
        self.driver.refresh()
        self.assertFalse(self.add_page.contacts_exist(["d.boldin@corp.mail.ru"]), "Ошибка, контакт существует")
