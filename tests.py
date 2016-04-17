# -*- coding: utf-8 -*-
import unittest
import urlparse

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class Page(object):
    BASE_URL = 'http://sport.mail.ru/'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()


class Component(object):
    MY_XPATH = ''
    NEWS_XPATH = ''
    TEAM_XPATH = ''
    TABLE_XPATH = ''
    CALENDAR_XPATH = ''
    STATISTICS_XPATH = ''

    def __init__(self, driver):
        self.driver = driver

    def click(self):
        self.driver.find_element_by_xpath(self.MY_XPATH).click()

    @property
    def news(self):
        return SubComponent(self.driver, self.NEWS_XPATH)

    @property
    def team(self):
        return SubComponent(self.driver, self.TEAM_XPATH)

    @property
    def table(self):
        return SubComponent(self.driver, self.TABLE_XPATH)

    @property
    def calendar(self):
        return SubComponent(self.driver, self.CALENDAR_XPATH)

    @property
    def statistics(self):
        return SubComponent(self.driver, self.STATISTICS_XPATH)


class SubComponent(object):
    XPATH = ''
    TITLE = ''

    def __init__(self, driver, xpath):
        self.driver = driver
        self.XPATH = xpath

    def open_in_new_tab(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.XPATH)
        )
        element.click()
        # ActionChains(self.driver).key_down(Keys.COMMAND).click(element).key_up(
        #     Keys.COMMAND).perform()
        # self.driver.switch_to_window(self.driver.window_handles[1])
        # self.TITLE = self.driver.title

    def close(self, window):
        self.driver.close()
        self.driver.switch_to_window(window)

    def get_title(self):
        return self.TITLE


class FormComponent(object):
    def __init__(self, driver):
        self.driver = driver


class SearchForm(FormComponent):
    XPATH = "//input[@placeholder='Введите название команды или имя спортсмена']"

    def __init__(self, driver):
        super(SearchForm, self).__init__(driver)
        self.element = self.driver.find_element_by_xpath(self.XPATH)

    def set_text(self, text):
        self.element.send_keys(text)

    def submit(self):
        self.element.send_keys(Keys.RETURN)


class ChempionLeague(Component):
    NEWS_TITLE = u'Лига чемпионов - Еврокубки - Футбол - все новости на тему Лига чемпионов сезона 2016 - Спорт Mail.Ru'
    TEAM_TITLE = u'Все команды - Футбол - Еврокубки - Лига чемпионов - сезон 2015/2016 - полный список участников на Спорт Mail.Ru'
    TABLE_TITLE = u'Все турнирные таблицы - Лига чемпионов сезона 2015/2016 - Еврокубки - Футбол - Спорт Mail.Ru'
    CALENDAR_TITLE = u'Календарь, расписание и результаты всех матчей - Лига чемпионов сезона 2015/2016 - Еврокубки - Футбол - Спорт Mail.Ru'
    STATISTICS_TITLE = u'Вся статистика - Лига чемпионов сезона 2015/2016 - Еврокубки - Футбол - Спорт Mail.Ru'
    MY_XPATH = "//a[contains(text(),'Лига чемпионов')]"
    NEWS_XPATH = "//li[contains(@id, 'tab117')]/ul/li/a[contains(text(),'Новости')]"
    TEAM_XPATH = "//li[contains(@id, 'tab117')]/ul/li/a[contains(text(),'Команды')]"
    TABLE_XPATH = "//li[contains(@id, 'tab117')]/ul/li/a[contains(text(),'Таблица')]"
    CALENDAR_XPATH = "//li[contains(@id, 'tab117')]/ul/li/a[contains(text(),'Календарь / результаты')]"
    STATISTICS_XPATH = "//li[contains(@id, 'tab117')]/ul/li/a[contains(text(),'Статистика')]"


class EuropeLeague(Component):
    NEWS_TITLE = u'Лига Европы - Еврокубки - Футбол - все новости на тему Лига Европы сезона 2016 - Спорт Mail.Ru'
    TEAM_TITLE = u'Все команды - Футбол - Еврокубки - Лига Европы - сезон 2015/2016 - полный список участников на Спорт Mail.Ru'
    TABLE_TITLE = u'Все турнирные таблицы - Лига Европы сезона 2015/2016 - Еврокубки - Футбол - Спорт Mail.Ru'
    CALENDAR_TITLE = u'Календарь, расписание и результаты всех матчей - Лига Европы сезона 2015/2016 - Еврокубки - Футбол - Спорт Mail.Ru'
    STATISTICS_TITLE = u'Вся статистика - Лига Европы сезона 2015/2016 - Еврокубки - Футбол - Спорт Mail.Ru'
    MY_XPATH = "//a[contains(text(),'Лига Европы')]"
    NEWS_XPATH = "//li[contains(@id, 'tab118')]/ul/li/a[contains(text(),'Новости')]"
    TEAM_XPATH = "//li[contains(@id, 'tab118')]/ul/li/a[contains(text(),'Команды')]"
    TABLE_XPATH = "//li[contains(@id, 'tab118')]/ul/li/a[contains(text(),'Таблица')]"
    CALENDAR_XPATH = "//li[contains(@id, 'tab118')]/ul/li/a[contains(text(),'Календарь / результаты')]"
    STATISTICS_XPATH = "//li[contains(@id, 'tab118')]/ul/li/a[contains(text(),'Статистика')]"


class SuperCup(Component):
    NEWS_TITLE = u'Суперкубок - Еврокубки - Футбол - все новости на тему Суперкубок сезона 2016 - Спорт Mail.Ru'
    TEAM_TITLE = u'Все команды - Футбол - Еврокубки - Суперкубок - сезон 2015 - полный список участников на Спорт Mail.Ru'
    TABLE_TITLE = u'Все турнирные таблицы - Суперкубок сезона 2015/2016 - Еврокубки - Футбол - Спорт Mail.Ru'
    CALENDAR_TITLE = u'Календарь, расписание и результаты всех матчей - Суперкубок сезона 2015 - Еврокубки - Футбол - Спорт Mail.Ru'
    STATISTICS_TITLE = u'Вся статистика - Суперкубок сезона 2015 - Еврокубки - Футбол - Спорт Mail.Ru'
    MY_XPATH = "//a[contains(text(),'Суперкубок')]"
    NEWS_XPATH = "//li[contains(@id, 'tab113')]/ul/li/a[contains(text(),'Новости')]"
    TEAM_XPATH = "//li[contains(@id, 'tab113')]/ul/li/a[contains(text(),'Команды')]"
    TABLE_XPATH = "//li[contains(@id, 'tab113')]/ul/li/a[contains(text(),'Таблица')]"
    CALENDAR_XPATH = "//li[contains(@id, 'tab113')]/ul/li/a[contains(text(),'Календарь / результаты')]"
    STATISTICS_XPATH = "//li[contains(@id, 'tab113')]/ul/li/a[contains(text(),'Статистика')]"


class EuroCupsPage(Page):
    PATH = 'football-eurocups/'

    @property
    def chempion_league(self):
        return ChempionLeague(self.driver)

    @property
    def europe_league(self):
        return EuropeLeague(self.driver)

    @property
    def super_cup(self):
        return SuperCup(self.driver)

    @property
    def searchFrom(self):
        return SearchForm(self.driver)


def test_component(self, league):
    news = league.news
    news.open_in_new_tab()
    self.assertEqual(league.NEWS_TITLE, news.get_title())
    news.close(self.originalWindow)

    team = league.team
    team.open_in_new_tab()
    self.assertEqual(league.TEAM_TITLE, team.get_title())
    team.close(self.originalWindow)

    if isinstance(league, SuperCup) is False:
        table = league.table
        table.open_in_new_tab()
        self.assertEqual(league.TABLE_TITLE, table.get_title())
        table.close(self.originalWindow)

    calendar = league.calendar
    calendar.open_in_new_tab()
    self.assertEqual(league.CALENDAR_TITLE, calendar.get_title())
    calendar.close(self.originalWindow)

    statistics = league.statistics
    statistics.open_in_new_tab()
    self.assertEqual(league.STATISTICS_TITLE, statistics.get_title())
    statistics.close(self.originalWindow)


class ExampleTest(unittest.TestCase):
    NEWS_TITLE = u'Лига Европы - Еврокубки - Футбол - все новости на тему Лига Европы сезона 2016 - Спорт Mail.Ru'

    def setUp(self):
        # browser = os.environ.get('HW4BROWSER', 'CHROME')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        euroCupsPage = EuroCupsPage(self.driver)
        euroCupsPage.open()
        self.originalWindow = self.driver.current_window_handle

        euroLeague = euroCupsPage.europe_league
        euroLeague.click()
        euroLeague.news.open_in_new_tab()
        # europeLeague = euroCupsPage.super_cup
        # europeLeague.click()
        # test_component(self, europeLeague)
        #
        # europeLeague = euroCupsPage.europe_league
        # europeLeague.click()
        # test_component(self, europeLeague)
        #
        # europeLeague = euroCupsPage.chempion_league
        # europeLeague.click()
        # test_component(self, europeLeague)
        #
        # searchForm = euroCupsPage.searchFrom
        # searchForm.set_text('Cristiano Ronaldo')
        # searchForm.submit()
        # self.assertNotIn(u'По вашему запросу ничего не найдено.', self.driver.page_source)
