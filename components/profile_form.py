from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base_component import BaseComponent


class ProfileFormLocators:
    def __init__(self):
        self.root = '//div[@class="main-page"]'
        self.page_title = '//div[@class="profile-title"]'
        self.personal_info_btn = '//div[@class="btn-href"][0]'
        self.my_res_or_vac_btn = '//div[@class="btn-href"][1]'
        self.chosen_btn = '//div[@class="btn-href"][2]'
        self.responses_btn = '//div[@class="btn-href"][3]'

        self.personal_name = '//div[@id="name"]'
        self.personal_surname = '//div[@id="surname"]'
        self.personal_email = '//div[@id="email"]'

        self.delete_btn = '//div[@id="deleteAccount"]'
        self.profile_navbar_btns = '//div[@class="btn-href"]'

        self.empty_list = '//div[@class="main__list-profile"]'
        self.cards_list = '//div[@class="main-list-row"]'
        self.responses_list = '//div[@class="response"]'
        self.fav_list = '//div[@class="list-row"]'

        self.open_card_btn = '//div[@class="main__buttons_one"]'
        self.edit_card_btn = '//div[@class="main__buttons_two"]'

        self.vacancy_link_resp = '//a[@class="response-row-info__vacancy-link"]'
        self.company_link_resp = '//a[@class="response-row-info__company-link"]'
        self.resume_link_resp = '//a[@class="response-row-info__resume-link"]'

        self.upload_avatar_btn = '//input[@id="avatar"]'
        self.upload_avatar = '//div[@id="logoProfile"]'

        self.error_field = '//div[@class="error"]'
        self.error_phone = '//span[@class="error"]'
        self.list = '//div[@class="pers-list"]'
        self.edit_btn = '//a[@href="/profile"]'
        self.edited_input = '//input[@class="pers-list-row__input"]'

        self.my_first_resume = '(//div[@class="main-list-row"])[1]'
        self.my_first_resume_edit = '(//div[text()="Изменить резюме"])[1]'

        self.favorite_title = '(//div[@class="list-row-description__name"])/a'
        self.favorite_description = '//div[@class="list-row-description__specialism"]'

        self.text_fields = '//div[@class="pers-list-row__input-field"]'

        self.response_item = '//div[@class="response-row-info"]'
        self.response_item_title = '//a[@class="response-row-info__vacancy-link"]'



class ProfileForm(BaseComponent):
    def __init__(self, driver):
        super(ProfileForm, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)

        self.locators = ProfileFormLocators()

    def is_open(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.locators.page_title)))
            return True
        except:
            return False

    def click_to_delete_btn(self):
        delete = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.delete_btn))
        )
        delete.click()

    def check_profile_name(self):
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.personal_name)))
        return element.text

    def check_profile_surname(self):
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.personal_surname)))
        return element.text

    def check_profile_email(self) -> bool:
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.personal_email)))
        return element.text

    def click_to_my_cards(self):
        my_resumes = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.profile_navbar_btns))
        )
        my_resumes[1].click()

    def click_to_my_profile_info(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.profile_navbar_btns))
        )[0].click()

    def check_page_with_cards_is_open(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.locators.cards_list)))
            return True
        except TimeoutException:
            return False

    def check_page_with_responses_is_open(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.locators.responses_list)))
            return True
        except TimeoutException:
            return False

    def check_page_with_fav_is_open(self):
        try:
            self.wait.until(
                EC.visibility_of_all_elements_located((By.XPATH, self.locators.fav_list)))
            return True
        except:
            return False

    def click_to_my_response(self):
        my_responses = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.profile_navbar_btns))
        )
        my_responses[3].click()

    def click_to_my_fav(self):
        my_responses = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.profile_navbar_btns))
        )
        my_responses[2].click()

    def click_to_open_card(self):
        card_btn = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.open_card_btn))
        )
        card_btn[0].click()

    def click_to_edit_card(self):
        card_btn = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.edit_card_btn))
        )
        card_btn[0].click()

    def open_vacancy_responses(self):
        vac_btn = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.vacancy_link_resp))
        )
        vac_btn[0].click()

    def open_company_responses(self):
        company_btn = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.company_link_resp))
        )
        company_btn[0].click()

    def open_resume_responses(self):
        company_btn = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.resume_link_resp))
        )
        company_btn[0].click()

    def click_to_load_btn(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.upload_avatar_btn))
        )

    def check_avatar_loaded(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.upload_avatar))
        )

    def check_error(self):
        try:
            error = WebDriverWait(self.driver, 3, 0.1).until(
                EC.presence_of_element_located((By.XPATH, self.locators.error_field))
            )
            return error.text
        except TimeoutException:
            return ''


    def check_error_phone(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.error_phone))
        )

    def wait_for_list(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.list))
        )

    def click_to_edit_or_save_name(self, field_number):
        self.wait_for_list()
        btn = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.edit_btn))
        )
        btn[field_number].click()

    def get_edited_field(self):
        self.wait_for_list()
        return WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.edited_input))
        )

    def get_text_fields(self, field_number):
        self.wait_for_list()
        fields = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.text_fields))
        )

        return fields[field_number].get_attribute("innerText")


    def clear(self, element):
        value = element.get_attribute('value')
        if len(value) > 0:
            for char in value:
                element.send_keys(Keys.BACK_SPACE)

    def click_first_my_resume_edit(self):
        self.click_to_my_cards()
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, self.locators.my_first_resume_edit))
        ).click()

    def get_favorite_data(self):
        return {
            'title': self.get_field(self.locators.favorite_title),
            'description': self.get_field(self.locators.favorite_description)
        }

    def get_responses(self):
        resp = self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.response_item_title))
        )

        return resp
