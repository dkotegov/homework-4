from components.component import Component


class NavbarComponent(Component):
    USERNAME = '//h3[@id="navbar-username"]'

    def get_username(self):
        return self.driver.find_element_by_xpath(self.USERNAME).text
