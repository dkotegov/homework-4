from pages.auth_page import AuthPage


def setup_auth(test, data=None) -> bool:
    if data is None:
        data = {
            'EMAIL': test.EMAIL,
            'PASSWORD': test.PASSWORD
        }
    auth_page = AuthPage(test.driver)
    auth_page.open()

    auth_form = auth_page.auth_form
    auth_form.set_email(data['EMAIL'])
    auth_form.set_password(data['PASSWORD'])
    auth_form.submit()
    if data['EMAIL'] == test.EMAIL and data['PASSWORD'] == test.PASSWORD:
        return auth_form.wait_for_mainpage()
    return True


def auth_as_applicant(test):
    data = {
        'EMAIL': 'margot@margot.ru',
        'PASSWORD': 'margot',
        'NAME': 'margot',
        'SURNAME': 'margot',
        'PHONE': '12345678910'
    }
    auth_page = AuthPage(test.driver)
    auth_page.open()

    auth_form = auth_page.auth_form
    auth_form.set_email(data['EMAIL'])
    auth_form.set_password(data['PASSWORD'])
    auth_form.submit()
    auth_form.wait_for_mainpage()
    return data


def auth_as_employer_no_comp(test):
    data = {
        'EMAIL': 'testEmaployer@testEmaployer.ru',
        'PASSWORD': 'testEmaployer'
    }
    auth_page = AuthPage(test.driver)
    auth_page.open()

    auth_form = auth_page.auth_form
    auth_form.set_email(data['EMAIL'])
    auth_form.set_password(data['PASSWORD'])
    auth_form.submit()
    auth_form.wait_for_mainpage()


def auth_as_employer_has_comp(test):
    data = {
        'EMAIL': 'employer@employer.ru',
        'PASSWORD': 'employer'
    }
    auth_page = AuthPage(test.driver)
    auth_page.open()

    auth_form = auth_page.auth_form
    auth_form.set_email(data['EMAIL'])
    auth_form.set_password(data['PASSWORD'])
    auth_form.submit()
    auth_form.wait_for_mainpage()
