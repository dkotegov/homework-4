from components.base_component import BaseComponent


class AuthForm(BaseComponent):
    EMAIL_INPUT = "//input[@id='field_email']"
    PASSWORD_INPUT = "//input[@id='field_password']"
    SUBMIT_BUTTON = "//input[@class='button-pro __wide']"
    LOGOUT_BAR = "//div[@class='ucard-mini_cnt_i']"
    LOGOUT_BUTTON = "//a[@data-l='t,logoutCurrentUser']"
    CONFIRM_LOGOUT_BUTTON = "//input[@class='button-pro form-actions_yes']"
    ADD_PROFILE_BUTTON = "//a[@data-l='t,add_user']"

    def get_login(self):
        return self.get_visibility_element(self.EMAIL_INPUT)

    def get_password(self):
        return self.get_visibility_element(self.PASSWORD_INPUT)

    def submit(self):
        return self.get_clickable_element(self.SUBMIT_BUTTON)

    def get_add_profile_button(self):
        return self.get_clickable_element(self.ADD_PROFILE_BUTTON)

    # def get_logout_bar(self):
    #     return self.driver.find_element_by_xpath(self.LOGOUT_BAR)
    #     #return self.get_clickable_element(self.LOGOUT_BAR)
    #
    # def get_logout_button(self):
    #     return self.driver.find_element_by_xpath(self.LOGOUT_BUTTON)
    #     #return self.get_clickable_element(self.LOGOUT_BUTTON)
    #
    # def get_confirm_logout_button(self):
    #     #return self.driver.find_element_by_xpath(self.CONFIRM_LOGOUT_BUTTON)
    #     return self.get_clickable_element(self.CONFIRM_LOGOUT_BUTTON)

