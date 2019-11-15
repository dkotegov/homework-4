# coding=utf-8

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from pages.authPage import AuthPage
from pages.mailPage import MailPage
from pages.ABPage import ABPage


class ABTests(unittest.TestCase):
    BROWSER_NAME = os.getenv('SELENIUM_TEST_BROWSER', 'CHROME')

    MAIL_URL = 'https://mail.ru/'
    ADDRESSBOOK_URL = 'https://e.mail.ru/addressbook'

    EMAIL = os.getenv('EMAIL', '5fuctorial')
    PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        self.driver = Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=getattr(DesiredCapabilities, self.BROWSER_NAME).copy()
        )

        self.page = AuthPage(self.MAIL_URL, self.driver)
        self.page.open()
        self.page.get_form.authenticate(self.EMAIL, self.PASSWORD)

        self.page = MailPage(self.MAIL_URL, self.driver)
        self.page.open()

        self.page.switch_to_ab()

        self.page = ABPage(self.ADDRESSBOOK_URL, self.driver)

    def tearDown(self):
        self.driver.quit()

# -------------------- crueltycute tests --------------------

    def testBlockedGroup(self):
        self.page.test_blocked_group()

    # def testAddToGroup(self):  # TODO(crueltycute): doesn't pass and breaks the next ones somehow
    #     self.page.add_to_group()

    def testAddNewGroup(self):
        self.page.add_group('kek')

    def testDuplicateGroupName(self):
        self.page.duplicate_group_name()

    def testRenameGroup(self):
        self.page.rename_group('new Kek')

    def testAddToFavorite(self):
        self.page.add_to_favorite()

    def testRemoveFromFavorite(self):
        self.page.remove_from_favorite()

# -------------------- Smet1 tests --------------------

    def testEditField(self):
        self.page.edit_field()

    def testMultipleSelected(self):
        self.page.multiple_selected()

    def testEditUser(self):
        self.page.edit_user()

    def testMultipleDelete(self):
        self.page.multiple_delete()

    def testRevertByFilter(self):
        self.page.revert_by_filter()

    def testDoubleRevert(self):
        self.page.double_revert()
