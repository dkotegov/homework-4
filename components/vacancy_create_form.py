from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent


class VacancyCreateFormLocators:
    def __init__(self):
        self.root = "//div[@class='sum-form-wrap']"

        self.list_mine = "//div[@class='list-row-description__name']//a"
        self.list_vac = "//div[@class='list-row-description__name']//a"
        self.title = "//input[@id='summary-name']"
        self.title_text = "//div[@class='describe-employer__vac-name']"
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
        self.browse_image_btn = '//input[@id="sum-img-load"]'


        self.error_title = '(//span[@class="error"])[1]'
        self.error_description = '(//span[@class="error"])[2]'
        self.error_skills = '(//span[@class="error"])[3]'
        self.error_requirements = '(//span[@class="error"])[4]'
        self.error_responsibilities = '(//span[@class="error"])[5]'
        self.error_salary = '(//span[@class="error"])[6]'
        self.error_phone = '(//span[@class="error"])[7]'
        self.error_email = '(//span[@class="error"])[8]'
        self.error_place = '(//span[@class="error"])[9]'
        self.error_server = '(//span[@class="error"])[10]'



class VacancyCreateForm(BaseComponent):
    def __init__(self, driver):
        super(VacancyCreateForm, self).__init__(driver)
        self.wait = WebDriverWait(self.driver, 10, 0.1)
        self.locators = VacancyCreateFormLocators()

        self.error_message = 'Поле обязательно для заполнения.'
        self.error_message_email = 'Укажите email.'
        self.error_message_phone = 'Неверный номер телефона.'
        self.error_message_common = 'Что-то пошло не так. Попробуйте позже.'

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

    def is_text_in_input(self, locator: str, expected_text):
        try:
            _ = self.wait.until(
                EC.text_to_be_present_in_element((By.XPATH, locator), expected_text)
            )
            return True
        except (TimeoutException, AssertionError):
            return False

    def get_element_text(self, locator):
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, locator))
        )
        return self.driver.find_element_by_xpath(locator).text

    def get_elements_text(self, locator):
        elements_list = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, locator))
        )
        return [e.text for e in elements_list]

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

    def check_vacancy_exist(self, vacancy_title) -> bool:
        vac_titles = self.get_elements_text(self.locators.list_mine)
        return vacancy_title in vac_titles

    def check_vacancy_in_list_exist(self, vacancy_title) -> bool:
        vac_titles = self.get_vacancies_in_list_titles()
        return vacancy_title in vac_titles

    def get_vacancies_in_list_titles(self):
        return self.get_elements_text(self.locators.list_vac)

    def open_by_title(self, vac_title):
        links = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.list_vac))
        )
        for link in links:
            if link.text == vac_title:
                link.click()
                break

    @property
    def get_title(self) -> str:
        return self.get_element_text(self.locators.title_text)

    @property
    def is_title_error(self):
        return self.is_text_in_input(self.locators.error_title, self.error_message)

    @property
    def is_description_error(self):
        return self.is_text_in_input(self.locators.error_description, self.error_message)

    @property
    def is_place_error(self):
        return self.is_text_in_input(self.locators.error_place, self.error_message)

    @property
    def is_skills_error(self):
        return self.is_text_in_input(self.locators.error_skills, self.error_message)

    @property
    def is_requirements_error(self):
        return self.is_text_in_input(self.locators.error_requirements, self.error_message)

    @property
    def is_resp_error(self):
        return self.is_text_in_input(self.locators.error_responsibilities, self.error_message)

    @property
    def is_phone_error(self):
        return self.is_text_in_input(self.locators.error_phone, self.error_message_phone)

    @property
    def is_email_error(self):
        return self.is_text_in_input(self.locators.error_email, self.error_message_email)

    def is_salary_error(self, error_message):
        return self.is_text_in_input(self.locators.error_salary, error_message)

    def is_server_error(self, error_message):
        return self.is_text_in_input(self.locators.error_server, error_message)
