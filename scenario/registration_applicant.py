import random
import string

from pages.profile_page import ProfilePage
from pages.registration_page import RegistrationPage


class RegistrationApplicantScenario:
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

    def __init__(self, test):
        self.test = test

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
