# -*- coding: utf-8 -*-

import os, unittest, urlparse

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, NoSuchWindowException


class Page(object):
    BASE_URL = 'https://calendar.mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get("data:,")
        self.driver.get(url)
        self.driver.maximize_window()

class Component(object):
    def __init__(self, driver):
        self.driver = driver

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('HW4BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        
        USEREMAIL = os.environ['HW4LOGIN']
        PASSWORD = os.environ['HW4PASSWORD']
     
        auth_page = AuthPage(self.driver)
        auth_page.open()
     
        auth_form = auth_page.form
        auth_form.set_login(USEREMAIL)
        auth_form.set_password(PASSWORD)
        auth_form.submit()

    def tearDown(self):
        self.driver.quit()


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)

class MainPage(Page):
    PATH = ''

    @property
    def more_button(self):
        return MoreButton(self.driver)

    @property
    def settings_button(self):
        return SettingsButton(self.driver)

class CommonPage(Page):
    PATH = '/?action=settings&page=common'

    @property
    def navigation_elements(self):
        return NavigationElements(self.driver)

    @property
    def settings_form(self):
        return CommonSettingsForm(self.driver)

class ImportPage(Page):
    PATH = '/?action=settings&page=import'

    @property
    def navigation_elements(self):
        return NavigationElements(self.driver)

    @property
    def import_form(self):
        return ImportForm(self.driver)

class RemindersPage(Page):
    PATH = '/?action=settings&page=reminders'

    @property
    def navigation_elements(self):
        return NavigationElements(self.driver)

class CitiesPage(Page):
    PATH = '/?action=settings&page=common-region'

    @property
    def cities_form(self):
        return CitiesForm(self.driver)


class AuthForm(Component):
    LOGIN = 'Login'
    PASSWORD = 'Password'
    SUBMIT = '//button[text()="Войти"]'
 
    def set_login(self, login):
        self.driver.find_element_by_name(self.LOGIN).send_keys(login)
 
    def set_password(self, pwd):
        self.driver.find_element_by_name(self.PASSWORD).send_keys(pwd)
 
    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()

class MoreButton(Component):
    def move_to(self):
        self.driver.find_elements_by_xpath("//*[contains(text(), 'Ещё')]")[0].click()

class SettingsButton(Component):
    def click(self):
        self.driver.find_elements_by_xpath("//*[contains(text(), 'Настройки')]")[1].click()

class NavigationElements(Component):
    def navigate_to_common(self):
        self.driver.find_elements_by_xpath("//*[contains(text(), 'Общие настройки')]")[0].click()

    def navigate_to_import(self):
        self.driver.find_elements_by_xpath("//*[contains(text(), 'Импорт')]")[6].click()

    def navigate_to_reminders(self):
        self.driver.find_elements_by_xpath("//*[contains(text(), 'Уведомления')]")[0].click()

    def save(self):
        try:
            self.driver.find_elements_by_xpath("//*[contains(text(), 'Сохранить')]")[2].click()
        except IndexError as e:
            self.save()

    def cancel(self):
        self.driver.find_elements_by_xpath("//*[contains(text(), 'Отменить')]")[0].click()

    def close(self):
        self.driver.find_elements_by_class_name("popup__close")[0].click()

class CommonSettingsForm(Component):
    def get_current_city(self):
        return self.driver.find_elements_by_css_selector('.settings-region__link .underlined_dashed')[0].get_attribute('innerHTML')

    def click_city(self):
        self.driver.find_elements_by_class_name('settings-region__link')[0].click()

    def get_start_time(self):
        start = self.driver.find_elements_by_name("start")[0]
        return start.get_attribute('value')

    def change_start_time(self):
        start = self.driver.find_elements_by_name("start")[0]
        old_start = start.get_attribute('value')
        new_start = old_start[:-1] + str((int(old_start[-1]) + 1) % 10)
        start.clear()
        start.send_keys(new_start)
        return new_start

    def get_end_time(self):
        start = self.driver.find_elements_by_name("end")[0]
        return start.get_attribute('value')

    def change_end_time(self,):
        start = self.driver.find_elements_by_name("end")[0]
        old_start = start.get_attribute('value')
        new_start = old_start[:-1] + str((int(old_start[-1]) + 1) % 10)
        start.clear()
        start.send_keys(new_start)
        return new_start

    def get_days_of_week(self):
        checkboxes = self.driver.find_elements_by_class_name('workdays__day')
        ret = []
        for i in range(len(checkboxes)):
            if checkboxes[i].is_selected():
                ret.append(i)
        return ret

    def change_days_of_week(self):
        checkboxes = self.driver.find_elements_by_class_name('workdays__day')
        for i in range(len(checkboxes)):
            checkboxes[i].click()

    def get_showing_free_time_to_all(self):
        return self.driver.find_elements_by_xpath("//*[contains(text(), 'Показывать мое свободное время всем пользователям')]").is_selected()

    def change_showing_free_time_to_all(self):
        self.driver.find_elements_by_xpath("//*[contains(text(), 'Показывать мое свободное время всем пользователям')]").click()

class CitiesForm(Component):
    def set_auto(self):
        self.driver.find_elements_by_class_name('x-pm-region-select__auto-detected-city')[0].click()

    def get_auto(self):
        return self.driver.find_elements_by_class_name('x-pm-region-select__auto-detected-city')[0].get_attribute('innerHTML')

    def set_manual(self):
        self.driver.find_elements_by_class_name('x-pm-region-select__form__label')[1].click()

    def type_city(self, name):
        input = self.driver.find_element_by_id('x-pm-region-select__input')
        input.clear()
        input.send_keys(name)

    def get_input(self):
        return self.driver.find_element_by_id('x-pm-region-select__input').get_attribute('value')

    def get_suggestions(self):
        ret = []
        elems = self.driver.find_elements_by_class_name('x-pm-region-select__suggest__item')
        for elem in elems:
            ret.append(elem.get_attribute('data-suggest'))
        return ret

    def choose_suggestion(self, name):
        try:
            elems = self.driver.find_elements_by_class_name('x-pm-region-select__suggest__item')
            for elem in elems:
                if name == elem.get_attribute('data-suggest'):
                    elem.click()
                    return elem
            return None
        except StaleElementReferenceException as e:
            return self.choose_suggestion(name)

    def move_to_end_of_suggestions(self):
        while True:
            elem = self.driver.find_elements_by_class_name('x-pm-region-select__suggest__item')[-1]
            ActionChains(self.driver).move_to_element(elem).perform()
            new_elem = self.driver.find_elements_by_class_name('x-pm-region-select__suggest__item')[-1]
            if elem == new_elem:
                break

    def go_back(self):
        self.driver.find_elements_by_xpath("//*[contains(text(), 'Вернуться')]")[1].click()

    def save(self):
        self.driver.find_elements_by_xpath("//*[contains(text(), 'Сохранить')]")[1].click()

class ImportForm(Component):
    YA_LOGIN = "dbwqudqwdqwbudqw@yandex.ru"
    YA_PASS = "https://passport.yandex.ru/registration/mail?from=mail&origin=home_v14_ru&retpath=https%3A%2F%2Fmail.yandex.ru"

    def import_yandex(self):
        self.driver.find_elements_by_xpath("//*[contains(text(), 'Яндекс.Календарь')]")[0].click()
        self.driver.find_elements_by_name('login')[0].send_keys(self.YA_LOGIN)
        self.driver.find_elements_by_name('password')[0].send_keys(self.YA_PASS)
        self.driver.find_elements_by_xpath("//*[contains(text(), 'Импортировать')]")[1].click()

        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_elements_by_xpath("//*[contains(text(), 'Календари успешно импортированы')]")
        )


class ExtraTest(BaseTestCase):
    def test_more_settings(self):
        main_page = MainPage(self.driver)

        main_page.more_button.move_to()
        main_page.settings_button.click()

        self.assertTrue(CommonPage.PATH in main_page.driver.current_url)

class DateTest(BaseTestCase):
    def test_save(self):
        common_page = CommonPage(self.driver)
        settings_form = common_page.settings_form
        navigation_elements = common_page.navigation_elements

        common_page.open()
        time1 = settings_form.get_start_time()
        settings_form.change_start_time()
        navigation_elements.save()

        common_page.open()
        time2 = settings_form.get_start_time()
        self.assertNotEqual(time1, time2)

    def test_cancel(self):
        common_page = CommonPage(self.driver)
        settings_form = common_page.settings_form
        navigation_elements = common_page.navigation_elements

        common_page.open()
        time1 = settings_form.get_start_time()
        settings_form.change_start_time()
        navigation_elements.cancel()

        common_page.open()
        time2 = settings_form.get_start_time()
        self.assertEqual(time1, time2)

    def test_close(self):
        common_page = CommonPage(self.driver)
        settings_form = common_page.settings_form
        navigation_elements = common_page.navigation_elements

        common_page.open()
        time1 = settings_form.get_start_time()
        settings_form.change_start_time()
        navigation_elements.close()

        common_page.open()
        time2 = settings_form.get_start_time()
        self.assertEqual(time1, time2)

class CitiesTest(BaseTestCase):
    def test_auto_select(self):
        cities_page = CitiesPage(self.driver)
        cities_page.open()

        cities_form = cities_page.cities_form
        cities_form.set_auto()
        self.assertEqual(cities_form.get_auto(), u"Москва")

    def test_city_manual(self):
        cities_page = CitiesPage(self.driver)
        cities_page.open()

        city = u"Архангельск"

        cities_form = cities_page.cities_form
        cities_form.set_manual()
        cities_form.type_city(city)
        cities_form.choose_suggestion(city)
        cities_form.save()

        common_page = CommonPage(self.driver)
        result_city = common_page.settings_form.get_current_city()

        cities_page.open()
        cities_form.set_auto()
        cities_form.save()

        self.assertEqual(city, result_city)

    def test_city_back(self):
        cities_page = CitiesPage(self.driver)
        cities_page.open()

        cities_form = cities_page.cities_form
        cities_form.go_back()

        main_page = MainPage(self.driver)
        self.assertTrue(CommonPage.PATH in main_page.driver.current_url)

class CalendarTest(BaseTestCase):
    def test_yandex_calendar(self):
        import_page = ImportPage(self.driver)
        import_page.open()

        import_form = import_page.import_form
        import_form.import_yandex()


