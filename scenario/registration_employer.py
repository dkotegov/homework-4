import random
import string

from pages.registration_page import RegistrationPage


class RegistrationEmployerScenario:
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

    def registration_employer(self, select_company=None, data=None):

        registration_page = RegistrationPage(self.test)
        registration_page.open()

        registration_page.click_checkout_btn()

        if not select_company:
            registration_page.click_to_checkbox()
        else:
            if registration_page.select_company():
                registration_page.click_to_checkbox()

        registration_page.set_data(self.data)
        registration_page.wait_for_reg_is_done()
        return data
