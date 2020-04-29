from setup.constants import PROJECT_URL
from tests.conftest import accessor as a
from tests.pages.base.base_pages import BasePages
from selenium.webdriver.support.select import Select

AUTH_MODAL = 'a[href="/login"]'
LOGIN_LOGIN = '#js-email-login'
LOGIN_PASSWODR = '#js-password-login'

FILM_CONTENT = '.film'
FILM_YEAR = '[href^="/search?yarmin="]'
FILM_GENRE = '[href^="/search?genres="]'
FILM_COUNTRY = '[href^="/search?countries="]'
FILM_ACTOR = '[href^="/actor"]'
FILM_SAME = '[href^="/film?"]'
FILM_RATING = '.film__decription_main'

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

STAR_BUTTON = '#stars'
STAR_3 = 'i[data-index="2"]'


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

    def click_select(): 
        element = a.find_element_by_css_selector(LIST_SELECT)
        element.wait_and_click()

    def choose_new_list_option(): 
        element = a.find_element_by_css_selector(LIST_NEW_LIST)
        element.wait_and_click()

    def set_list_name(name): 
        element = a.find_element_by_css_selector(LIST_NEW_INPUT)
        element.wait_and_click()
        element.send_keys(name)

    def sumbit_list_create():
        a.wait_for_load(css_locator=LIST_NEW_SUBMIT)
        element = a.find_element_by_css_selector(LIST_NEW_SUBMIT)
        element.wait_and_click()

    def cancel_list_create():
        a.wait_for_load(css_locator=LIST_NEW_CANCEL)
        element = a.find_element_by_css_selector(LIST_NEW_CANCEL)
        element.wait_and_click()

    def get_current_list():
        a.wait_for_load(css_locator=LIST_SELECT)
        element = a.find_element_by_css_selector(LIST_SELECT)
        select = Select(element.element)
        selected_option = select.first_selected_option
        return selected_option.text

    def click_year():
        element = a.find_element_by_css_selector(FILM_YEAR)
        element.wait_and_click()

    def click_genre():
        element = a.find_element_by_css_selector(FILM_GENRE)
        element.wait_and_click()

    def click_actor():
        element = a.find_element_by_css_selector(FILM_ACTOR)
        element.wait_and_click()

    def click_COUNTRY():
        element = a.find_element_by_css_selector(FILM_COUNTRY)
        element.wait_and_click()

    def click_star():
        element = a.find_element_by_css_selector(STAR_3)
        element.wait_and_click()

    def click_same_film():
        element = a.find_element_by_css_selector(FILM_SAME)
        element.wait_and_click()

    def check_stars(): 
        element = a.find_element_by_css_selector(STAR_BUTTON)

    def get_film_rating():
        element = a.find_element_by_css_selector(FILM_RATING)
        rating_line = element.get_text()
        rating = rating_line.split(' ')[1]
        return rating

