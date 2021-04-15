from testutils import Page
from .components import AvatarForm, MenuForm, PasswordForm


class Settings(Page):
    base_url = "https://softree.group"
    path = "settings"

    def open_pass_form(
        self,
        menu_form: MenuForm,
        pass_form: PasswordForm,
    ):
        menu_form.click_pass()
        return pass_form.password

    def open_avatar_form(
        self,
        menu_form: MenuForm,
        pass_form: PasswordForm,
    ):
        menu_form.click_avatar()
        return pass_form.email

    def update_pass(
        self,
        menu_form: MenuForm,
        pass_form: PasswordForm,
        old_pass: str,
        new_pass: str,
        repeat_pass: str
    ) -> None:
        menu_form.click_pass()
        pass_form.fill_form(old_pass, new_pass, repeat_pass)
        pass_form.submit()

    def update_avatar(
        self,
        menu_form: MenuForm,
        avatar_form: AvatarForm,
        file_path: str,
    ) -> list:
        menu_form.click_avatar()
        avatar_form.upload_file(file_path)
        return avatar_form.errors

    @property
    def avatar_form(self):
        return AvatarForm(self.driver)

    @property
    def menu_form(self):
        return MenuForm(self.driver)

    @property
    def password_form(self):
        return PasswordForm(self.driver)
