from steps.BaseSteps import BaseSteps


class LettersHeader(BaseSteps):
    EMAIL = '//span[@id="PH_authMenu_button"]'

    @property
    def email(self):
        return self.wait_until_and_get_elem_by_xpath(self.EMAIL).text
