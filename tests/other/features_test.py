# coding=utf-8

import unittest
from pages.features_page import FeaturesPage
from pages.groups_page import GroupsPage
from setup.default_setup import default_setup
import urllib


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

    def test_not_have_compose_button_on_user_without_email(self):
        """
        Отсутствие кнопки написания письма при отсутствии почты
        """
        self.groups.create_contact_without_email(self.names.contact_firstname)

        self.assertFalse(self.features.compose_button_exists('null'))

    def test_open_new_page_on_compose(self):
        """
        Открытие страницы e.mail.ru/compose?to<encode-почта контакта> при написании письма контакту
        """
        self.groups.create_contact(self.names.contact_email)
        self.features.compose(self.names.contact_email)

        self.driver.switch_to.window(window_name=self.driver.window_handles[-1])

        expected_url = "e.mail.ru/compose?to={}".format(urllib.quote(self.names.contact_email))
        self.assertIn(expected_url, self.driver.current_url)

    def test_not_have_create_event_button_on_user_without_email(self):
        """
        Отсутствие кнопки создания события при отсутствии почты
        """
        self.groups.create_contact_without_email(self.names.contact_firstname)

        self.assertFalse(self.features.create_event_button_exists('null'))

    def test_open_new_page_on_create_event(self):
        """
        Открытие страницы calendar.mail.ru с двумя участниками (почта пользователя и почта контакта) при создании события
        """
        self.groups.create_contact(self.names.contact_email)
        self.features.create_event(self.names.contact_email)

        self.driver.switch_to.window(window_name=self.driver.window_handles[-1])

        emails = self.features.get_attendee_emails()
        self.assertEqual(emails[0], self.EMAIL)
        self.assertEqual(emails[1], self.names.contact_email)
        self.assertIn("calendar.mail.ru", self.driver.current_url)
