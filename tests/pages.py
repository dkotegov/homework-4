# -*- coding: utf-8 -*-
import urlparse

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class Page(object):
    BASE_URL = 'http://msk.realty.mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class SalePage(Page):
    PATH = '/sale/living/'

    @property
    def offer(self):
        return PageOffer(self.driver)


class PageOffer(SalePage):
    CLASS_TITLE = 'p-instance__title'
    ADD_BTN = '//div[@data-module="Favorites"]'
    ICON = '//div[@data-module="Favorites"]//i[@class="icon_color_project"]'
    OFFER_ID = ''

    def open(self, offer_num=0):
        super(PageOffer, self).open()
        title_links = self.driver.find_elements_by_class_name(self.CLASS_TITLE)
        link = title_links[offer_num].get_attribute('href')
        self.driver.get(link)

    @property
    def slider(self):
        return Slider(self.driver)

    def add_to_favourites(self):
        button = self.driver.find_element_by_xpath(self.ADD_BTN)
        self.set_offer_id()
        button.click()
        try:
            icon = WebDriverWait(self.driver, 2, 0.1).until(
                lambda d: d.find_element_by_xpath(self.ICON)
            )
        except TimeoutException:
            pass


    def set_offer_id(self):
        button = self.driver.find_element_by_xpath(self.ADD_BTN)
        self.OFFER_ID = button.get_attribute('data-uid')

    def get_offer_id(self):
        return self.OFFER_ID


class FavouritesPage(Page):
    PATH = 'https://pro.realty.mail.ru/favorites/'
    LINK = '//span[@bem-id="234"]'
    DROPDOWN_CLASS = '//span[@bem-id="247"]/a/span'
    DELETE_BTN = '//a[@title="Удалить"]'

    def open(self):
        self.driver.get(self.PATH)      # здесь PATH строится не на основе базового, поэтому метод open переопределяем
        self.driver.maximize_window()

    @property
    def offer(self):
        return PageOffer(self.driver)

    def get_count(self):
        btns = self.driver.find_elements_by_xpath(self.DELETE_BTN)
        return len(btns)

    def clear_list(self):
        while self.driver.find_elements_by_xpath(self.DELETE_BTN):
            f_item = FavouriteItem(self.driver)
            f_item.open()
            check_page = PageOffer(self.driver)
            check_page.add_to_favourites()
            self.open()


class FavouriteItem(FavouritesPage):
    CLASS_TITLE = 'offers_list__content__address'

    def open(self, offer_num=0):
        super(FavouriteItem, self).open()
        title_links = self.driver.find_elements_by_class_name(self.CLASS_TITLE)
        link = title_links[offer_num].get_attribute('href')
        self.driver.get(link)


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)


class AuthForm(Component):
    LOGIN = '//input[@name="Username"]'
    FORM_FRAME = '//iframe[@class="ag-popup__frame__layout__iframe"]'
    PASSWORD = '//input[@name="Password"]'
    SUBMIT = '//button[@data-name="submit"]'
    LOGIN_BUTTON = '//a[text()="Вход"]'

    def open_form(self):
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(self.FORM_FRAME))

    def set_login(self, login):
        input = WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LOGIN)
        )
        input.send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class Slider(Component):
    OPEN_CLASS = 'photo__action'
    CLOSE_CLASS = 'viewbox__close'
    CLOSE_AREA = 'viewbox__cell'
    ICON_NEXT = 'icon_control_next'
    ICON_PREV = 'icon_control_previous'
    BOX_NEXT = 'viewbox__control_next'
    BOX_PREV = 'viewbox__control_previous'
    ACTIVE_SLIDE = '//div[contains(@class, "viewbox__slide_active")]'
    CURRENT_NUM = '//div[contains(@class, "viewbox__slide_active")]//span[@class="viewbox__current"]'
    TOTAL_NUM = 'viewbox__total'
    PREVIEW_IMG = '//img[@class="viewbox__preview-pic"]'

    def __init__(self, driver):
        super(Slider, self).__init__(driver)

    def open_slider(self):
        slider = self.driver.find_element_by_class_name(self.OPEN_CLASS)
        slider.click()

    def close_slider(self, by_area=0):
        if by_area:
            btn_close = self.driver.find_element_by_class_name(self.CLOSE_AREA)
            actions = ActionChains(self.driver)
            actions.move_to_element_with_offset(btn_close, 0, 0).click().perform()
        else:
            btn_close = self.driver.find_element_by_class_name(self.CLOSE_CLASS)
            btn_close.click()

    def click_next(self, method=0):
        btn_next = self.driver.find_element_by_class_name(self.ICON_NEXT)
        if method:
            btn_next = self.driver.find_element_by_class_name(self.BOX_NEXT)
        btn_next.click()

    def click_prev(self, method=0):
        btn_prev = self.driver.find_element_by_class_name(self.ICON_PREV)
        if method:
            btn_prev = self.driver.find_element_by_class_name(self.BOX_PREV)
        btn_prev.click()

    def go_to_slide(self, slide_num=0):
        imgs = self.driver.find_elements_by_xpath(self.PREVIEW_IMG)
        imgs[slide_num].click()

    def get_page_num_from_browser(self):
        current_num = WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CURRENT_NUM))
        size = current_num.get_attribute("innerText")
        if not size:
            size = current_num.text
        return int(size)

    def get_max_page_num(self):
        max_num = WebDriverWait(self.driver, 20, 0.1).until(
            lambda d: d.find_element_by_class_name(self.TOTAL_NUM))
        size = max_num.get_attribute("innerText")
        if not size:
            size = max_num.text
        return int(size)

    @property
    def banner(self):
        return Banner(self.driver)


class Banner(Component):
    CLASS = 'js-popup_banner'

    def find(self):
        self.driver.find_element_by_class_name(self.CLASS)
