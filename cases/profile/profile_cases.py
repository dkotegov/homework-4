import random
import string
import time

from cases.base_cases import Test
from pages.profile_page import ProfilePage

letters = string.ascii_lowercase

NAME_ERROR = 'Имя не должно быть пустым или содержать цифры, спецсимволы и знаки препинания.'
DATE_ERROR = 'Некорректный формат даты рождения.'
EMAIL_ERROR = 'Неправильный формат электронной почты.'

PASSWORD_CHANGE_SUCCESS = 'Пароль успешно изменен.'

AVATAR_ERROR = 'Только картинки, пожалуйста!!!'


class ProfileTest(Test):
    def setUp(self):
        super().setUp()
        self.page = ProfilePage(self.driver)
        self.page.BASE_URL = 'https://qdaqda.ru/profile?tab=aboutTab'
        self.login()
        self.page.open()

    def test_profile_change_avatar(self):
        # Загружает картинку, показывает превью.

        style_before = self.page.get_avatar_pic_style()
        self.page.upload_avatar('/files/1.png')
        style_after = self.page.get_new_avatar_pic_style(style_before)

        self.assertNotEqual(style_before, style_after)

    def test_profile_change_avatar_error_not_pic(self):
        # Ошибка при попытке загрузки не картинки.

        self.page.upload_avatar('/files/1.zip')
        text = self.page.get_avatar_error()

        self.assertEqual(AVATAR_ERROR, text)

    ''' <BUG>
    def test_profile_change_avatar_error_big_file(self):
        # Ошибка при попытке загрузки тяжелого файла > 10 Мб. Проверить, что аватар не изменился.
    '''

    ''' Проверено в SubscriptionCases
    def test_profile_redirect_subs(self):
        # Переадресовывают на соответствующие страницы при нажатии.
    '''

    ''' Проверено в SearchCases
        def test_profile_back_button(self):
            # Переадресовывает на главную страницу.
    '''

    def test_profile_name_number_error(self):
        # Ошибка при смене: на имя с цифрами

        n = random.randint(1, 27)
        new_name = str(n) + ''.join(random.choice(letters) for i in range(10))

        self.page.fill_name(new_name)
        self.page.click_save_changes()
        error = self.page.get_name_error_text()

        self.assertEqual(NAME_ERROR, error)

    def test_profile_name_comma_error(self):
        # Ошибка при смене: на имя со знаками препинания.

        new_name = '.' + ''.join(random.choice(letters) for i in range(10))

        self.page.fill_name(new_name)
        self.page.click_save_changes()
        error = self.page.get_name_error_text()

        self.assertEqual(NAME_ERROR, error)

    def test_profile_name_special_error(self):
        # Ошибка при смене: на имя со знаками препинания.

        new_name = '@' + ''.join(random.choice(letters) for i in range(10))

        self.page.fill_name(new_name)
        self.page.click_save_changes()
        error = self.page.get_name_error_text()

        self.assertEqual(NAME_ERROR, error)

    ''' <BUG>
    def test_profile_name_long_error(self):
        # Ошибка при смене: на длинное имя (>256 символов).
    '''

    def test_profile_name_empty_error(self):
        # Ошибка при смене: на пустое имя

        new_name = ''

        self.page.fill_name(new_name)
        self.page.click_save_changes()
        error = self.page.get_name_error_text()

        self.assertEqual(NAME_ERROR, error)

    ''' <BUG>
    def test_profile_about_long_error(self):
        # Ошибка при сохранении со слишком длинной строкой.
    '''

    def test_profile_birthday_format_error(self):
        # При вводе чего-либо вне формата и попытке сохранить высвечивается предупреждение.

        n = random.randint(10, 27)
        new_date = '2000/01/' + str(n)

        self.page.fill_birthday(new_date)
        self.page.click_save_changes()
        self.page.wait_for_page(self.page.CONTAINER_BOTTOM)
        error = self.page.get_birthday_error_text()

        self.assertEqual(DATE_ERROR, error)

    ''' <BUG>
    def test_profile_city_long_error(self):
        # Ошибка при сохранении с длинной строкой (>256 символов).
    '''

    def test_profile_email_format_error(self):
        # Ошибка при вводе почты некорректного формата (отсутствие @, .<символы> и так далее).

        new_email = ''.join(random.choice(letters) for i in range(10))

        self.page.fill_email(new_email)
        self.page.click_save_changes()
        error = self.page.get_email_error_text()

        self.assertEqual(EMAIL_ERROR, error)

    '''<BUG>
    Остальное здесь забаговано, так как кто-то забыл повесить проверки /:
    '''