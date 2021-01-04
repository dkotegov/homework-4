from steps.IdSteps import PersonaInfoSteps
from .BasePage import Page


class Main_page(Page):
    BASE_URL = "https://id.mail.ru"
    PATH = ""

    @property
    def personal_info_steps(self):
        return PersonaInfoSteps(self.driver)

    def click_change_personal_info(self) -> str:
        return self.personal_info_steps.click_personal_info_settings()

    def click_get_all_settings(self) -> str:
        """
        :return: Текст заголовка
        """
        return self.personal_info_steps.click_all_settings()

    def get_name_surname_from_card(self) -> (str, str):
        return self.personal_info_steps.get_name_surname_from_card()

    def click_add_reserve_email(self) -> bool:
        """
        :return: Текст в хедере
        """
        return self.personal_info_steps.click_add_reserve_email()

    def add_email(self, email, has_error=True) -> str:
        """
        :return: Значение хедера
        """
        self.personal_info_steps.clear_email()
        self.personal_info_steps.insert_reserve_email(email)
        self.personal_info_steps.click_confirm_email()
        if has_error:
            return self.personal_info_steps.check_input_email_result()
        else:
            return self.personal_info_steps.get_correct_email_header()

    def check_correct_email_header(self):
        return self.personal_info_steps.get_correct_email_header()

    def clear_reserve_email(self):
        self.open("https://id.mail.ru/contacts")
        self.personal_info_steps.click_delete_reserve_email_btn()
        self.personal_info_steps.click_confirm_button()
        self.personal_info_steps.check_if_deleted()

    def open_popup(self):
        self.open("https://id.mail.ru/contacts?open-add-extra-email=1")

    def close_pop_up(self) -> str:
        return self.personal_info_steps.close_pop_up()
