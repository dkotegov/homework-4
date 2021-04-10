from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent


class ResumeCreateFormLocators:
    def __init__(self):
        self.root = "//div[@class='sum-form-wrap']"
        self.title = "//*[@id='title']"
        self.description = '//textarea[@id="description"]'
        self.place = '//input[@id="place"]'
        self.skills = '//textarea[@id="skills"]'
        self.submit = '//button[@id="send-form-cand"]'


class ResumeCreateForm(BaseComponent):
    def __init__(self, driver):
        super(ResumeCreateForm, self).__init__(driver)
        self.wait = WebDriverWait(self.driver, 30, 0.1)
        self.locators = ResumeCreateFormLocators()

    def set_title(self, title: str):
        """
        Ввод названия в окне создания резюме
        :param title: название резюме
        """
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.title))
        ).send_keys(title)

    def set_description(self, description: str):
        """
        Ввод описания в окне создания резюме
        :param description: описание резюме
        """
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.description))
        ).send_keys(description)

    def set_place(self, place: str):
        """
        Ввод должности в окне создания резюме
        :param place: желаемая должность
        """
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.place))
        ).send_keys(place)

    def set_skills(self, skills: str):
        """
        Ввод новыков в окне создания резюме
        :param skills: навыки
        """
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.skills))
        ).send_keys(skills)

    def submit(self):
        """
        Завершает создание резюме
        """
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.submit))
        ).click()

    def wait_for_resume_page(self):
        """
        Ождидает пока не откроется страница резюме
        """
        self.wait.until(
            EC.url_matches("https://studhunt.ru/resume")
        )
