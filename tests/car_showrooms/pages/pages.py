import urlparse

from tests.car_showrooms.pages.components import AddShowroomForm, ShowroomList, SpecialOffersList, SearchForm


class ShowroomPage(object):
    BASE_URL = 'https://cars.mail.ru/dealers/msk'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    @property
    def search_form(self):
        return SearchForm(self.driver)

    @property
    def showroom_list(self):
        return ShowroomList(self.driver)

    @property
    def special_offers_list(self):
        return SpecialOffersList(self.driver)

    @property
    def add_showroom_form(self):
        return AddShowroomForm(self.driver)
