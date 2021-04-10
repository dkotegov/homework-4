import random
import string

from pages.registration_page import RegistrationPage


def registration_applicant(test, data=None):
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
    registration_form.set_name(data['name'])
    registration_form.set_surname(data['surname'])
    registration_form.set_email(data['email'])
    registration_form.set_password(data['password'])
    registration_form.set_confirm_password(data['confirm_password'])
    registration_form.submit()
    registration_form.wait_for_mainpage()

    return data

