import unittest
import os

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote

from config import HUB_ADDRESS
from pages.pages import JobPage, CreateJobPage
from steps.steps import AuthStep, JobSteps


class CreateJobTest(unittest.TestCase):
    USEREMAIL = os.environ['USEREMAIL']
    PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor=HUB_ADDRESS,
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth = AuthStep(self.driver)
        auth.login(self.USEREMAIL, self.PASSWORD)

    def tearDown(self):
        self.driver.quit()

    def test_success(self):
        title = "Название заказа. Selenium"

        job = JobSteps(self.driver)
        job.create(title)

        job = JobPage(self.driver)
        job.get_job_title(title)

    def test_budget(self):
        page = CreateJobPage(self.driver)
        page.open_form()

        err = 'Выберите значение не больше 1000000.'
        form = page.form
        form.set_budget("10000000")
        form.submit()
        self.assertEqual(form.get_budget_error(), err)

    def test_tags(self):
        page = CreateJobPage(self.driver)
        page.open_form()

        form = page.form
        tags_extra = "js,css,qa,android,python,extra,fields"
        tags = "js,css,qa,android,python"
        form.set_tag(tags_extra)
        self.assertEqual(form.get_form_tags(), tags)

    def test_empty(self):
        page = CreateJobPage(self.driver)
        page.open_form()

        err = 'Заполните пожалуйста это поле'
        form = page.form
        form.submit()
        self.assertEqual(form.get_title_error(), err)


