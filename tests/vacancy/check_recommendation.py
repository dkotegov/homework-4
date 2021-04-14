import unittest

from pages.main_page import MainPage
from pages.vacancies_page import VacanciesPage
from pages.vacancy_page import VacancyPage
from scenario.auth import setup_auth, auth_as_employer_has_comp
from scenario.default_setup import default_setup
from scenario.registration_applicant import RegistrationApplicantScenario
from scenario.vacancy import VacancyScenario


class CheckRecommendations(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)
        self.PROFESSION = "Воспитатель"
        self.mainPage = MainPage(self.driver)
        self.vacanciesPage = VacanciesPage(self.driver)
        self.vacancyPage = VacancyPage(self.driver)
        self.mainPage.open()

    def test_vacancy_open_on_click(self):
        setup_auth(self)
        self.mainPage.click_recommendations()
        self.assertTrue(self.vacanciesPage.is_open())
        self.vacanciesPage.click_on_first_vacancy()
        self.assertTrue(self.vacancyPage.is_open())

    def tearDown(self):
        self.driver.quit()


class CheckRecommendationsCreate(unittest.TestCase):
    def setUp(self) -> None:
        default_setup(self)
        self.PROFESSION = "Воспитатель"
        self.mainPage = MainPage(self.driver)
        self.vacanciesPage = VacanciesPage(self.driver)
        self.vacancyPage = VacancyPage(self.driver)
        self.mainPage.open()
        self.Applicant = RegistrationApplicantScenario(self)
        self.data = self.Applicant.registration_applicant()

    def test_vacancy_equiv_on_click(self):
        self.mainPage.search_by_profession(self.PROFESSION)
        self.vacanciesPage.click_on_first_vacancy()
        name = self.vacancyPage.get_vacancy_name()
        self.mainPage.open()
        self.mainPage.click_recommendations()
        self.assertTrue(self.vacanciesPage.check_vacancies_exists_by_name(name))

    def tearDown(self):
        self.Applicant.delete_applicant()
        self.driver.quit()