from components.profile_form import ProfileForm
from pages.base_page import BasePage


class ProfilePage(BasePage):
    """
    Страница профиля
    """

    BASE_URL = 'https://studhunt.ru/'
    PATH = 'profile'

    def __init__(self, driver):
        super(ProfilePage, self).__init__(driver)

        self.contact_form = ProfileForm(self.driver)

    def check_profile_email(self, email) -> bool:
        return self.contact_form.check_profile_email() == email
