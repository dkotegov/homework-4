from pages.BasePage import Page
from steps.SecuritySteps import SecuritySteps


class SecurityPage(Page):
    PATH = "security"

    def click_devices_link(self):
        security_steps = SecuritySteps(self.driver)
        security_steps.click_devices_link()

    def is_device_page_open(self) -> bool:
        security_steps = SecuritySteps(self.driver)
        return not (security_steps.get_device_page() is None)

    def click_services_link(self):
        security_steps = SecuritySteps(self.driver)
        security_steps.click_services_link()

    def is_service_page_open(self) -> bool:
        security_steps = SecuritySteps(self.driver)
        return not (security_steps.get_service_page() is None)

    def is_history_page_open(self) -> bool:
        security_steps = SecuritySteps(self.driver)
        return not (security_steps.get_history_page() is None)

    def click_history_link(self):
        security_steps = SecuritySteps(self.driver)
        security_steps.click_history_link()

    def click_keys_more_link(self):
        security_steps = SecuritySteps(self.driver)
        security_steps.click_keys_more_link()

    def is_keys_more_page_load(self) -> bool:
        security_steps = SecuritySteps(self.driver)
        return security_steps.is_url_equal('help.mail.ru/id/login/way/keys')

    def click_2fact_more_link(self):
        security_steps = SecuritySteps(self.driver)
        security_steps.click_2fact_more_link()

    def is_2fact_more_page_load(self) -> bool:
        security_steps = SecuritySteps(self.driver)
        return security_steps.is_url_equal('help.mail.ru/id/protection/2auth')

    def is_keys_page_load(self) -> bool:
        security_steps = SecuritySteps(self.driver)
        return security_steps.is_url_equal('account.mail.ru/security/authentication/keys')


    def is_2fact_page_load(self) -> bool:
        security_steps = SecuritySteps(self.driver)
        return security_steps.is_url_equal('account.mail.ru/user/2-step-auth')

    def click_set_password_link(self):
        security_steps = SecuritySteps(self.driver)
        security_steps.click_set_password_link()

    def is_set_password_popup_open(self) -> bool:
        security_steps = SecuritySteps(self.driver)
        return not (security_steps.get_set_password_popup() is None)

    def click_keys_link(self):
        security_steps = SecuritySteps(self.driver)
        security_steps.click_keys_link()

    def click_2fact_link(self):
        security_steps = SecuritySteps(self.driver)
        security_steps.click_2fact_link()
