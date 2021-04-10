from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from components.base_component import BaseComponent


class NavbarLocators:
    def __init__(self):
        self.vacancies_btn = '//a[@href="/employersList"]'
        self.resumes_btn = '//a[@href="/candidatesList"]'
        self.companies_btn = '//a[@href="/companiesList"]'
        self.mainpage_btn = '//a[@href="/"]'
        self.registration_btn = '//a[@href="/reg"]'
        self.auth_btn = '//a[@href="/auth"]'
        self.profile_btn = '//a[@href="/profile"]'
        self.chats_btn = '//a[@href="/chats"]'
        self.logout_btn = '//a[@href="/logout"]'
        self.notification_btn = '//a[@id="note-button"]'
        self.recommendation_btn = '//a[@href="/recommendations"]'


class NavbarForm(BaseComponent):
    def __init__(self, driver):
        super(NavbarForm, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = NavbarLocators()

    def click_on_vacancies(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.vacancies_btn)))
        element.click()

    def click_on_resumes(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.resumes_btn)))
        element.click()

    def click_on_companies(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.companies_btn)))
        element.click()

    def click_on_logo(self):
        mainpage = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.mainpage_btn))
        )
        mainpage.click()

    def click_on_registration(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.registration_btn)))
        element.click()

    def click_on_profile(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.profile_btn)))
        element.click()

    def click_on_auth(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.auth_btn)))
        element.click()

    def click_on_notification(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.notification_btn)))
        element.click()

    def click_on_chats(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.chats_btn)))
        element.click()

    def click_on_logout(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.logout_btn)))
        element.click()

    def click_on_recommendation(self):
        element = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.locators.recommendation_btn)))
        element.click()
