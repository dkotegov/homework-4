from component import Component


class NavbarComponent(Component):
    USERNAME = '//a[@id="navbar-username]'

    def get_username(self):
        return self.driver.find_element_by_xpath(self.USERNAME).text
        # return WebDriverWait(self.driver, 30, 0.1).until( todo delete?
        #     lambda d: d.find_element_by_xpath(self.USERNAME).text
        # )
