# -*- coding: utf-8 -*-


import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from page import *


class BasicTest(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def login(self, username):
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.set_login(username)
        auth_form.set_password(PASSWORD)
        auth_form.submit()

    def logout(self):
        page = Page(self.driver)
        page.open()
        page.top_menu.open()
        page.top_menu.logout()

    def upload_photo(self, username, count=1):
        self.login(username)

        person_page = PersonPage(self.driver, '')
        photos = []

        for i in range(count):
            photos.append(person_page.photo_manager.upload_photo('pic.jpg'))

        self.logout()
        return photos

    def remove_photos(self, username, photos):
        self.logout()
        self.login(username)

        for i in photos:
            photo_page = PhotoPage(self.driver, i[1], i[0])
            photo_page.open()
            photo_page.remove()

        self.logout()
        return photos

    def set_marks(self, username, photos, marks):
        self.login(username)

        person_page = PersonPage(self.driver, '')
        name = person_page.get_name()

        for i in range(len(photos)):
            photo_page = PhotoPage(self.driver, photos[i][1], photos[i][0])
            photo_page.open()

            print(marks[i])
            mark = photo_page.mark
            mark.set_mark(marks[i])

        self.logout()
        return name

    def remove_marks(self, username, photos, name, logout=True, cancel=False):
        self.login(username)

        for photo in photos:
            photo_page = PhotoPage(self.driver, photo[1], photo[0])
            photo_page.open()

            marks = photo_page.marks
            marks.open()

            marks.remove(name)

            marks.cancel_remove() if cancel else None

        self.logout() if logout else None

    def check_marks(self, username, photos, mark_values, name, logout=True):
        self.login(username) if username else None

        for i in range(len(photos)):
            photo_page = PhotoPage(self.driver, photos[i][1], photos[0][0])
            photo_page.open()

            marks = photo_page.marks
            marks.open()

            if not marks.check_mark(mark_values[i], name):
                self.logout() if logout else None
                return False

        self.logout() if logout else None

        return True
