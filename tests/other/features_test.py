# coding=utf-8

import unittest
from pages.features_page import FeaturesPage
from pages.groups_page import GroupsPage
from setup.default_setup import default_setup


class FeaturesTestNames:

    def __init__(self):
        self.contact_email = u'test@mail.ru'
        self.contact_firstname = u'Имя'


class FeaturesTest(unittest.TestCase):

    def setUp(self):
        default_setup(self)

        self.names = FeaturesTestNames()
        self.features = FeaturesPage(self.driver)
        self.groups = GroupsPage(self.driver)

        self.features.open()

        self.groups.delete_all_contacts()

    def tearDown(self):
        self.features.open()

        self.driver.quit()

    def test_have_compose_button_on_user_with_email(self):
        """
        Наличие кнопки написания письма при наличии почты
        """
        self.groups.create_contact(self.names.contact_email)

        self.assertTrue(self.features.compose_button_exists(self.names.contact_email))

    def test_not_have_compose_button_on_user_without_email(self):
        """
        Отсутствие кнопки написания письма при отсутствии почты
        """
        self.groups.create_contact_without_email(self.names.contact_firstname)

        self.assertFalse(self.features.compose_button_exists('null'))

    def test_open_new_page_on_compose(self):
        """
        Открытие страницы e.mail.ru при написании письма
        """
        self.groups.create_contact(self.names.contact_email)
        self.features.compose(self.names.contact_email)

        self.driver.switch_to.window(window_name=self.driver.window_handles[-1])

        self.assertIn("e.mail.ru", self.driver.current_url)

    def test_have_create_event_button_on_user_with_email(self):
        """
        Наличие кнопки создания события при наличии почты
        """
        self.groups.create_contact(self.names.contact_email)

        self.assertTrue(self.features.create_event_button_exists(self.names.contact_email))

    def test_not_have_create_event_button_on_user_without_email(self):
        """
        Отсутствие кнопки создания события при отсутствии почты
        """
        self.groups.create_contact_without_email(self.names.contact_firstname)

        self.assertFalse(self.features.create_event_button_exists('null'))

    def test_open_new_page_on_create_event(self):
        """
        Открытие calendar.mail.ru при создании события
        """
        self.groups.create_contact(self.names.contact_email)
        self.features.create_event(self.names.contact_email)

        self.driver.switch_to.window(window_name=self.driver.window_handles[-1])

        self.assertIn("calendar.mail.ru", self.driver.current_url)
