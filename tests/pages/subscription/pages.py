from setup.constants import PROJECT_URL
from tests.conftest import accessor
from tests.pages.base.base_pages import BasePages


class Pages(BasePages):
    @staticmethod
    def open_actor_page(actor_id=1):
        accessor.get(f'{PROJECT_URL}actor?films&id={actor_id}')

    @staticmethod
    def find_actor_subscription_nowait(actor_id):
        locator = '.film-card__img a'
        accessor.find_element_by_css_selector(locator)

    @staticmethod
    def find_actor_subscription(actor_id):
        locator = '.film-card__img a'
        accessor.wait_for_load(css_locator=locator)
        link = accessor.find_element_by_css_selector(locator)
        assert link.element.get_attribute('href') == f'https://cinsear.ru/actor?films&id={actor_id}'

    @staticmethod
    def subscribe():
        button_selector = '.js-subscribe-button'
        accessor.wait_for_load(css_locator=button_selector)
        button = accessor.find_element_by_css_selector(button_selector)
        assert button.element.get_attribute('value').lower() == 'подписаться'
        button.click()

    @staticmethod
    def unsubscribe():
        button_selector = '.js-subscribe-button'
        accessor.wait_for_load(css_locator=button_selector)
        accessor.sleep(1)
        button = accessor.find_element_by_css_selector(button_selector)
        assert button.element.get_attribute('value').lower() == 'отписаться'
        button.click()
