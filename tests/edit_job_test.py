import unittest
import os
from selenium.webdriver import DesiredCapabilities, Remote

from config import HUB_ADDRESS
from pages.pages import JobPage, CreateJobPage
from steps.steps import AuthStep, JobSteps


class EditJobTest(unittest.TestCase):
    USEREMAIL = os.environ['USEREMAIL']
    PASSWORD = os.environ['PASSWORD']
    JOB_TITLE = 'old title'
    NEW_TITLE = 'new title'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor=HUB_ADDRESS,
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth = AuthStep(self.driver)
        auth.login(self.USEREMAIL, self.PASSWORD)

        job = JobSteps(self.driver)
        job.create(self.JOB_TITLE)

    def tearDown(self):
        self.driver.quit()

    def test_edit_success(self):
        page = JobPage(self.driver)
        page.open_edit_form()

        form = page.form

        form.get_header('Редактирование работы')

        form.set_title(self.NEW_TITLE)
        form.submit()

        page.get_job_title(self.NEW_TITLE)
