from .BaseSteps import BaseSteps
from selenium.common.exceptions import TimeoutException


class PersonaInfoSteps(BaseSteps):
    bottom_buttons = '//div[@data-test-id="card-footer"]/a'
    personal_data_header = '//div[@data-test-id="mailid-profile-container"]/h1'
    contacts_header = '//h1[@data-test-id="main-header"]'
    name_surname_left_card_path = '//div[@data-test-id="form-group-fio"]/div/div/p'
    name_surname_left_bar_path = '//h3[@data-test-id="full-name"]'
    add_reserve_email = '//a[@data-test-id="add-button-extraEmail"]'
    reserve_email_header_pop_up = '//h1[@data-test-id="recovery-preview-addEmail-header"]/span'
    confirm_reserve_email_btn_path = '//button[@data-test-id="recovery-addEmail-submit"]'
    reserve_email_input = '//input[@data-test-id="recovery-addEmail-emailField-input"]'
    result_email_span = '//div[@data-test-id="error-footer-text"]/small/span'
    correct_email_header = '//h1[@data-test-id="recovery-success-addscc-header"]'
    delete_email_path = '//button[@data-test-id="recovery-delete-email-button"]'
    confirm_delete_email_button = '//button[@data-test-id="recovery-deleteEmail-submit"]'
    delete_header = '//h1[@data-test-id="recovery-success-dltscc-header"]'
    close_btn = '//button[@data-test-id="recovery-addEmail-cancel"]'

    def click_personal_info_settings(self) -> str:
        """
        :return: Текст хедера в личных данных
        """
        personal_info_btn = self.wait_until_and_get_elements_by_xpath(self.bottom_buttons)[0]
        personal_info_btn.click()
        return self.wait_until_and_get_elem_by_xpath(self.personal_data_header).text

    def click_all_settings(self) -> str:
        """
        :return: Текст хедера во вкладке контакты и адреса
        """
        all_settings_btn = self.wait_until_and_get_elements_by_xpath(self.bottom_buttons)[1]
        all_settings_btn.click()
        return self.wait_until_and_get_elem_by_xpath(self.contacts_header).text

    def get_name_surname_from_card(self) -> (str, str):
        """
        :return: Получает имя и фамилию из левой карточке на главной странице
        """
        text = str(
            self.wait_until_and_get_elem_by_xpath(self.name_surname_left_card_path).text
        )
        splited = text.split(" ")
        return splited[0], splited[1]

    def get_name_surname_from_left_bar(self) -> (str, str):
        """
        :return: Получает имя и фамилию из бокового бара
        """
        text = str(
            self.wait_until_and_get_elem_by_xpath(self.name_surname_left_bar_path).text
        )
        splited = text.split(" ")
        return splited[0], splited[1]

    def click_add_reserve_email(self):
        """
        :return: Текст хедера в pop up добавления почты
        """
        self.wait_until_and_get_elem_by_xpath(self.add_reserve_email).click()
        return self.wait_until_and_get_elem_by_xpath(
            self.reserve_email_header_pop_up
        ).text

    def click_confirm_email(self):
        self.wait_until_and_get_elem_by_xpath(
            self.confirm_reserve_email_btn_path
        ).click()

    def insert_reserve_email(self, email):
        self.wait_until_and_get_elem_by_xpath(self.reserve_email_input).send_keys(
            email
        )

    def check_input_email_result(self) -> str:
        """
        :return: Что произошло после ввода email
        """
        return self.wait_until_and_get_elem_by_xpath(self.result_email_span).text

    def get_correct_email_header(self) -> str:
        return self.wait_until_and_get_elem_by_xpath(self.correct_email_header).text

    def click_delete_reserve_email_btn(self):
        self.wait_until_and_get_elem_by_xpath(self.delete_email_path).click()

    def click_confirm_button(self):
        self.wait_until_and_get_elem_by_xpath(self.confirm_delete_email_button).click()

    def clear_email(self):
        self.wait_until_and_get_elem_by_xpath(self.reserve_email_input).clear()

    def check_if_deleted(self) -> bool:
        text = self.wait_until_and_get_elem_by_xpath(self.delete_header).text
        return text == "Резервная почта удалена"

    def close_pop_up(self):
        self.wait_until_and_get_elem_by_xpath(self.close_btn).click()
        return self.wait_until_and_get_elem_by_xpath(self.contacts_header).text
