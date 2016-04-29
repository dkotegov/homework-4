# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

_MAX_WAIT_TIME = 100

class HeadMailPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, login, password):
        self.driver.find_element_by_id("PH_authLink").click()
        method = lambda x :self.driver.find_elements_by_css_selector(".ag-popup__frame__layout__iframe")
        frame = WebDriverWait(self.driver, _MAX_WAIT_TIME).until(method)
        self.driver.switch_to_frame(frame[0])
        button_submit = WebDriverWait(self.driver, _MAX_WAIT_TIME).until(lambda x: self.driver.find_elements_by_css_selector("[data-uniqid='toolkit-4']"))

        input_email = self.driver.find_elements_by_css_selector(".b-email__name > input:nth-child(1)")[0]
        input_email.send_keys(login)

        input_password = self.driver.find_elements_by_css_selector("div.b-input-btn__cell:nth-child(1) > :nth-child(1)")[0]
        input_password.send_keys(password)

        button_submit[0].click()

    def logout(self):
        button_logout = self.driver.find_element_by_id("PH_logoutLink")
        button_logout.click()

    def get_email_user_login_correct(self):
        return self.driver.find_element_by_id("PH_user-email").text

    def click_link(self, index):
        link = self.driver.find_elements_by_class_name("x-ph__link")[index]
        link.click()

    def click_link_registration(self):
        link = self.driver.find_element_by_id("PH_regLink")
        link.click()

class PortalMenuToolbarPage:
    def __init__(self, driver):
        self.driver = driver
        self.link = ".pm-toolbar__button__inner"
        self.logo = ".pm-logo__link"

    def move_to_link(self):
        link = self.driver.find_elements_by_css_selector(self.link)[0]
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(link).perform()

    def get_background_color_link(self):
        link = self.driver.find_elements_by_css_selector(self.link)[0]
        return link.value_of_css_property("background-color")

    def click_logo(self):
        link = self.driver.find_elements_by_css_selector(self.logo)[0]
        link.click()

class PortalMenuSubmenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.link = "span.js-button:nth-child(5)"
        self.dropdown = "span.js-button:nth-child(5) > span:nth-child(2)"

    def move_to_link(self):
        link = self.driver.find_elements_by_css_selector(self.link)[0]
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(link).perform()

    def get_dropdown(self):
        return self.driver.find_elements_by_css_selector(self.dropdown)[0]

    def dropdown_is_open(self):
        dropdown = self.get_dropdown()
        opacity = dropdown.value_of_css_property("opacity")
        visibility = dropdown.value_of_css_property("visibility")
        display = dropdown.value_of_css_property("display")

        if opacity == "1" and visibility == "visible" and display == "block":
            return True
        return False

class AdvertisingUnitPage:
    def __init__(self, driver):
        self.driver = driver
        self.links = [".item_small",
                      ".cols__column_large_percent-50:nth-child(2)",
                      ".yap-title-block__text"]
        self.advertising_close_button = ".yap-adtune__button"
        self.advertising = ".yap-layout__inner"

    def click_link(self, selector):
        link = self.driver.find_elements_by_css_selector(selector)[0]
        link.click()

    def hide_advertising(self):
        advertising = self.driver.find_elements_by_css_selector(self.advertising_close_button)[0]
        advertising.click()

        self.driver.switch_to_window(self.driver.window_handles[1])
        self.driver.find_elements_by_css_selector(".radiobox .radiobox__radio")[0].click()
        self.driver.find_elements_by_css_selector(".button")[0].click()

        self.driver.switch_to_window(self.driver.window_handles[0])

    def get_baner_text(self):
        element = self.driver.find_elements_by_css_selector(".yap-adtune-message__text")[0]
        return element.text

    def move_to_advertising(self):
        advertising = self.driver.find_elements_by_css_selector(self.advertising)[0]
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(advertising).perform()
        button = self.driver.find_elements_by_class_name("yap-layout__adtune")[0]
        WebDriverWait(self.driver, _MAX_WAIT_TIME).until(EC.visibility_of(button))


class BlockHoroPage:
    def __init__(self, driver):
        self.driver = driver
        self.date_block = ".p-prediction__date__text"
        self.title = "h1.hdr__inner"
        self.date_birth = ".p-prediction__left .link__text"

    def get_date(self):
        element = self.driver.find_elements_by_css_selector(self.date_block)[0]
        return element.text

    def get_horo_title(self):
        element = self.driver.find_elements_by_css_selector(self.title)[0]
        return element.text

    def get_date_birth(self):
        element  = self.driver.find_elements_by_css_selector(self.date_birth)[0]
        return element.text

    def click_button_choice_date(self, index):
        selector = ".filter__item_underlined"
        link = self.driver.find_elements_by_css_selector(selector)[index]
        link.click()



class ZodiacSignPage:
    def __init__(self, driver):
        self.driver = driver
        self.day = ".js-date__select[data-range='day']"
        self.month = ".js-date__select[data-range='month']"
        self.year = ".js-date__select[data-range='year']"

    def select_date(self, day, month, year):
        dayInput = self.driver.find_elements_by_css_selector(self.day)[0]
        monthInput = self.driver.find_elements_by_css_selector(self.month)[0]
        yearInput = self.driver.find_elements_by_css_selector(self.year)[0]

        dayInput.click()
        selector = ".js-date__select [data-optidx='" + str(day) + "']"
        self.driver.find_elements_by_css_selector(selector)[0].click()

        monthInput.click()
        selector = ".dropdown_month_fix [data-optidx='" + str(month - 1) + "']"
        self.driver.find_elements_by_css_selector(selector)[0].click()


    def click_all_horo(self):
        self.driver.find_elements_by_css_selector(".button_top")[0].click()


class SearchDreamPage:
    def __init__(self, driver):
        self.driver = driver
        self.searchInput = ".input__field[name=q]"
        self.searchButton = "button.margin_left_10"
        self.alphabet = ".cols__column_small_percent-50 .filter__text"

    def search_by_text(self, dream):
        search_input = self.driver.find_elements_by_css_selector(self.searchInput)[0]
        search_input.send_keys(dream)

        button = self.driver.find_elements_by_css_selector(self.searchButton)[0]
        button.click()

    def search_by_alphabet(self, index):
        alphabet = self.driver.find_elements_by_css_selector(self.alphabet)[index]
        alphabet.click()


class LunisolarForecastPage:
    def __init__(self, driver):
        self.driver = driver
        self.date = ".p-content-item__number__inner"

    def get_date(self):
        element = self.driver.find_elements_by_css_selector(self.date)[0]
        return element.text


class SubscriptionUnitPage:
    def __init__(self, driver):
        self.driver = driver
        self.vk_link_selector = ".icon_social_vk"
        self.facebook_link_selector = ".icon_social_fb"
        self.ok_link_selector = ".icon_social_ok"

    def go_group_vk(self):
        link = self.driver.find_elements_by_css_selector(self.vk_link_selector)[0]
        link.click()

    def go_group_facebook(self):
        link = self.driver.find_elements_by_css_selector(self.facebook_link_selector)[0]
        link.click()

    def go_group_ok(self):
        link = self.driver.find_elements_by_css_selector(self.ok_link_selector)[0]
        link.click()

    def click_button_subscription_horo(self):
        button = self.driver.find_elements_by_css_selector(".cell_right > button")[0]
        button.click()

    def is_subscription_horo(self):
        element = self.driver.find_elements_by_css_selector(".cell_right .button__text")[0]

        if element.value_of_css_property("display") == "none":
            return True
        return False

class LadyUnitPage:
    def __init__(self, driver):
        self.driver = driver
        self.images = ".grid__item:not(.hidden_small) .photo__pic"

        self.images_slider = ".js-slider__item"

    def get_scale_image(self, index):
        element = self.driver.find_elements_by_css_selector(self.images)[index]
        return element.value_of_css_property("transform")

    def move_to_image(self, index):
        image = self.driver.find_elements_by_css_selector(self.images)[index]
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(image).perform()

    def click_slider_left(self):
        slader_left_button = self.driver.find_elements_by_class_name("js-slider__prev")[0]
        slader_left_button.click()

    def click_slider_right(self):
        slader_right_button = self.driver.find_elements_by_class_name("js-slider__next")[0]
        slader_right_button.click()

    def get_transform(self, index):
        element = self.driver.find_elements_by_css_selector(self.images_slider)[index + 2]
        return element.value_of_css_property("transform")



