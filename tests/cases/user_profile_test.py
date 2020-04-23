from tests.pages.user_profile import ProfilePage
from tests.pages.authorization import AuthForm
from tests.cases.base import TestAuthorizedWithFillFields


class ProfileTest(TestAuthorizedWithFillFields):
    def setUp(self):
        super().setUp()
        self.page = ProfilePage(self.driver)

    # Отправить сообщение обратной связи ( длина > 0 символов)
    def test_create_message(self):
        message = 'Проблемы'
        self.page.form.create_message(message)

    # Перейти внастройки профиля через кнопку в профиле
    def test_go_to_settings_from_profile(self):
        self.page.form.go_to_settings_from_profile()

    # Перейтив  настройки профиля через меню в хедере
    def test_go_to_settings_from_menu(self):
        self.page.form.go_to_settings_from_menu()
