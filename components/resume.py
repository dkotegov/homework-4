from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


from components.base_component import BaseComponent


class ResumeFormLocators:
    def __init__(self):
        self.root = "//div[@class='cand-options']"

        self.description = "//div[text()='Подробная информация']/following-sibling::div"
        self.place = "//div[@class='about-candidate']/div[2]"
        self.skills = "//div[text()='Персональные навыки']/following-sibling::div"
        self.salary = "(//div[@class='inline-icon-desc__body'])[1]"
        self.position = '//span[@class="work-position"]'
        self.name_job = '//span[@class="name-company"]'

        self.response_btn = '(//div[@id="responseResumeBtn"])'
        self.vacancy_select_popup = '//div[@class="popUp-main"]'
        self.first_vacation = '(//div[@class="list-row"])[1]'
        self.response_done = '//div[@class="response__done"]'

        self.favorite_btn = '(//div[@class="cand-options-contact"])/div[1]'


class ResumeForm(BaseComponent):
    def __init__(self, driver):
        super(ResumeForm, self).__init__(driver)
        self.wait = WebDriverWait(self.driver, 30, 0.1)
        self.locators = ResumeFormLocators()

    def wait_for_resume_page(self):
        self.wait.until(
            EC.url_matches("https://studhunt.ru/resume")
        )

    def add_to_response(self):
        self.click_locator(self.locators.response_btn)

    def add_to_favorite(self):
        self.click_locator(self.locators.favorite_btn)

    def get_text_favorite_btn(self):
        self.wait.until(EC.element_to_be_clickable((
            By.XPATH, self.locators.favorite_btn))
        )
        return self.get_field(self.locators.favorite_btn)

    def get_description(self) -> str:
        return self.wait.until(
            lambda d: d.find_element_by_xpath(self.locators.description)
        ).text

    def get_place(self) -> str:
        return self.wait.until(
            lambda d: d.find_element_by_xpath(self.locators.place)
        ).text

    def get_skills(self) -> str:
        return self.wait.until(
            lambda d: d.find_element_by_xpath(self.locators.skills)
        ).text

    def get_salary(self) -> []:
        salary = self.wait.until(
            lambda d: d.find_element_by_xpath(self.locators.salary)
        ).text
        return salary.split('-')

    def get_position(self) -> []:
        return self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.position))
        )

    def get_name_job(self) -> []:
        return self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.name_job))
        )

    def response(self):
        self.click_locator(self.locators.response_btn)
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.vacancy_select_popup))
        )
        data = self.get_field(self.locators.first_vacation)
        self.click_locator(self.locators.first_vacation)
        return data

    def get_response_done(self):
        text = self.get_field(self.locators.response_done)
        self.click_locator(self.locators.response_done)
        return text

