import time

from .BaseSteps import BaseSteps, clear
from selenium.common.exceptions import TimeoutException


class InputAnnotationsErrors:
    def __init__(
            self, name_err: str, last_name_err: str, nickname_err: str, city_err: str
    ):
        self.name_err = name_err
        self.last_name_err = last_name_err
        self.nickname_err = nickname_err
        self.city_err = city_err


class PersonalDataSteps(BaseSteps):
    name_path = '//input[@data-test-id="firstname-field-input"]'
    last_name_path = '//input[@data-test-id="lastname-field-input"]'
    nickname_path = '//input[@data-test-id="nickname-field-input"]'
    city_path = '//input[@data-test-id="city-field-input"]'
    submit_btn_path = '//button[@data-test-id="save-button"]'
    name_err_path = '//small[@data-test-id="firstname-field-error"]'
    last_name_err_path = '//small[@data-test-id="lastname-field-error"]'
    nickname_err_path = '//small[@data-test-id="nickname-field-error"]'
    city_err_path = '//small[@data-test-id="city-field-error"]'
    avatar_input = '//input[@data-test-id="photo-file-input"]'
    upload_process = '//div[@data-test-id="photo-upload-progress"]'
    photo_ready = '//div[@data-test-id="photo-overlay"]'
    accept_city_popup = '//div[@data-test-id="select-value:Москва, Россия"]'

    def upload_avatar(self, path: str):
        el = self.wait_until_and_get_invisible_elem_by_xpath(self.avatar_input)
        el.send_keys(path)

    def click_submit_avatar_btn(self):
        submit_avatar_btn = self.wait_until_and_get_elements_by_xpath(self.submit_btn_path)[1]
        submit_avatar_btn.click()

    def fill_name(self, name):
        self.fill_input(self.name_path, name)

    def fill_last_name(self, last_name):
        self.fill_input(self.last_name_path, last_name)

    def fill_nickanme(self, nickname):
        self.fill_input(self.nickname_path, nickname)

    def fill_city(self, city):
        self.fill_city_input(self.city_path, city)
        if city != "":
            self.click_on_popup_el_if_popup_exist(self.accept_city_popup)

    def collect_errors(self) -> InputAnnotationsErrors:
        """
        :return: Возвращает структуру с ошибками в процессе заполнения формы
        """
        name_err = self.get_element_text(self.name_err_path)
        last_name_err = self.get_element_text(self.last_name_err_path)
        nickname_err = self.get_element_text(self.nickname_err_path)
        city_err = self.get_element_text(self.city_err_path)
        return InputAnnotationsErrors(name_err, last_name_err, nickname_err, city_err)

    def click_submit(self) -> InputAnnotationsErrors:
        btn = self.wait_until_and_get_elem_by_xpath(self.submit_btn_path)
        btn.click()
        return self.collect_errors()

    def check_if_uploaded(self):
        try:
            self.wait_until_and_get_elem_by_xpath(self.upload_process)
            self.wait_until_and_get_elem_by_xpath(self.photo_ready)
            return True
        except TimeoutException:
            return False

    def fill_city_input(self, city_path, city):
        """
        Так как pop up с выбором города очень тупой и использует React,
         мы будем ждать пока он раздуплиться, иначе просто не работает(я пытался)
        :param city_path:
        :param city:
        :return:
        """
        el = self.wait_until_and_get_elem_by_xpath(city_path)
        el.click()
        clear(el)
        time.sleep(2)
        el.send_keys(city)
        time.sleep(2)
        el.submit()
        time.sleep(2)
