from pages.pages import AuthPage, CreateJobPage, JobPage
from utils.wait import Waiter


class Step(object):

    def __init__(self, driver):
        self.driver = driver


class AuthStep(Step):
    def login(self, username, password):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        form = auth_page.form
        form.set_login(username)
        form.set_password(password)
        form.submit()


class JobSteps(Step):
    def create(self, title = 'Название'):
        page = CreateJobPage(self.driver)
        page.open_form()

        form = page.form
        form.set_type()
        form.set_title(title)
        form.set_description("Описание достаточно длинное для удобвлетворения требований")
        form.set_category()
        form.set_country()
        form.set_tag("javascript")
        form.set_budget("100")
        form.set_level()
        form.set_spec()
        form.set_city()

        form.submit()


