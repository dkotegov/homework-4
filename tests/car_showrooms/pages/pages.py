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
    def search_form(self):
        from tests.car_showrooms.search_showroom_tests import SearchForm
        return SearchForm(self.driver)

    @property
    def showroom_list(self):
        from tests.car_showrooms.list_showroom_test import ShowroomList
        return ShowroomList(self.driver)

    @property
    def special_offers_list(self):
        from tests.car_showrooms.list_special_offers_test import SpecialOffersList
        return SpecialOffersList(self.driver)

    @property
    def add_showroom_form(self):
        from tests.car_showrooms.add_showroom_test import AddShowroomForm
        return AddShowroomForm(self.driver)


class Component(object):
    def __init__(self, driver):
        self.driver = driver
