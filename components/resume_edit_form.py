from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from components.resume_create_form import ResumeCreateForm
from components.resume_create_form import ResumeCreateFormLocators


class ResumeEditFormLocators(ResumeCreateFormLocators):
    def __init__(self):
        super().__init__()
        self.root = '//div[text()="Редактирование резюме"]'

        self.submit = '//button[text()="Сохранить"]'
        self.delete_exp_btn = '//div[@class="job__delete"]'


class ResumeEditForm(ResumeCreateForm):
    def __init__(self, driver):
        super(ResumeEditForm, self).__init__(driver)
        self.locators = ResumeEditFormLocators()

        self.error_message_input = 'Поле обязательно для заполнения.'
        self.error_message_email = 'Укажите email.'
        self.error_message_common = 'Что-то пошло не так. Попробуйте позже.'

    def clear_inputs(self):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.description))
        ).clear()
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.place))
        ).clear()
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.skills))
        ).clear()

    def delete_experience(self):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.delete_exp_btn))
        ).click()

