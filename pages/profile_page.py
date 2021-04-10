from components.profile_form import ProfileForm
from pages.base_page import BasePage


class ProfilePage(BasePage):
    """
    Страница профиля
    """

    BASE_URL = 'https://studhunt.ru/'
    PATH = 'profile'

    def __init__(self, driver, container='//div[@id="app"]'):
        super(ProfilePage, self).__init__(driver, container)

        self.contact_form = ProfileForm(self.driver)

    def check_profile_email(self, email) -> bool:
        return self.contact_form.check_profile_email() == email
