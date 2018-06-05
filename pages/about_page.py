from selenium.common.exceptions import NoSuchElementException, TimeoutException

from components.about_form import AboutForm
from pages.page import Page


class AboutPage(Page):
    def __init__(self, driver, url):
        super(AboutPage, self).__init__(driver)
        self.about_form = AboutForm(self.driver)
        self.PAGE = url + "/about"

    def add_to_reletionship(self, name):
        self.about_form.marital_status_specify().click()
        self.about_form.reletionship().click()
        self.about_form.search_friend().send_keys(name)
        self.about_form.add_reletionship().click()

    def break_reletionship(self):
        self.about_form.edit_reletionship().click()
        self.about_form.break_reletionship().click()

    def clear_reletionship(self):
        try:
            self.about_form.marital_status_specify()
        except TimeoutException:
            try:
                self.about_form.reletionship_cansel_request().click()
            except TimeoutException:
                self.break_reletionship()

    def add_army_correct(self, city, unit):
        army_form = self.about_form.army_form()
        army_form.add_city_unit(city, unit)
        army_form.button_ok()
        self.about_form.close_popup()

    def add_army_no_city_correct_unit(self, unit):
        army_form = self.about_form.army_form()
        army_form.put_city('')
        army_form.add_unit(unit)
        army_form.button_ok()
        self.about_form.close_popup()

    def add_army_correct_city_incorrect_unit(self, city, unit):
        army_form = self.about_form.army_form()
        army_form.add_city(city)
        army_form.put_unit(unit)

        error = army_form.army_error()
        army_form.button_close()

        return error

    def add_army_duplicate(self, city, unit):
        self.add_army_correct(city, unit)

        army_form = self.about_form.army_form()
        army_form.add_city_unit(city, unit)
        return army_form.army_error()

    def check_army_presence(self):
        try:
            self.about_form.get_top_unit()
            return True
        except TimeoutException:
            return False

    def add_career_correct(self, city, job):
        career_form = self.about_form.career_form()
        career_form.add_city_job(city, job)
        career_form.button_ok()
        self.about_form.close_popup()

    def add_career_no_city_correct_job(self, job):
        career_form = self.about_form.career_form()
        career_form.put_city('')
        career_form.add_job(job)
        career_form.button_ok()
        self.about_form.close_popup()

    def add_career_incorrect_city_correct_job(self, city):
        career_form = self.about_form.career_form()
        career_form.put_city(city)
        return career_form.city_error()

    def add_career_correct_city_incorrect_job(self, city, job):
        career_form = self.about_form.career_form()
        career_form.add_city(city)
        career_form.put_job(job)
        return career_form.job_error()

    def add_career_duplicate(self, city, job):
        self.add_career_correct(city, job)

        career_form = self.about_form.career_form()
        career_form.add_city_job(city, job)
        return career_form.job_error()

    def check_job_presence(self):
        try:
            self.about_form.get_top_job()
            return True
        except TimeoutException:
            return False