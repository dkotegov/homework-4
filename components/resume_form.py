from selenium.webdriver.support.wait import WebDriverWait

from components.base_component import BaseComponent


class ResumeForm(BaseComponent):
    PLACE = "//div[@class='about-candidate']/div[2]"
    DESCRIPTION = "//div[@class='job-description']/div[2]"
    SKILLS = "//div[@class='job-description']/div[5]"

    def get_description(self) -> str:
        """
        Возвращает описание со страницы резюме
        :return description: описание резюме
        """
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.DESCRIPTION)
        ).text

    def get_place(self) -> str:
        """
        Возвращает должность со страницы резюме
        :return place: желаемая должность
        """
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.PLACE)
        ).text

    def get_skills(self) -> str:
        """
        Возвращает новыки со страницы резюме
        :return skills: навыки
        """
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SKILLS)
        ).text
