

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
            'name': name,
            'surname': surname,
            'email': email,
            'password': password,
            'confirm_password': password,
        }

    registration_page = RegistrationPage(test.driver)
    registration_page.open()

    registration_form = registration_page.registration_form

    registration_form.click_checkout_btn()

    if not select_company:
        registration_form.select_checkbox()
    else:
        if registration_page.select_company():
            registration_form.select_checkbox()

    registration_page.set_data(data)
    registration_form.submit()
    registration_form.wait_for_mainpage()

    return data

