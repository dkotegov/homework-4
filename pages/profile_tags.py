from pages.base_component import Component


class ProfileTags(Component):
    TAGS_BTN = '//button[@id="editTagsBtn"]'
    TAGS_MODAL = '//div[@id="modalTags"]'
    MODAL_CPP_TAG = '//div[@class="tabTags"]/label/span[contains(text(), "C++")]'
    MODAL_GOLANG_TAG = '//div[@class="tabTags"]/label/span[contains(text(), "Golang")]'
    HELP_TEXT = '//span[@class="helpText"]'
    PROFILE_TAG = '//div[@class="selectedTagsWrapper"]/label/span'
    CLOSE_TAGS_MODAL = '//button[@id="closeTagsModal"]'
    TAGS_MODAL_CROSS = '//span[@class="modal__close"]'
    UPDATE_CONFIRMATION = '//div[@class="mtoasts__toast"]/p[contains(text(), "Вы успешно применили тэги")]'
    CLOSE_CONFIRMATION = '//div[@class="closeWrapper"]/span[@class="close"]'

    def open_tags_modal(self):
        self._wait_until_clickable(self.TAGS_BTN).click()

    def wait_for_tags_modal(self):
        self._wait_until_visible(self.TAGS_MODAL)

    def get_modal_visibility(self):
        return self._is_element_visible(self.TAGS_MODAL)

    def click_cpp_tag(self):
        self._wait_until_clickable(self.MODAL_CPP_TAG).click()

    def click_golang_tag(self):
        self._wait_until_clickable(self.MODAL_GOLANG_TAG).click()

    def get_cpp_tag_bg_color(self):
        return self._find_element(self.MODAL_CPP_TAG).value_of_css_property('background-color')

    def get_golang_tag_bg_color(self):
        return self._find_element(self.MODAL_GOLANG_TAG).value_of_css_property('background-color')

    def get_help_text(self):
        return self._find_element(self.HELP_TEXT).text

    def click_commit_tags_update(self):
        self._wait_until_clickable(self.CLOSE_TAGS_MODAL).click()

    def wait_for_update_confirmation(self):
        self._wait_until_visible(self.UPDATE_CONFIRMATION)

    def close_update_confirmation(self):
        self._wait_until_clickable(self.CLOSE_CONFIRMATION).click()

    def get_tags(self):
        return [x.text for x in self._find_elements(self.PROFILE_TAG)]

    def click_close_modal(self):
        self._wait_until_clickable(self.TAGS_MODAL_CROSS).click()

    def wait_for_modal_closing(self):
        self._wait_until_invisible(self.TAGS_MODAL)
