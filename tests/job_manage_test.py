import unittest
import os
from selenium.webdriver import DesiredCapabilities, Remote

from config import HUB_ADDRESS
from pages.pages import JobPage, CreateJobPage
from steps.steps import AuthStep, JobSteps


class JobManageTest(unittest.TestCase):
    USEREMAIL = os.environ['USEREMAIL']
    PASSWORD = os.environ['PASSWORD']
    JOB_TITLE = 'this is a test job'

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

    def test_publish(self):
        publish = 'Опубликовать'
        close = 'Закрыть'

        page = JobPage(self.driver)

        text = page.get_toggle_text()
        page.toggle_publish()
        if text == publish:
            page.check_toggle(close)
            self.assertEqual(close, page.get_toggle_text())
        elif text == close:
            page.check_toggle(publish)
            self.assertEqual(publish, page.get_toggle_text())


