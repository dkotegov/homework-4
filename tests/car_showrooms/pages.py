import urlparse


class ShowroomPage(object):
    BASE_URL = 'https://cars.mail.ru/dealers/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    @property
    def regions_selection_form(self):
        from tests.car_showrooms.search_showroom_tests import RegionSelectionForm
        return RegionSelectionForm(self.driver)

    @property
    def showroom_list(self):
        from tests.car_showrooms.list_showroom_test import ShowroomList
        return ShowroomList(self.driver)


class Component(object):
    def __init__(self, driver):
        self.driver = driver