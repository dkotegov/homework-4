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

    def check_profile_data(self, data):
        return self.profile_form.check_profile_name() == data['name'] and self.profile_form.check_profile_surname() == data['surname'] and self.profile_form.check_profile_email() == data['email']

    def delete_account(self):
        self.profile_form.click_to_delete_btn()