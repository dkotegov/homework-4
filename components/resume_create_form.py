from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent


class ResumeCreateForm(BaseComponent):
    TITLE = "//*[@id='title']"
    DESCRIPTION = '//textarea[@id="description"]'
    PLACE = '//input[@id="place"]'
    SKILLS = '//textarea[@id="skills"]'
    SUBMIT = '//button[@id="send-form-cand"]'

    def set_title(self, title: str):
        """
        Ввод названия в окне создания резюме
        :param title: название резюме
        """
        a = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.TITLE))
        )
        a.send_keys(title)

    def set_description(self, description: str):
        """
        Ввод описания в окне создания резюме
        :param description: описание резюме
        """
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.DESCRIPTION))
        ).send_keys(description)

    def set_place(self, place: str):
        """
        Ввод должности в окне создания резюме
        :param place: желаемая должность
        """
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.PLACE))
        ).send_keys(place)

    def set_skills(self, skills: str):
        """
        Ввод новыков в окне создания резюме
        :param skills: навыки
        """
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.SKILLS))
        ).send_keys(skills)

    def submit(self):
        """
        Завершает создание резюме
        """
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.SUBMIT))
        ).click()

    def wait_for_resume_page(self):
        """
        Ождидает пока не откроется страница резюме
        """
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.url_matches("https://studhunt.ru/resume")
        )
