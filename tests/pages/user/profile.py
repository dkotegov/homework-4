from tests.pages.profile import ProfilePage


class UserProfilePage(ProfilePage):
    """
    Стриница профиля пользователя
    """

    NAME = '//input[@name="name"]'

    ERROR_NAME = '//p[@id="nameError"]'

    def __init__(self, driver):
        self.PATH = 'profile/edits'
        super(ProfilePage, self).__init__(driver)

    def set_name(self, name):
        elem = self.driver.find_element_by_xpath(self.NAME)
        elem.clear()
        elem.send_keys(name)

    def get_name_error(self):
        return self.driver.find_element_by_xpath(self.ERROR_NAME).text
