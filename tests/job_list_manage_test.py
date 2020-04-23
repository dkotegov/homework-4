import unittest
import os

from selenium.webdriver import DesiredCapabilities, Remote

from config import HUB_ADDRESS
from pages.pages import JobPage, CreateJobPage, JobListPage
from steps.steps import AuthStep, JobSteps


class JobListManageTest(unittest.TestCase):
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

        page = JobListPage(self.driver)
        page.open()
        item = page.item

        text = item.get_toggle_text()
        item.toggle_publish()
        if text == publish:
            item.check_toggle(close)
            self.assertEqual(close, item.get_toggle_text())
        elif text == close:
            item.check_toggle(publish)
            self.assertEqual(publish, item.get_toggle_text())

    def test_delete(self):
        page = JobListPage(self.driver)
        page.open()

        item = page.item
        item.delete()





