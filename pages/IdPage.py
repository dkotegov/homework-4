from steps.IdSteps import PersonaInfoSteps
from .BasePage import Page
from selenium.common.exceptions import TimeoutException


class Main_page(Page):
    BASE_URL = "https://id.mail.ru"
    PATH = ""

    @property
    def personal_info_steps(self):
        return PersonaInfoSteps(self.driver)

    def click_change_personal_info(self) -> bool:
        """
        :return: Произошел ли удачный переход на страницу смены информации
        """
        text = self.personal_info_steps.click_personal_info_settings()
        if text == "Личные данные":
            return True
        return False

    def click_get_all_settings(self) -> bool:
        """
        :return: Произошел ли удачный переход
        """
        text = self.personal_info_steps.click_all_settings()
        if text == "Контакты и адреса":
            return True
        return False

    def get_name_surname_from_left_bar(self) -> (str, str):
        return self.personal_info_steps.get_name_surname_from_left_bar()

    def get_name_surname_from_card(self) -> (str, str):
        return self.personal_info_steps.get_name_surname_from_card()

    def click_add_reserve_email(self) -> bool:
        """
        :return: Произошел ли удачный переход
        """
        text = self.personal_info_steps.click_add_reserve_email()
        if text == "Добавление резервной почты":
            return True
        return False

    def add_email(self, email) -> str:
        """
        :return: Значение хедера
        """
        self.personal_info_steps.clear_email()
        self.personal_info_steps.insert_reserve_email(email)
        self.personal_info_steps.click_confirm_email()
        try:
            return self.personal_info_steps.check_input_email_result()  # Проверяем есть ли сообщение об ошибке
        except TimeoutException:
            return self.personal_info_steps.get_correct_email_header()  # Если его нет, значит запрос корректный

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
