import random
import string

from pages.profile_page import ProfilePage
from pages.registration_page import RegistrationPage


def registration_applicant(test, data=None):
    if data is None:
        name = ''.join(random.choice(string.ascii_letters) for i in range(10))
        surname = ''.join(random.choice(string.ascii_letters) for i in range(10))
        email = (''.join(random.choice(string.ascii_letters) for i in range(10))) + '@mail.ru'
        password = ''.join(random.choice(string.ascii_letters) for i in range(10))
        data = {
            'NAME': name,
            'SURNAME': surname,
            'EMAIL': email,
            'PASSWORD': password,
            'CONFIRM_PASSWORD': password,
        }

    registration_page = RegistrationPage(test.driver)
    registration_page.open()

    registration_page.set_data(data)
    registration_page.wait_for_reg_is_done()

    return data

class RegistrationApplicantScenario:
    def __init__(self, test):
        self.test = test
        self.name = ''.join(random.choice(string.ascii_letters) for i in range(10))
        self.surname = ''.join(random.choice(string.ascii_letters) for i in range(10))
        self.email = (''.join(random.choice(string.ascii_letters) for i in range(10))) + '@mail.ru'
        self.password = ''.join(random.choice(string.ascii_letters) for i in range(10))
        self.data = {
            'NAME': self.name,
            'SURNAME': self.surname,
            'EMAIL': self.email,
            'PASSWORD': self.password,
            'CONFIRM_PASSWORD': self.password,
        }


    def registration_applicant(self, data=None):

        registration_page = RegistrationPage(self.test.driver)
        registration_page.open()

        registration_page.set_data(self.data)
        registration_page.wait_for_reg_is_done()

        return self.data

    def delete_applicant(self):
        profile_page = ProfilePage(self.test.driver)
        profile_page.open()
        profile_page.delete_account()
