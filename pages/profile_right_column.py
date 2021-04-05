from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from pages.base_component import Component
from collections import namedtuple


class ProfileRightColumn(Component):
    __Skills = namedtuple('Skills', ['value', 'edit_btn', 'text_field', 'check_mark', 'cross_mark'])
    SKILLS = __Skills(
        '//span[contains(@class, "profile__skills")]',
        '//img[contains(@class, "profile__skills-editicon")]',
        '//div[contains(.,"Навыки")]/following-sibling::textarea[@class="block"][1]',
        '//span[contains(text(), "Навыки")]/following-sibling::img[@src="assets/check-mark.svg"]',
        '//span[contains(text(), "Навыки")]/following-sibling::img[@src="assets/x-mark.svg"]'
    )
    __Interests = namedtuple('Interests', ['value', 'edit_btn', 'text_field', 'check_mark', 'cross_mark'])
    INTERESTS = __Interests(
        '//span[contains(@class, "profile__interests")]',
        '//img[contains(@class, "profile__interests-editicon")]',
        '//div[contains(.,"Интересы")]/following-sibling::textarea[@class="block"][1]',
        '//span[contains(text(), "Интересы")]/following-sibling::img[@src="assets/check-mark.svg"]',
        '//span[contains(text(), "Интересы")]/following-sibling::img[@src="assets/x-mark.svg"]'
    )
    __Education = namedtuple('Education', ['value', 'edit_btn', 'text_field', 'check_mark', 'cross_mark'])
    EDUCATION = __Education(
        '//span[contains(@class, "profile__education")]',
        '//img[contains(@class, "profile__education-editicon")]',
        '//div[contains(.,"Образование")]/following-sibling::textarea[@class="block"][1]',
        '//span[contains(text(), "Образование")]/following-sibling::img[@src="assets/check-mark.svg"]',
        '//span[contains(text(), "Образование")]/following-sibling::img[@src="assets/x-mark.svg"]'
    )
    __Job = namedtuple('Job', ['value', 'edit_btn', 'text_field', 'check_mark', 'cross_mark'])
    JOB = __Job(
        '//span[contains(@class, "profile__job")]',
        '//img[contains(@class, "profile__job-editicon")]',
        '//div[contains(.,"Работа")]/following-sibling::textarea[@class="block"][1]',
        '//span[contains(text(), "Работа")]/following-sibling::img[@src="assets/check-mark.svg"]',
        '//span[contains(text(), "Работа")]/following-sibling::img[@src="assets/x-mark.svg"]'
    )
    __Aims = namedtuple('Aims', ['value', 'edit_btn', 'text_field', 'check_mark', 'cross_mark'])
    AIMS = __Aims(
        '//span[contains(@class, "profile__aims")]',
        '//img[contains(@class, "profile__aims-editicon")]',
        '//div[contains(.,"Цели")]/following-sibling::textarea[@class="block"][1]',
        '//span[contains(text(), "Цели")]/following-sibling::img[@src="assets/check-mark.svg"]',
        '//span[contains(text(), "Цели")]/following-sibling::img[@src="assets/x-mark.svg"]'
    )

    UPDATE_CONFIRMATION = '//div[@class="mtoasts__toast"]/p[contains(text(), "Вы отредактировали профиль")]'
    CLOSE_CONFIRMATION = '//div[@class="closeWrapper"]/span[@class="close"]'

    def click_edit(self, field: namedtuple):
        self._wait_until_clickable(field.edit_btn).click()

    def clear_textfield(self, field):
        target = self._wait_until_visible(field.text_field)
        ActionChains(self.driver).click(target)\
            .key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)\
            .send_keys(Keys.DELETE).perform()

    def fill_textfield(self, field, text):
        self.clear_textfield(field)
        self._wait_until_visible(field.text_field).send_keys(text)

    def click_check_mark(self, field):
        self._wait_until_clickable(field.check_mark).click()

    def click_cross_mark(self, field):
        self._wait_until_clickable(field.cross_mark).click()

    def get_value(self, field):
        return self._wait_until_visible(field.value).text

    def wait_for_update_confirmation(self):
        self._wait_until_preset(self.UPDATE_CONFIRMATION)
