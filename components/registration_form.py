
from components.base_component import BaseComponent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class RegistrationFormLocators:
    def __init__(self):
        self.root = '//div[@class="main-page"]'
        self.auth_link = '//a[@href="/auth"]'
        self.page_title = '//div[@class="page-name page-name_small page-name_reg"]'

        self.checkout_btn = '//div[@data-value="Работодатель"]'
        self.checkbox_btn = '//input[@id="regCheckbox"]'
        self.select_company_btn = '//div[@class="dropbtn"]'
        self.company_list = '//div[@class="dropdown-content__div"]'

        self.name_field = '//input[@id="firstNameReg"]'
        self.surname_field = '//input[@id="lastNameReg"]'
        self.email_field = '//input[@id="emailReg"]'
        self.password_field = '//input[@id="passwReg"]'
        self.password2_field = '//input[@id="passwReg2"]'
        self.submit_btn = '//button[@class="input-data-card__enter-btn"]'

        self.profile_btn = '//a[@href="/profile"]'

        self.errors_list = '//span[@class="error"]'
        self.top_error = '//div[@class="error error_limit-width error_center"]'




class RegistrationForm(BaseComponent):
    def __init__(self, driver):
        super(RegistrationForm, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)

        self.locators = RegistrationFormLocators()

    def click_to_auth_href(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.auth_link))
        )
        element.click()

    def is_open(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.locators.page_title)))
            return True
        except:
            return False

    def click_select_company_btn(self):
        select_company_btn = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.select_company_btn))
        )
        select_company_btn.click()

    def choose_company(self):
        company_list = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.company_list))
        )
        if len(company_list) > 0:
            company_list[0].click()
            return True
        else:
            return False

    def select_checkbox(self):
        checkbox = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.checkbox_btn))
        )
        checkbox.click()

    def click_checkout_btn(self):
        checkout_btn = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.checkout_btn))
        )
        checkout_btn.click()

    def set_name(self, name: str):
        user_name = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.name_field))
        )
        user_name.send_keys(name)

    def set_surname(self, surname: str):
        user_surname = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.surname_field))
        )
        user_surname.send_keys(surname)

    def set_email(self, email: str):
        user_email = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.email_field))
        )
        user_email.send_keys(email)

    def set_password(self, pwd: str):
        password = WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.locators.password_field))
        )
        password.send_keys(pwd)

    def set_confirm_password(self, pwd: str):
        password = WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.locators.password2_field))
        )
        password.send_keys(pwd)

    def submit(self):
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.submit_btn))
        )
        submit.click()

    def wait_for_mainpage(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.locators.profile_btn)
        )

    def all_errors(self):
        return self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.errors_list)))

    def top_error(self):
        return self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.top_error)))[0]