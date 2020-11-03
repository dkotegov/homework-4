from Base import Component


class TabsAtHome(Component):
    FROM_MAIL_SELECTOR = '//div[@data-name="/attaches"]'
    INBOX_SELECTOR = '//div[@data-name="0"]'
    TRASH_SELECTOR = '//div[@data-name="/trashbin"]'
    SELECT_ALL_SELECTOR = '//div[@data-name="selectAll"]'
    HELPER_SELECTOR = '//span[@data-icon="ph-icons-video-help"]'
    SHARE_SELECTOR = '//div[@data-name="share"]'

    def open_inbox(self):
        self._wait_until_and_click_elem_by_xpath(self.FROM_MAIL_SELECTOR).click()
        self._wait_until_and_click_elem_by_xpath(self.INBOX_SELECTOR).click()

    def select_all_files(self):
        self._wait_until_and_click_elem_by_xpath(self.SELECT_ALL_SELECTOR).click()

    def open_trash(self):
        self._wait_until_and_click_elem_by_xpath(self.TRASH_SELECTOR)

    def open_helper(self):
        self._wait_until_and_click_elem_by_xpath(self.HELPER_SELECTOR)

    def open_share_button(self):
        self._wait_until_and_click_elem_by_xpath(self.SHARE_SELECTOR)
