import unittest

from pages.main_page import MainPage
from setup.default_setup import default_setup


class Navbar(unittest.TestCase):

    def setUp(self) -> None:
        default_setup(self)

        self.page = MainPage(self.driver)
        self.page.open()

    # def test_vacancy_link(self):
    #     self.page.check_open_vac_list()
    #
    # def test_resume_link(self):
    #     self.page.check_open_res_list()
    #
    # def test_company_link(self):
    #     self.page.check_open_comp_list()

    def test_mainpage_link(self):
        self.page.check_open_comp_list()
        self.page.check_open_mainpage()

