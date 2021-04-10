from components.profile_form import ProfileForm
from pages.base_page import BasePage


class ProfilePage(BasePage):
    """
    Страница профиля
    """

    PATH = 'profile'

    def __init__(self, driver):
        self.profile_form = ProfileForm(driver)
        super(ProfilePage, self).__init__(driver, self.profile_form.locators.root)

    def check_open_page(self):
        return self.profile_form.is_open()

    def check_profile_email(self, email) -> bool:
        return self.profile_form.check_profile_email() == email
