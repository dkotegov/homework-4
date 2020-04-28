from setup.constants import PROJECT_URL
from tests.conftest import accessor as a


class BaseSteps:
    @staticmethod
    def open_site():
        a.driver.get(PROJECT_URL)
