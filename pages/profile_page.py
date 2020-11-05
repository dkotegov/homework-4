from base_classes.page import Page
from components.profile_form import ProfileForm


class ProfilePage(Page):
    PATH = 'profile'
    CONTAINER = '//div[@class="profile"]'

    @property
    def profile_form(self):
        return ProfileForm(self.driver)

    def change_name(self, name: str):
        self.profile_form.set_name(name)
        self.profile_form.submit_about()
        if self.profile_form.is_invalid_name():
            return False

        self.reload()
        return True

    def change_surname(self, surname: str):
        self.profile_form.set_surname(surname)
        self.profile_form.submit_about()
        if self.profile_form.is_invalid_surname():
            return False

        self.reload()
        return True

    def change_avatar(self, path_to_avatar: str):
        self.profile_form.set_avatar(path_to_avatar)
        if self.profile_form.is_invalid_avatar():
            return False

        self.reload()
        return True

    def change_password(self, old_password, new_password, new_password_repeat: str):
        self.profile_form.set_old_password(old_password)
        self.profile_form.set_new_password(new_password)
        self.profile_form.set_new_password_repeat(new_password_repeat)
        self.profile_form.submit_password()
        if self.profile_form.is_invalid_old_password() or self.profile_form.is_invalid_new_password():
            return False

        self.reload()
        return True

    def change_email(self, email: str):
        self.profile_form.set_email(email)
        self.profile_form.submit_email()
        if self.profile_form.is_invalid_email():
            return False

        self.reload()
        return True
