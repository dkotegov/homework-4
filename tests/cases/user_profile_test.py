from tests.pages.user_profile import ProfilePage
from tests.cases.base import TestAuthorized


class ProfileTest(TestAuthorized):
    def setUp(self):
        super().setUp()
        self.page = ProfilePage(self.driver)

    # Отправить сообщение обратной связи ( длина > 0 символов)
    def test_create_message(self):
        message = 'Проблемы'

        self.page.form.submit_message_button()
        self.page.form.set_question(message)
        self.page.form.submit_send_button()

        msg_text = self.page.form.get_message_from_field()
        self.assertEqual(msg_text, '', 'Error sending message')
