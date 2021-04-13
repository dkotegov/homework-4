import components
from pages.base_page import BasePage
from components.company_create_form import CompanyCreateForm


class CreateCompanyPage(BasePage):
    PATH = 'createCompany'

    def __init__(self, driver):
        self.company_create_form = CompanyCreateForm(driver)
        super(CreateCompanyPage, self).__init__(driver, self.company_create_form.locators.root)

    @property
    def form(self) -> components.company_create_form:
        return CompanyCreateForm(self.driver)