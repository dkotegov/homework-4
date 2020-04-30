from tests.pages.lists.pages import Pages
from tests.steps.base.base_steps import BaseSteps


class Steps(BaseSteps):
    @staticmethod
    def select_list(list_name):
        Pages.select_list(list_name)

    @staticmethod
    def create_list(list_name):
        Steps.select_list('новый список')
        Pages.enter_new_list_name(list_name)
        Pages.save_new_list()
