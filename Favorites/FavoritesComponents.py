from Base import Component


class Utils(Component):
    FILE_IN_FAVORITES = '//a[@data-qa-name="{}"]'

    def check_if_file_exists(self, filename):
        return self._check_if_element_exists_by_xpath(self.FILE_IN_FAVORITES.format(filename))
