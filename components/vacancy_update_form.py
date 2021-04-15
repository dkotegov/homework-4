from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent


class VacancyUpdateFormLocators:
    def __init__(self):
        self.root = "//div[@class='sum-form-wrap']"

        self.title = "//input[@id='summary-name']"
        self.description = '//textarea[@id="description"]'
        self.skills = '//textarea[@id="skills"]'
        self.requirements = '//textarea[@id="requirements"]'
        self.responsibilities = '//textarea[@id="duties"]'
        self.phone = '//input[@id="phone"]'
        self.address = '//input[@id="address"]'

        self.salary_min = '//input[@id="salary_min"]'
        self.salary_max = '//input[@id="salary_max"]'
        self.email = '//input[@id="email"]'

        self.submit = '//button[@id="send-form-empl"]'
        self.submit_delete = '//div[@id="deleteVacancy"]'
        self.browse_image_btn = '//input[@id="sum-img-load"]'

        self.error_title = '(//span[@class="error"])[1]'
        self.error_description = '(//span[@class="error"])[2]'
        self.error_skills = '(//span[@class="error"])[3]'
        self.error_requirements = '(//span[@class="error"])[4]'
        self.error_responsibilities = '(//span[@class="error"])[5]'

        self.error_salary = '(//span[@class="error"])[6]'

        self.error_phone = '(//span[@class="error"])[7]'
        self.error_place = '(//span[@class="error"])[9]'


class VacancyUpdateForm(BaseComponent):
    def __init__(self, driver):
        super(VacancyUpdateForm, self).__init__(driver)
        self.wait = WebDriverWait(self.driver, 10, 0.1)
        self.locators = VacancyUpdateFormLocators()

        self.error_message = 'Поле обязательно для заполнения.'
        self.error_message_email = 'Укажите email.'
        self.error_message_phone = 'Неверный номер телефона.'
        self.error_message_common = 'Что-то пошло не так. Попробуйте позже.'
        self.error_message_salary = ''

    def set_input(self, locator: str, data: str):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, locator))
        ).send_keys(data)

    def submit(self):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.submit))
        ).click()

    def wait_for_vacancy_page(self):
        self.wait.until(
            EC.url_matches("https://studhunt.ru/vacancy")
        )

    def is_error_input(self, locator: str, error_message):
        try:
            _ = self.wait.until(
                EC.text_to_be_present_in_element((By.XPATH, locator), error_message)
            )
            return True
        except (TimeoutException, AssertionError):
            return False

    def load_image(self):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.browse_image_btn))
        ).send_keys('test_data/big_img.png')

    def set_title(self, title: str):
        self.set_input(self.locators.title, title)

    def set_description(self, description: str):
        self.set_input(self.locators.description, description)

    def set_skills(self, skills: str):
        self.set_input(self.locators.skills, skills)

    def set_requirements(self, requirements: str):
        self.set_input(self.locators.requirements, requirements)

    def set_responsibilities(self, responsibilities: str):
        self.set_input(self.locators.responsibilities, responsibilities)

    def set_phone(self, phone: str):
        self.set_input(self.locators.phone, phone)

    def set_address(self, address: str):
        self.set_input(self.locators.address, address)

    def set_salary_min(self, salary: str):
        self.set_input(self.locators.salary_min, salary)

    def set_salary_max(self, salary: str):
        self.set_input(self.locators.salary_max, salary)

    def set_email(self, email: str):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.email))
        ).clear()
        self.set_input(self.locators.email, email)

    def submit_delete(self):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.submit_delete))
        ).click()

    @property
    def is_title_error(self):
        return self.is_error_input(self.locators.error_title, self.error_message)

    @property
    def is_description_error(self):
        return self.is_error_input(self.locators.error_description, self.error_message)

    @property
    def is_place_error(self):
        return self.is_error_input(self.locators.error_place, self.error_message)

    @property
    def is_skills_error(self):
        return self.is_error_input(self.locators.error_skills, self.error_message)

    @property
    def is_requirements_error(self):
        return self.is_error_input(self.locators.error_requirements, self.error_message)

    @property
    def is_resp_error(self):
        return self.is_error_input(self.locators.error_responsibilities, self.error_message)

    @property
    def is_phone_error(self):
        return self.is_error_input(self.locators.error_phone, self.error_message_phone)

    def is_salary_error(self, error_message):
        return self.is_error_input(self.locators.error_salary, error_message)

