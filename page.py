# coding=utf-8
import urlparse

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page(object):
    BASE_URL = 'https://news.mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class MMVB(object):
    USD = './/*[@class="s-rate s-rate_mmvb c-clearin"]/li[1]/span/span[2]/span[1]'
    EUR = './/*[@class="s-rate s-rate_mmvb c-clearin"]/li[2]/span/span[2]/span[1]'

    def __init__(self, driver):
        self.driver = driver

    def get_usd(self):
        return float(self.driver.find_element_by_xpath(self.USD).text)

    def get_eur(self):
        return float(self.driver.find_element_by_xpath(self.EUR).text)


class CB(object):
    USD = './/*[@class="s-rate c-clearin"]/li[1]/a/span[2]/span[@class="s-rate__item__cont__value"]'
    EUR = './/*[@class="s-rate c-clearin"]/li[2]/a/span[2]/span[@class="s-rate__item__cont__value"]'
    GBP = './/*[@class="s-rate c-clearin"]/li[3]/a/span[2]/span[@class="s-rate__item__cont__value"]'
    CHF = './/*[@class="s-rate c-clearin"]/li[4]/a/span[2]/span[@class="s-rate__item__cont__value"]'
    DATE = './/*[@data-module="Dropdown.Ajs.CurrCal"]/a/span'
    OTHER_RATES = './/div[@class="s-index__regionnews__list"]/div/div/a/span/span[1]'
    SHARE_MY = './/a[@class="js-shares_all_btn share share_my"]'
    SHARE_VK = './/a[@class="js-shares_all_btn share share_vk"]'
    SHARE_OK = './/a[@class="js-shares_all_btn share share_ok"]'
    SHARE_FB = './/a[@class="js-shares_all_btn share share_fb"]'
    SHARE_TW = './/a[@class="js-shares_all_btn share share_tw"]'

    def __init__(self, driver):
        self.driver = driver

    def get_usd(self):
        return float(self.driver.find_element_by_xpath(self.USD).text)

    def get_eur(self):
        return float(self.driver.find_element_by_xpath(self.EUR).text)

    def get_gbp(self):
        return float(self.driver.find_element_by_xpath(self.GBP).text)

    def get_chf(self):
        return float(self.driver.find_element_by_xpath(self.CHF).text)

    def get_date(self):
        return self.driver.find_element_by_xpath(self.DATE).text

    def get_other_rates(self):
        return [float(rate.text) for rate in self.driver.find_elements_by_xpath(self.OTHER_RATES)]

    def get_button_share_my(self):
        return self.driver.find_element_by_xpath(self.SHARE_MY)

    def get_button_share_vk(self):
        return self.driver.find_element_by_xpath(self.SHARE_VK)

    def get_button_share_ok(self):
        return self.driver.find_element_by_xpath(self.SHARE_OK)

    def get_button_share_fb(self):
        return self.driver.find_element_by_xpath(self.SHARE_FB)

    def get_button_share_tw(self):
        return self.driver.find_element_by_xpath(self.SHARE_TW)


class MiddleBlock(object):
    CURRENCY_PAIRS = u'.//*[@data-typename="Валютные пары"]/div/div/table/tbody/tr/td[1]/div'
    OIL_AND_PRECIOUS_METALS = u'.//*[@data-typename="Нефть и драгметаллы"]/div/div/table/tbody/tr/td[1]/div'
    BLUE = u'.//*[@data-typename="Голубые фишки"]/div/div/table/tbody/tr/td[1]/div'

    def __init__(self, driver):
        self.driver = driver

    def get_currency_pairs(self):
        return [float(rate.text) for rate in self.driver.find_elements_by_xpath(self.CURRENCY_PAIRS)]

    def get_oil_open_pairs(self):
        return [float(rate.text) for rate in self.driver.find_elements_by_xpath(self.OIL_AND_PRECIOUS_METALS)]

    def get_blue(self):
        return [float(rate.text) for rate in self.driver.find_elements_by_xpath(self.BLUE)]


class CurrencyConverter(object):
    FIRST_INPUT = './/div[@class="b-calc"]/form/div[1]/div[1]/input[2]'
    SECOND_INPUT = './/div[@class="b-calc"]/form/div[3]/div[1]/input[2]'
    FIRST_CURRENCY = './/div[@class="b-calc"]/form/div[1]/div[2]/div/a[@class="c-text-select__link js-link"]'
    SECOND_CURRENCY = './/div[@class="b-calc"]/form/div[3]/div[2]/div/a[@class="c-text-select__link js-link"]'
    USD_1 = './/div[@class="b-calc"]/form/div[1]//div[@class="c-text-select__dropdown__list__item js-currency_item"][@data-code="USD"]/a'
    EUR_1 = './/div[@class="b-calc"]/form/div[1]//div[@class="c-text-select__dropdown__list__item js-currency_item"][@data-code="EUR"]/a'
    RUB_1 = './/div[@class="b-calc"]/form/div[1]//div[@class="c-text-select__dropdown__list__item js-currency_item"][@data-code="RUB"]/a'
    USD_2 = './/div[@class="b-calc"]/form/div[3]//div[@class="c-text-select__dropdown__list__item js-currency_item"][@data-code="USD"]/a'
    EUR_2 = './/div[@class="b-calc"]/form/div[3]//div[@class="c-text-select__dropdown__list__item js-currency_item"][@data-code="EUR"]/a'
    RUB_2 = './/div[@class="b-calc"]/form/div[3]//div[@class="c-text-select__dropdown__list__item js-currency_item"][@data-code="RUB"]/a'

    def __init__(self, driver):
        self.driver = driver

    def set_first_input(self, value):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.FIRST_INPUT))
        )
        self.driver.find_element_by_xpath(self.FIRST_INPUT).clear()
        self.driver.find_element_by_xpath(self.FIRST_INPUT).send_keys(str(value))

    def set_second_input(self, value):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.FIRST_INPUT))
        )
        self.driver.find_element_by_xpath(self.SECOND_INPUT).clear()
        self.driver.find_element_by_xpath(self.SECOND_INPUT).send_keys(str(value))

    def get_first_input(self):
        return self.driver.find_element_by_xpath(self.FIRST_INPUT).get_attribute("value").replace(' ', '')

    def get_second_input(self):
        return self.driver.find_element_by_xpath(self.SECOND_INPUT).get_attribute("value").replace(' ', '')

    def set_first_currency(self, value):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.FIRST_CURRENCY))
        )
        select = self.driver.find_element_by_xpath(self.FIRST_CURRENCY)
        select.click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, value))
        )
        currency = self.driver.find_element_by_xpath(value)
        currency.click()

    def set_second_currency(self, value):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.SECOND_CURRENCY))
        )
        select = self.driver.find_element_by_xpath(self.SECOND_CURRENCY)
        select.click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, value))
        )
        currency = self.driver.find_element_by_xpath(value)
        currency.click()

    def convert_rub_to_eur(self, sum):
        self.set_first_currency(self.RUB_1)
        self.set_second_currency(self.EUR_2)
        self.set_first_input(sum)
        return float(self.get_second_input())

    def convert_rub_to_eur_inverse(self, sum):
        self.set_first_currency(self.EUR_1)
        self.set_second_currency(self.RUB_2)
        self.set_second_input(sum)
        return float(self.get_first_input())

    def convert_usd_to_rub(self, sum):
        self.set_first_currency(self.USD_1)
        self.set_second_currency(self.RUB_2)
        self.set_first_input(sum)
        return float(self.get_second_input())

    def convert_eur_to_rub(self, sum):
        self.set_first_currency(self.EUR_1)
        self.set_second_currency(self.RUB_2)
        self.set_first_input(sum)
        return float(self.get_second_input())





class CurrencyPage(Page):
    PATH = 'currency.html'

    @property
    def cb(self):
        return CB(self.driver)

    @property
    def mmvb(self):
        return MMVB(self.driver)

    @property
    def middle_block(self):
        return MiddleBlock(self.driver)

    @property
    def currency_converter(self):
        return CurrencyConverter(self.driver)






