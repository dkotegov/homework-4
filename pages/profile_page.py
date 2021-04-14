import os

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


    def check_profile_email(self, email) -> bool:
        return self.profile_form.check_profile_email() == email

    def check_open_page(self):
        return self.profile_form.is_open()

    def check_profile_data(self, data):
        return self.profile_form.check_profile_name() == data['NAME'] and self.profile_form.check_profile_surname() == data['SURNAME'] and self.profile_form.check_profile_email() == data['EMAIL']

    def delete_account(self):
        self.profile_form.click_to_delete_btn()

    def click_link_to_my_cards(self):
        self.profile_form.click_to_my_cards()
        return self.profile_form.check_page_with_cards_is_open()

    def click_link_to_myResponses(self):
        self.profile_form.click_to_my_response()
        return self.profile_form.check_page_with_responses_is_open()

    def click_to_link_myFavorite(self):
        self.profile_form.click_to_my_fav()
        return self.profile_form.check_page_with_fav_is_open()

    def view_card(self):
        self.profile_form.click_to_open_card()

    def edit_card(self):
        self.profile_form.click_to_edit_card()

    def open_vacancy_responses(self):
        self.profile_form.open_vacancy_responses()

    def open_company_responses(self):
        self.profile_form.open_company_responses()

    def open_resume_responses(self):
        self.profile_form.open_resume_responses()

    def upload_avatar(self, path):
        btn = self.profile_form.click_to_load_btn()
        btn.send_keys(os.getcwd()+path)

    def check_upload_avatar(self):
        self.profile_form.check_avatar_loaded()

    def check_error(self, text):
        error = self.profile_form.check_error()
        return error == text

    def check_span_error(self, text):
        error = self.profile_form.check_error_phone()
        return error.text == text

    def edit(self, text, field_number):
        self.profile_form.click_to_edit_or_save_name(field_number)

        field = self.profile_form.get_edited_field()
        self.profile_form.clear(field)

        field.send_keys(text)
        self.profile_form.click_to_edit_or_save_name(field_number)

    def click_my_first_resume_edit(self):
        self.profile_form.click_first_my_resume_edit()

    def click_my_profile_info(self):
        self.profile_form.click_to_my_profile_info()

    def get_my_favorite(self) -> {}:
        self.profile_form.click_to_my_fav()
        return self.profile_form.get_favorite_data()

    def get_text(self, text, field_number):
        return text == self.profile_form.get_text_fields(field_number)


