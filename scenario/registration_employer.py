

import random
import string

from pages.registration_page import RegistrationPage


def registration_employer(test, select_company, data=None):
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

    registration_page.click_checkout_btn()

    if not select_company:
        registration_page.click_to_checkbox()
    else:
        if registration_page.select_company():
            registration_page.click_to_checkbox()

    registration_page.set_data(data)
    registration_page.wait_for_reg_is_done()
    return data

