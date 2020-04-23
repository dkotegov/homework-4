from pages.default import DefaultPage, DefaultSteps

class MainPage(DefaultPage):

    @property
    def steps(self):
        return MainSteps(self.driver)


class MainSteps(DefaultSteps):

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

    AUTH_SETUP_ACCOUNT_INFO = '[div.MainPage-mobile__personalCard--3OTal > div > div:nth-child(2) > [data-test-id="card-footer"]'
    AUTH_SETUP_ALL_SETTINGS = '[div.MainPage-mobile__contactsCard--3KdWm > div > div:nth-child(2) > [data-test-id="card-footer"]'
    AUTH_ACCOUNT_INFO = '[data-test-id="navigation-menu-item:profile"]'
    AUTH_ALL_SETTINGS = '[data-test-id="navigation-menu-item:contacts"]'

    def button_signin(self):
        self.waiting_for_visible(self.SIGNIN)
        self.driver.find_element_by_css_selector(self.SIGNIN).click()

    def button_signup(self):
        self.waiting_for_visible(self.SIGNUP)
        self.driver.find_element_by_css_selector(self.SIGNUP).click()
    
    def ref_signup(self):
        self.waiting_for_visible(self.SIGNUP_REF)
        self.driver.find_element_by_css_selector(self.SIGNUP_REF).click()

    def ref_remind(self):
        self.waiting_for_visible(self.REMIND)
        self.driver.find_element_by_css_selector(self.REMIND).click()

    def ref_auth_setup_account_info(self):
        self.waiting_for_visible(self.AUTH_SETUP_ACCOUNT_INFO)
        self.driver.find_element_by_css_selector(self.AUTH_SETUP_ACCOUNT_INFO).click()
    
    def ref_auth_setup_all_settings(self):
        self.waiting_for_visible(self.AUTH_SETUP_ALL_SETTINGS)
        self.driver.find_element_by_css_selector(self.AUTH_SETUP_ALL_SETTINGS).click()

    def ref_auth_account_info(self):
        self.waiting_for_visible(self.AUTH_ACCOUNT_INFO)
        self.driver.find_element_by_css_selector(self.AUTH_ACCOUNT_INFO).click()
    
    def ref_auth_all_settings(self):
        self.waiting_for_visible(self.AUTH_ALL_SETTINGS)
        self.driver.find_element_by_css_selector(self.AUTH_ALL_SETTINGS).click()

    def services(self):
        self.waiting_for_visible(self.SERVICES)
        self.driver.find_element_by_css_selector(self.SERVICES).click()
        self.waiting_for_visible(self.MORELESSSERVICES)
        self.driver.find_element_by_css_selector(self.MORELESSSERVICES).click()

    def service_cm(self):
        self.waiting_for_visible(self.SERVICE_CM)
        self.driver.find_element_by_css_selector(self.SERVICE_CM).click()

    def service_dc(self):
        self.waiting_for_visible(self.SERVICE_DC)
        self.driver.find_element_by_css_selector(self.SERVICE_DC).click()

    def service_vseapteki(self):
        self.waiting_for_visible(self.SERVICE_VSEAPTEKI)
        self.driver.find_element_by_css_selector(self.SERVICE_VSEAPTEKI).click()

    def service_marusia(self):
        self.waiting_for_visible(self.SERVICE_MARUSIA)
        self.driver.find_element_by_css_selector(self.SERVICE_MARUSIA).click()

    def service_auto(self):
        self.waiting_for_visible(self.SERVICE_AUTO)
        self.driver.find_element_by_css_selector(self.SERVICE_AUTO).click()

    def service_health(self):
        self.waiting_for_visible(self.SERVICE_HEALTH)
        self.driver.find_element_by_css_selector(self.SERVICE_HEALTH).click()

    def service_horo(self):
        self.waiting_for_visible(self.SERVICE_HORO)
        self.driver.find_element_by_css_selector(self.SERVICE_HORO).click()

    def service_pogoda(self):
        self.waiting_for_visible(self.SERVICE_POGODA)
        self.driver.find_element_by_css_selector(self.SERVICE_POGODA).click()

    def service_lady(self):
        self.waiting_for_visible(self.SERVICE_LADY)
        self.driver.find_element_by_css_selector(self.SERVICE_LADY).click()

    def service_calendar(self):
        self.waiting_for_visible(self.SERVICE_CALENDAR)
        self.driver.find_element_by_css_selector(self.SERVICE_CALENDAR).click()

    def service_realty(self):
        self.waiting_for_visible(self.SERVICE_REALTY)
        self.driver.find_element_by_css_selector(self.SERVICE_REALTY).click()

    def service_Hi_Tecjh(self):
        self.waiting_for_visible(self.SERVICE_HI_TECH)
        self.driver.find_element_by_css_selector(self.SERVICE_HI_TECH).click()

    def service_pets(self):
        self.waiting_for_visible(self.SERVICE_PETS)
        self.driver.find_element_by_css_selector(self.SERVICE_PETS).click()

    def service_dobro(self):
        self.waiting_for_visible(self.SERVICE_DOBRO)
        self.driver.find_element_by_css_selector(self.SERVICE_DOBRO).click()

    def service_my(self):
        self.waiting_for_visible(self.SERVICE_MY)
        self.driver.find_element_by_css_selector(self.SERVICE_MY).click()

    def service_kino(self):
        self.waiting_for_visible(self.SERVICE_KINO)
        self.driver.find_element_by_css_selector(self.SERVICE_KINO).click()

    def service_games(self):
        self.waiting_for_visible(self.SERVICE_GAMES)
        self.driver.find_element_by_css_selector(self.SERVICE_GAMES).click()

    def service_deti(self):
        self.waiting_for_visible(self.SERVICE_DETI)
        self.driver.find_element_by_css_selector(self.SERVICE_DETI).click()
    
    def services_less(self):
        self.waiting_for_visible(self.MORELESSSERVICES)
        self.driver.find_element_by_css_selector(self.MORELESSSERVICES).click()

    def tab(self):
        self.waiting_for_visible(self.SERVICES)
        self.driver.find_element_by_css_selector(self.SERVICES).click()
        self.waiting_for_visible(self.ABOUT_ID)
        self.driver.find_element_by_css_selector(self.ABOUT_ID).click()
    
    def ref_mailru(self):
        self.waiting_for_visible(self.MAILRU_REF)
        self.driver.find_element_by_css_selector(self.MAILRU_REF).click()

    def ref_about_company(self):
        self.waiting_for_visible(self.ABOUT_COMPANY_REF)
        self.driver.find_element_by_css_selector(self.ABOUT_COMPANY_REF).click()

    def ref_support(self):
        self.waiting_for_visible(self.SUPPORT_REF)
        self.driver.find_element_by_css_selector(self.SUPPORT_REF).click()
    
    def ref_report(self):
        self.waiting_for_visible(self.REPORT_REF)
        self.driver.find_element_by_css_selector(self.REPORT_REF).click()

    def ref_vk(self):
        self.waiting_for_visible(self.VK_REF)
        self.driver.find_element_by_css_selector(self.VK_REF).click()
    
    def ref_tw(self):
        self.waiting_for_visible(self.TWITTER_REF)
        self.driver.find_element_by_css_selector(self.TWITTER_REF).click()
    
    def ref_fb(self):
        self.waiting_for_visible(self.FACEBOOK_REF)
        self.driver.find_element_by_css_selector(self.FACEBOOK_REF).click()
    
    def ref_ok(self):
        self.waiting_for_visible(self.ODNOKLASSNIKI_REF)
        self.driver.find_element_by_css_selector(self.ODNOKLASSNIKI_REF).click()

        
