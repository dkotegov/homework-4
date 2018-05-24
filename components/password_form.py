from components.base_component import BaseComponent


class PasswordForm(BaseComponent):
    CURRENT_INPUT = "//input[@name='fr.oldPassword']"
    NEW_INPUT = "//input[@name='fr.newPassword']"
    RETYPE_INPUT = "//input[@name='fr.retypePassword']"
    ELEMENT_THIRD = "//div[contains(@class,'form form__gl-2-2')]/div[contains(@class,'form_i')][3]/span[2]"
    ELEMENT_SECOND = "//div[contains(@class,'form form__gl-2-2')]/div[contains(@class,'form_i')][2]/span[2]"
    ELEMENT_FIRST = "//div[contains(@class,'form form__gl-2-2')]/div[contains(@class,'form_i')][1]/span[2]"
    SUBMIT_BUTTON = "//input[@data-l='t,submit']"

    def get_current_password_input(self):
        return self.get_element_by_path(self.CURRENT_INPUT)

    def get_new_password_input(self):
        return self.get_element_by_path(self.NEW_INPUT)

    def get_retype_password_input(self):
        return self.get_element_by_path(self.RETYPE_INPUT)

    def get_password_element(self):
        return self.get_visibility_element_with_exception(self.ELEMENT_FIRST)

    def get_second_password_element(self):
        return self.get_visibility_element_with_exception(self.ELEMENT_SECOND)

    def get_third__password_element(self):
        return self.get_visibility_element_with_exception(self.ELEMENT_THIRD)

    def get_submit(self):
        return self.get_clickable_element(self.SUBMIT_BUTTON)
