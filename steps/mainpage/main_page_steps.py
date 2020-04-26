from steps.base_steps import BaseSteps
from pages.mainpage.mainpage import MainPage

class MainSteps(BaseSteps):
    SIGNIN = '#about > div.buttons-wrap > [data-xray-click="login"]'
    SIGNUP = '#about > div.buttons-wrap > [data-xray-click="signup"]'
    REMIND = '[data-test-id="remind"]'
    SIGNUP_REF = '[data-test-id="signup-link"]'

    VK_REF = '#page > footer > div > ul.share > li > [data-xray-click="share_vk"]'
    TWITTER_REF = '#page > footer > div > ul.share > li > [data-xray-click="share_tw"]'
    FACEBOOK_REF = '#page > footer > div > ul.share > li > [data-xray-click="share_fb"]'
    ODNOKLASSNIKI_REF = '#page > footer > div > ul.share > li > [data-xray-click="share_ok"]'

    ABOUT_ID = '[data-xray-click="about_id"]'
    SERVICES = '[data-xray-click="services"]'
    MORELESSSERVICES = '[data-target="toggle"]'

    MAILRU_REF = '[data-xray-click="splash"]'
    ABOUT_COMPANY_REF = '[data-xray-click="about"]'
    SUPPORT_REF = '[data-xray-click="support"]'
    REPORT_REF = '[data-xray-click="report"]'

    SERVICE_CM = '[data-xray-click="service_cm"]'
    SERVICE_DC = '[data-xray-click="service_dc"]'
    SERVICE_VSEAPTEKI = '[data-xray-click="service_vseapteki"]'
    SERVICE_MARUSIA = '[data-xray-click="service_marusia"]'
    SERVICE_AUTO = '[data-xray-click="service_auto"]'
    SERVICE_HEALTH = '[data-xray-click="service_health"]'
    SERVICE_HORO = '[data-xray-click="service_horo"]'
    SERVICE_POGODA = '[data-xray-click="service_pogoda"]'
    SERVICE_LADY = '[data-xray-click="service_lady"]'
    SERVICE_CALENDAR = '[data-xray-click="service_calendar"]'
    SERVICE_REALTY = '[data-xray-click="service_realty"]'
    SERVICE_HI_TECH = '[data-xray-click="service_Hi-Tecjh"]'
    SERVICE_PETS = '[data-xray-click="service_pets"]'
    SERVICE_DOBRO = '[data-xray-click="service_dobro"]'
    SERVICE_MY = '[data-xray-click="service_my"]'
    SERVICE_KINO = '[data-xray-click="service_kino"]'
    SERVICE_GAMES = '[data-xray-click="service_games"]'
    SERVICE_DETI = '[data-xray-click="service_deti"]'

    AUTH_MAIN_BUTTON = '#root > div > div.Layout-mobile__navigationMenu--2qzgN > div > div.c0120 > [data-test-id="navigation-menu-item:main"]'
    AUTH_SETUP_ACCOUNT_INFO = '#root > div > div.Layout-mobile__container--2MbDy > div > div.MainPage-mobile__content--2ZMsq > div.MainPage-mobile__personalCard--3OTal > div > div:nth-child(2) > a > [data-test-id="card-footer"]'
    AUTH_SETUP_ALL_SETTINGS = '#root > div > div.Layout-mobile__container--2MbDy > div > div.MainPage-mobile__content--2ZMsq > div.MainPage-mobile__contactsCard--3KdWm > div > div:nth-child(2) > a > [data-test-id="card-footer"]'
    AUTH_ACCOUNT_INFO = '#root > div > div.Layout-mobile__navigationMenu--2qzgN > div > div.c0120 > [data-test-id="navigation-menu-item:profile"]'
    AUTH_ALL_SETTINGS = '#root > div > div.Layout-mobile__navigationMenu--2qzgN > div > div.c0120 > [data-test-id="navigation-menu-item:contacts"]'

    def __init__(self, driver, page=None):
        super().__init__(driver, MainPage)

    def button_signin(self):
        self.page.waiting_for_visible_by_selector(self.SIGNIN)
        self.page.driver.find_element_by_css_selector(self.SIGNIN).click()

    def button_signup(self):
        self.page.waiting_for_visible_by_selector(self.SIGNUP)
        self.page.driver.find_element_by_css_selector(self.SIGNUP).click()

    def ref_signup(self):
        self.page.waiting_for_visible_by_selector(self.SIGNUP_REF)
        self.page.driver.find_element_by_css_selector(self.SIGNUP_REF).click()

    def ref_remind(self):
        self.page.waiting_for_visible_by_selector(self.REMIND)
        self.page.driver.find_element_by_css_selector(self.REMIND).click()

    def ref_auth_main_button(self):
        self.page.waiting_for_visible_by_selector(self.AUTH_MAIN_BUTTON)
        self.page.driver.find_element_by_css_selector(self.AUTH_MAIN_BUTTON).click()

    def ref_auth_setup_account_info(self):
        self.page.waiting_for_visible_by_selector(self.AUTH_SETUP_ACCOUNT_INFO)
        self.page.driver.find_element_by_css_selector(self.AUTH_SETUP_ACCOUNT_INFO).click()

    def ref_auth_setup_all_settings(self):
        self.page.waiting_for_visible_by_selector(self.AUTH_SETUP_ALL_SETTINGS)
        self.page.driver.find_element_by_css_selector(self.AUTH_SETUP_ALL_SETTINGS).click()

    def ref_auth_account_info(self):
        self.page.waiting_for_visible_by_selector(self.AUTH_ACCOUNT_INFO)
        self.page.driver.find_element_by_css_selector(self.AUTH_ACCOUNT_INFO).click()

    def ref_auth_all_settings(self):
        self.page.waiting_for_visible_by_selector(self.AUTH_ALL_SETTINGS)
        self.page.driver.find_element_by_css_selector(self.AUTH_ALL_SETTINGS).click()

    def services(self):
        self.page.waiting_for_visible_by_selector(self.SERVICES)
        self.page.driver.find_element_by_css_selector(self.SERVICES).click()
        self.page.waiting_for_visible_by_selector(self.MORELESSSERVICES)
        self.page.driver.find_element_by_css_selector(self.MORELESSSERVICES).click()

    def service_cm(self):
        self.page.waiting_for_visible_by_selector(self.SERVICE_CM)
        self.page.driver.find_element_by_css_selector(self.SERVICE_CM).click()

    def service_dc(self):
        self.page.waiting_for_visible_by_selector(self.SERVICE_DC)
        self.page.driver.find_element_by_css_selector(self.SERVICE_DC).click()

    def service_vseapteki(self):
        self.page.waiting_for_visible_by_selector(self.SERVICE_VSEAPTEKI)
        self.page.driver.find_element_by_css_selector(self.SERVICE_VSEAPTEKI).click()

    def service_marusia(self):
        self.page.waiting_for_visible_by_selector(self.SERVICE_MARUSIA)
        self.page.driver.find_element_by_css_selector(self.SERVICE_MARUSIA).click()

    def service_auto(self):
        self.page.waiting_for_visible_by_selector(self.SERVICE_AUTO)
        self.page.driver.find_element_by_css_selector(self.SERVICE_AUTO).click()

    def service_health(self):
        self.page.waiting_for_visible_by_selector(self.SERVICE_HEALTH)
        self.page.driver.find_element_by_css_selector(self.SERVICE_HEALTH).click()

    def service_horo(self):
        self.page.waiting_for_visible_by_selector(self.SERVICE_HORO)
        self.page.driver.find_element_by_css_selector(self.SERVICE_HORO).click()

    def service_pogoda(self):
        self.page.waiting_for_visible_by_selector(self.SERVICE_POGODA)
        self.page.driver.find_element_by_css_selector(self.SERVICE_POGODA).click()

    def service_lady(self):
        self.page.waiting_for_visible_by_selector(self.SERVICE_LADY)
        self.page.driver.find_element_by_css_selector(self.SERVICE_LADY).click()

    def service_calendar(self):
        self.page.waiting_for_visible_by_selector(self.SERVICE_CALENDAR)
        self.page.driver.find_element_by_css_selector(self.SERVICE_CALENDAR).click()

    def service_realty(self):
        self.page.waiting_for_visible_by_selector(self.SERVICE_REALTY)
        self.page.driver.find_element_by_css_selector(self.SERVICE_REALTY).click()

    def service_Hi_Tecjh(self):
        self.page.waiting_for_visible_by_selector(self.SERVICE_HI_TECH)
        self.page.driver.find_element_by_css_selector(self.SERVICE_HI_TECH).click()

    def service_pets(self):
        self.page.waiting_for_visible_by_selector(self.SERVICE_PETS)
        self.page.driver.find_element_by_css_selector(self.SERVICE_PETS).click()

    def service_dobro(self):
        self.page.waiting_for_visible_by_selector(self.SERVICE_DOBRO)
        self.page.driver.find_element_by_css_selector(self.SERVICE_DOBRO).click()

    def service_my(self):
        self.page.waiting_for_visible_by_selector(self.SERVICE_MY)
        self.page.driver.find_element_by_css_selector(self.SERVICE_MY).click()

    def service_kino(self):
        self.page.waiting_for_visible_by_selector(self.SERVICE_KINO)
        self.page.driver.find_element_by_css_selector(self.SERVICE_KINO).click()

    def service_games(self):
        self.page.waiting_for_visible_by_selector(self.SERVICE_GAMES)
        self.page.driver.find_element_by_css_selector(self.SERVICE_GAMES).click()

    def service_deti(self):
        self.page.waiting_for_visible_by_selector(self.SERVICE_DETI)
        self.page.driver.find_element_by_css_selector(self.SERVICE_DETI).click()

    def services_less(self):
        self.page.waiting_for_visible_by_selector(self.MORELESSSERVICES)
        self.page.driver.find_element_by_css_selector(self.MORELESSSERVICES).click()

    def tab(self):
        self.page.waiting_for_visible_by_selector(self.SERVICES)
        self.page.driver.find_element_by_css_selector(self.SERVICES).click()
        self.page.waiting_for_visible_by_selector(self.ABOUT_ID)
        self.page.driver.find_element_by_css_selector(self.ABOUT_ID).click()

    def ref_mailru(self):
        self.page.waiting_for_visible_by_selector(self.MAILRU_REF)
        self.page.driver.find_element_by_css_selector(self.MAILRU_REF).click()

    def ref_about_company(self):
        self.page.waiting_for_visible_by_selector(self.ABOUT_COMPANY_REF)
        self.page.driver.find_element_by_css_selector(self.ABOUT_COMPANY_REF).click()

    def ref_support(self):
        self.page.waiting_for_visible_by_selector(self.SUPPORT_REF)
        self.page.driver.find_element_by_css_selector(self.SUPPORT_REF).click()

    def ref_report(self):
        self.page.waiting_for_visible_by_selector(self.REPORT_REF)
        self.page.driver.find_element_by_css_selector(self.REPORT_REF).click()

    def ref_vk(self):
        self.page.waiting_for_visible_by_selector(self.VK_REF)
        self.page.driver.find_element_by_css_selector(self.VK_REF).click()

    def ref_tw(self):
        self.page.waiting_for_visible_by_selector(self.TWITTER_REF)
        self.page.driver.find_element_by_css_selector(self.TWITTER_REF).click()

    def ref_fb(self):
        self.page.waiting_for_visible_by_selector(self.FACEBOOK_REF)
        self.page.driver.find_element_by_css_selector(self.FACEBOOK_REF).click()

    def ref_ok(self):
        self.page.waiting_for_visible_by_selector(self.ODNOKLASSNIKI_REF)
        self.page.driver.find_element_by_css_selector(self.ODNOKLASSNIKI_REF).click()
