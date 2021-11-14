from tests.pages.base import Page


class ProfilePage(Page):
    """
    Стриница профиля ресторана
    """

    PHONE = '//input[@name="number"]'
    EMAIL = '//input[@name="email"]'
    TITLE = '//input[@name="title"]'
    COST = '//input[@name="deliveryCost"]'
    CUR_PASSWORD = '//input[@name="password_current"]'
    NEW_PASSWORD = '//input[@name="password"]'
    REPEAT_PASSWORD = '//input[@name="password_repeat"]'
    ADDRESS = '//input[@id="js__map-edit-address"]'
    RADIUS = '//input[@name="radius"]'
    SAVE = '//input[@class="profile-userdata__submit"]'

    def __init__(self, driver):
        self.PATH = 'profile/edits'
        super(ProfilePage, self).__init__(driver)

    def set_phone(self, phone):
        self.driver.find_element_by_xpath(self.PHONE).send_keys(phone)

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.EMAIL).send_keys(email)

    def set_title(self, title):
        self.driver.find_element_by_xpath(self.TITLE).send_keys(title)

    def set_cost(self, cost):
        self.driver.find_element_by_xpath(self.COST).send_keys(cost)

    def set_current_password(self, password):
        self.driver.find_element_by_xpath(self.CUR_PASSWORD).send_keys(password)

    def set_new_password(self, password):
        self.driver.find_element_by_xpath(self.NEW_PASSWORD).send_keys(password)

    def set_repeat_password(self, password):
        self.driver.find_element_by_xpath(self.REPEAT_PASSWORD).send_keys(password)

    def click_save(self):
        self.driver.find_element_by_xpath(self.SAVE).click()
