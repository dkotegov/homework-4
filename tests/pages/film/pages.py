from setup.constants import PROJECT_URL
from tests.conftest import accessor as a
from tests.pages.base.base_pages import BasePages

AUTH_MODAL = 'a[href="/login"]'
LOGIN_LOGIN = '#js-email-login'
LOGIN_PASSWODR = '#js-password-login'

FILM_CONTENT = '.film'
FILM_YEAR = '[href^="/search?yarmin="]'
FILM_GENRE = '[href^="/search?genres="]'
FILM_COUNTRY = '[href^="/search?countries="]'
FILM_ACTOR = '[href^="/actor"]'

REVIEWS = '.feedback'
REVIEW_BODY_INPUT = '.js-text-input'
REVIEW_TITLE_INPUT = '.js-title-input'
REVIEW_SUBMIT = '[id="js-review-button"]'
REVIEW_BODY =  '.feedback__main div:nth-child(3)'
REVIEW_TITLE = '.feedback__main div:nth-child(2)'

LIST_SELECT = '.js-select'
LIST_SELECTED = '.js-select [selected="true"]'
LIST_NEW_LIST = '[value="new_list"]'
LIST_NEW_INPUT = '#js-list-input'
LIST_NEW_SUBMIT = '#js-create-list'
LIST_NEW_CANCEL = '#js-stop-create'


class Pages(BasePages):
    
    @staticmethod
    def check_film_content():
        a.wait_for_load(css_locator=FILM_CONTENT)

    def set_review_title( title):
        a.wait_for_load(css_locator=REVIEW_TITLE_INPUT)
        element = a.find_element_by_css_selector(REVIEW_TITLE_INPUT)
        element.wait_and_click()
        element.send_keys(title)

    def set_review_body(body):
        a.wait_for_load(css_locator=REVIEW_BODY_INPUT)
        element = a.find_element_by_css_selector(REVIEW_BODY_INPUT)
        element.wait_and_click()
        element.send_keys(body)
    
    def submit_review():
        element = a.find_element_by_css_selector(REVIEW_SUBMIT)
        element.click()

    def get_first_review_body():
        a.wait_for_load(css_locator=REVIEW_BODY)
        element = a.find_element_by_css_selector(REVIEW_BODY)
        return element.get_text()

    def get_first_review_title():
        a.wait_for_load(css_locator=REVIEW_TITLE)
        element = a.find_element_by_css_selector(REVIEW_TITLE)
        return element.get_text()
