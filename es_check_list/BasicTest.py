# -*- coding: utf-8 -*-

import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from page import *


class BasicTest(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', 'FIREFOX')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.driver.implicitly_wait(10)
        self.photos = []

    def tearDown(self):
        if self.photos:
            self.remove_photos(USERNAME_SECOND, self.photos)
        self.driver.quit()

    def login(self, username, first=False):
        auth_page = AuthPage(self.driver)
        auth_page.open(first)
        auth_form = auth_page.form
        auth_form.set_login(username)
        auth_form.set_password(PASSWORD)
        auth_form.submit()

    def logout(self):
        page = Page(self.driver)
        page.open()
        page.top_menu.open()
        page.top_menu.logout()

    def upload_photo(self, username, count=1, logout=True):
        self.login(username, True)

        person_page = PersonPage(self.driver, '')
        photos = []
        photo_manager = person_page.photo_manager
        photo_manager.open()

        for i in range(count):
            photos.append(photo_manager.upload_photo('pic.jpg'))

        self.logout() if logout else None
        return photos

    def remove_photos(self, username, photos):
        self.logout()
        self.login(username)

        for i in photos:
            photo_page = PhotoPage(self.driver, i[1], i[0])
            photo_page.open()
            photo_page.remove()

        return photos

    def set_marks(self, username, photos, marks, logout=True):
        self.login(username) if username else None

        for i in range(len(photos)):
            photo_page = PhotoPage(self.driver, photos[i][1], photos[i][0])
            photo_page.open()

            mark = photo_page.mark
            if not mark.set_mark(marks[i]):
                return False

        self.logout() if logout else None
        return True

    def remove_marks(self, username, photos, name, logout=True, cancel=False):
        self.login(username)

        for photo in photos:
            photo_page = PhotoPage(self.driver, photo[1], photo[0])
            photo_page.open()

            marks = photo_page.marks
            marks.open()

            if not marks.remove(name):
                return False

            marks.cancel_remove() if cancel else None

        self.logout() if logout else None
        return True

    def check_marks(self, username, photos, mark_values, name, logout=True):
        self.login(username) if username else None

        for i in range(len(photos)):
            photo_page = PhotoPage(self.driver, photos[i][1], photos[i][0])
            photo_page.open()

            marks = photo_page.marks

            if not marks.open():
                return False

            if not marks.check_mark(mark_values[i], name):
                self.logout() if logout else None
                return False

        self.logout() if logout else None

        return True

    def get_name(self, username=None, logout=False):
        self.login(username) if username else None
        person_page = PersonPage(self.driver)
        name = person_page.get_name()
        self.logout() if logout else None

        return name
