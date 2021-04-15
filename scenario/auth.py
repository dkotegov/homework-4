from pages.auth_page import AuthPage


def setup_auth(test, data=None) -> bool:
    if data is None:
        data = {
            'EMAIL': test.EMAIL_APPL,
            'PASSWORD': test.PASSWORD_APPL
        }
    auth_page = AuthPage(test.driver)
    auth_page.open()

    auth_form = auth_page.auth_form
    auth_form.set_email(data['EMAIL'])
    auth_form.set_password(data['PASSWORD'])
    auth_form.submit()
    return auth_form.wait_for_mainpage()


def setup_auth_failed(test, data=None):
    if data is None:
        data = {
            'EMAIL': test.EMAIL_APPL,
            'PASSWORD': test.PASSWORD_APPL
        }
    auth_page = AuthPage(test.driver)
    auth_page.open()

    auth_form = auth_page.auth_form
    auth_form.set_email(data['EMAIL'])
    auth_form.set_password(data['PASSWORD'])
    auth_form.submit()


def auth_as_applicant(test):
    data = {
        'EMAIL': test.EMAIL_APPL,
        'PASSWORD': test.PASSWORD_APPL,
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


def auth_as_employer_has_no_comp(test):
    auth_page = AuthPage(test.driver)
    auth_page.open()

    auth_form = auth_page.auth_form
    auth_form.set_email(test.EMAIL_EMPL)
    auth_form.set_password(test.PASSWORD_EMPL)
    auth_form.submit()
    auth_form.wait_for_mainpage()


def auth_as_employer_has_comp(test):
    auth_page = AuthPage(test.driver)
    auth_page.open()

    auth_form = auth_page.auth_form
    auth_form.set_email(test.EMAIL_EMPL_COMP)
    auth_form.set_password(test.PASSWORD_EMPL_COMP)
    auth_form.submit()
    auth_form.wait_for_mainpage()
