import os

from Components.component import Component
from PageObjects.page_objects import (AuthPage,MainPage)


class Commons(Component):
    LOGIN = os.environ['LOGIN']
    PASSWORD = os.environ['PASSWORD']

    def auth(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_login(self.LOGIN)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

    def open_groups_page(self):
        main_page = MainPage(self.driver)

        left_menu = main_page.left_menu
        left_menu.open_groups_page()