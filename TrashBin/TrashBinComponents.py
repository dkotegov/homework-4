from Base import Component


class Utils(Component):
    FILE_IN_TRASH = '//a[@data-qa-name="{}"]'

    def check_if_file_exist_by_name(self, filename):
        return self._check_if_element_exists_by_xpath(self.FILE_IN_TRASH.format(filename))

    def select_file(self, filename):
        self._wait_until_and_get_elem_by_xpath(self.FILE_IN_TRASH.format(filename)).click()


class Restore(Component):
    FILE_IN_TRASH = '//a[@data-qa-name="{}"]'
    TOOLBAR_RESTORE_BUTTON = '//div[@data-name="restore"]'
    INLINE_RESTORE_BUTTON = '//a[@data-qa-name="{}"]//div[@class="DataListControl__root--vZ6Hu' \
                            ' undefined DataListControl__root_24--2qd2T"]'
    SUBMIT_RESTORE_BUTTON = '//button[@data-name="action"]'

    def restore_file_from_toolbar(self, filename):
        self._wait_until_and_get_elem_by_xpath(self.FILE_IN_TRASH.format(filename)).click()
        self._wait_until_and_get_elem_by_xpath(self.TOOLBAR_RESTORE_BUTTON).click()
        self._wait_until_and_get_elem_by_xpath(self.SUBMIT_RESTORE_BUTTON).click()

    def restore_file_from_menu(self, filename):
        self._wait_until_and_get_elem_by_xpath(self.INLINE_RESTORE_BUTTON.format(filename)).click()
        self._wait_until_and_get_elem_by_xpath(self.SUBMIT_RESTORE_BUTTON).click()


class Delete(Component):
    CLEAR_TRASH_BUTTON = '//div[@data-name="clear"]'
    CLEAR_CONFIRM_BUTTON = '//button[@data-name="empty"]'

    def clear_trash_bin(self):
        self._wait_until_and_get_elem_by_xpath(self.CLEAR_TRASH_BUTTON).click()
        self._wait_until_and_get_elem_by_xpath(self.CLEAR_CONFIRM_BUTTON).click()
