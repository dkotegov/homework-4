# coding=utf-8

import unittest
from pages.groups_page import GroupsPage
from pages.favorites_page import FavoritesPage
from setup.default_setup import default_setup


class FavoritesTest(unittest.TestCase):

    def setUp(self):
        default_setup(self)

        self.groups = GroupsPage(self.driver)
        self.favorites = FavoritesPage(self.driver)

        self.groups.open()

        self.groups.delete_all_groups()
        self.groups.delete_all_contacts()

    def tearDown(self):
        self.groups.open()

        self.driver.quit()

    def test_add_to_favorites_from_contact_page(self):
        """
        Добавление в избранное со страницы просмотра контакта
        """
        email = 'test@mail.ru'
        self.groups.create_contact(email)
        self.favorites.add_to_favorites_from_contact_page(email)

        self.assertTrue(self.groups.contacts_exists([email, ], 'star'))

    def test_add_to_favorites_from_groups(self):
        """
        Добавление в избранное через группы
        """
        email = 'test@mail.ru'
        self.groups.create_contact(email)
        self.groups.add_contact_to_groups(email, ['star', ])

        self.assertTrue(self.groups.contacts_exists([email, ], 'star'))

    def test_add_to_favorites_from_contact_list(self):
        """
        Добавление контакта в избранное из списка контактов(при клике на звездочку)
        """
        email = 'test@mail.ru'
        self.groups.create_contact(email)

        self.favorites.add_to_favorites_from_star_in_contact_list(email)

        self.assertTrue(self.groups.contacts_exists([email, ], 'star'))

    def test_delete_from_favorites_with_star_button(self):
        """
        Удаление с помощью клика на звездочку в списке контактов
        """
        email = 'test@mail.ru'
        self.groups.create_contact(email)

        self.favorites.add_to_favorites_from_star_in_contact_list(email)
        self.favorites.add_to_favorites_from_star_in_contact_list(email)  # second call deletes from favorites

        self.assertFalse(self.groups.contacts_exists([email, ], 'star'))

    def test_delete_from_favorites_group(self):
        """
        Удаление с удалением из группы "избранное"
        """
        email = 'test@mail.ru'
        self.groups.create_contact(email)
        self.groups.add_contact_to_groups(email, ['star', ])
        self.groups.add_contact_to_groups(email, ['star', ])  # second call deletes from favorites

        self.assertFalse(self.groups.contacts_exists([email, ], 'star'))

    def test_delete_from_favorites_with_star_button_on_contact_page(self):
        """
        Удаление через нажатие на звездочку на странице просмотра контакта
        """
        email = 'test@mail.ru'
        self.groups.create_contact(email)
        self.favorites.add_to_favorites_from_contact_page(email)
        self.favorites.add_to_favorites_from_contact_page(email)  # second call deletes from favorites

        self.driver.refresh()
        self.assertFalse(self.groups.contacts_exists([email, ], 'star'))
