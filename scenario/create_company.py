import uuid

from pages.create_company_page import CreateCompanyPage


def create_company(test, data=None) -> None:

    if data is None:
        data = {
            'title': 'comp№' + str(uuid.uuid4()),
            'description': 'Some descriptions',
        }
    create_company_page = CreateCompanyPage(test.driver)
    create_company_page.open()

    create_company_form = create_company_without_submit(create_company_page.form, data)
    create_company_form.submit()
    create_company_form.wait_for_company_page()


def create_company_without_submit(create_company_form, data):
    create_company_form.set_title(data['title'])
    create_company_form.set_description(data['description'])
    return create_company_form
