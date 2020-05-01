from tests.pages.user_profile import ProfilePage
from tests.cases.base import TestAuthorizedWithFillFields


class HeaderTest(TestAuthorizedWithFillFields):
    def setUp(self):
        super().setUp()
        self.page = ProfilePage(self.driver)

    # Переход к главной странице
    def test_go_to_index(self):
        self.page.header_form.go_to_index()

    # Переход на страницу профиля
    def test_go_to_profile(self):
        self.page.header_form.go_to_profile()

    # Переход к сообщениям
    def test_go_to_dialog(self):
        self.page.header_form.go_to_dialog()

    # Переход к настройкам
    def test_go_to_settings(self):
        self.page.header_form.go_to_settings_from_menu()

    # Выход из аккаунта
    def test_exit(self):
        self.page.header_form.go_to_exit()
