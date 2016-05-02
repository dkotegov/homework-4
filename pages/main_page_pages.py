# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

_MAX_WAIT_TIME = 100

class HeadMailPage:
    def __init__(self, driver):
        self.driver = driver
        self.urls = ["https://mail.ru", "https://e.mail.ru", "https://my.mail.ru",
                "http://ok.ru", "https://games.mail.ru", "http://love.mail.ru",
                "https://news.mail.ru", "http://go.mail.ru"]

    def login(self, login, password):
        self.driver.find_element_by_id("PH_authLink").click()
        frame = WebDriverWait(self.driver, _MAX_WAIT_TIME).until(
            lambda x: x.find_element_by_css_selector(".ag-popup__frame__layout__iframe")
        )
        self.driver.switch_to_frame(frame)
        button_submit = WebDriverWait(self.driver, _MAX_WAIT_TIME).until(
            lambda x: x.find_element_by_css_selector("[data-uniqid='toolkit-4']")
        )

        input_email = self.driver.find_element_by_css_selector(".b-email__name > input:nth-child(1)")
        input_email.send_keys(login)

        input_password = self.driver.find_element_by_css_selector("div.b-input-btn__cell:nth-child(1) > :nth-child(1)")
        input_password.send_keys(password)

        button_submit.click()

    def logout(self):
        button_logout = self.driver.find_element_by_id("PH_logoutLink")
        button_logout.click()

    def get_email_user_login_correct(self):
        return self.driver.find_element_by_id("PH_user-email").text

    def click_link(self, url):
        index = self.urls.index(url)
        link = self.driver.find_elements_by_class_name("x-ph__link")[index]
        link.click()

    def click_link_registration(self):
        link = self.driver.find_element_by_id("PH_regLink")
        link.click()

    def get_text_error_login(self):
        error_panel = self.driver.find_element_by_class_name("b-panel__error")
        return error_panel.text

class PortalMenuToolbarPage:
    def __init__(self, driver):
        self.driver = driver
        self.link = ".pm-toolbar__button__inner"
        self.logo = ".pm-logo__link"

    def click_logo(self):
        link = self.driver.find_element_by_css_selector(self.logo)
        link.click()

class PortalMenuSubmenuPage:
    def __init__(self, driver):
        self.driver = driver
        self.link = "span.js-button:nth-child(5)"
        self.dropdown = "span.js-button:nth-child(5) > span:nth-child(2)"

    def move_to_link(self):
        link = self.driver.find_element_by_css_selector(self.link)
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(link).perform()

    def get_dropdown(self):
        return self.driver.find_element_by_css_selector(self.dropdown)

    def dropdown_is_open(self):
        dropdown = self.get_dropdown()
        opacity = dropdown.value_of_css_property("opacity")
        visibility = dropdown.value_of_css_property("visibility")
        display = dropdown.value_of_css_property("display")

        if opacity == "1" and visibility == "visible" and display == "block":
            return True
        return False

    def wait_show_dropdown(self):
        WebDriverWait(self.driver, _MAX_WAIT_TIME).until(
            EC.visibility_of(self.get_dropdown())
        )

class AdvertisingUnitPage:
    def __init__(self, driver):
        self.driver = driver
        self.links = [".item_small",
                      ".cols__column_large_percent-50:nth-child(2)",
                      ".yap-title-block__text"]
        self.advertising_close_button = ".yap-adtune__button"
        self.advertising = ".yap-layout__inner"

    def open_advertising(self, selector):
        link = self.driver.find_element_by_css_selector(selector)
        link.click()
        WebDriverWait(self.driver, _MAX_WAIT_TIME).until(
            lambda x: len(x.window_handles) == 2
        )
        self.driver.switch_to_window(self.driver.window_handles[1])

    def close_advertising(self):
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])

    def hide_advertising(self):
        advertising = self.driver.find_element_by_css_selector(self.advertising_close_button)
        advertising.click()

        self.driver.switch_to_window(self.driver.window_handles[1])
        self.driver.find_element_by_css_selector(".radiobox .radiobox__radio").click()
        self.driver.find_element_by_css_selector(".button").click()

        self.driver.switch_to_window(self.driver.window_handles[0])

    def get_baner_text(self):
        element = self.driver.find_element_by_css_selector(".yap-adtune-message__text")
        return WebDriverWait(self.driver, _MAX_WAIT_TIME).until(
            lambda x: element.text
        )

    def move_to_advertising(self):
        advertising = self.driver.find_element_by_css_selector(self.advertising)
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(advertising).perform()
        button = self.driver.find_element_by_class_name("yap-layout__adtune")
        WebDriverWait(self.driver, _MAX_WAIT_TIME).until(EC.visibility_of(button))


class BlockHoroPage:
    def __init__(self, driver):
        self.driver = driver
        self.date_block = ".p-prediction__date__text"
        self.title = "h1.hdr__inner"
        self.date_birth = ".p-prediction__left .link__text"

    def get_date(self):
        element = self.driver.find_element_by_css_selector(self.date_block)
        return element.text

    def get_horo_title(self):
        element = self.driver.find_element_by_css_selector(self.title)
        return element.text

    def get_zodiac_sign(self):
        return self.get_horo_title().split(" ")[-1]

    def get_date_birth(self):
        element  = self.driver.find_element_by_css_selector(self.date_birth)
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
        dayInput = self.driver.find_element_by_css_selector(self.day)
        monthInput = self.driver.find_element_by_css_selector(self.month)
        yearInput = self.driver.find_element_by_css_selector(self.year)

        dayInput.click()
        selector = ".js-date__select [data-optidx='" + str(day) + "']"
        self.driver.find_element_by_css_selector(selector).click()

        monthInput.click()
        selector = ".dropdown_month_fix [data-optidx='" + str(month - 1) + "']"
        self.driver.find_element_by_css_selector(selector).click()


    def click_all_horo(self):
        self.driver.find_element_by_css_selector(".button_top").click()


class SearchDreamPage:
    def __init__(self, driver):
        self.driver = driver
        self.searchInput = ".input__field[name=q]"
        self.searchButton = "button.margin_left_10"
        self.alphabet = ".cols__column_small_percent-50 .filter__text"

    def search_by_text(self, dream):
        search_input = self.driver.find_element_by_css_selector(self.searchInput)
        search_input.send_keys(dream)

        button = self.driver.find_element_by_css_selector(self.searchButton)
        button.click()

    def search_by_alphabet(self, index):
        alphabet = self.driver.find_elements_by_css_selector(self.alphabet)[index]
        alphabet.click()
        WebDriverWait(self.driver, _MAX_WAIT_TIME).until(
            lambda x: x.current_url.find("https://horo.mail.ru/sonnik/") != -1
        )



class LunisolarForecastPage:
    def __init__(self, driver):
        self.driver = driver
        self.date = ".p-content-item__number__inner"

    def get_date(self):
        element = self.driver.find_element_by_css_selector(self.date)
        return element.text


class SubscriptionUnitPage:
    def __init__(self, driver):
        self.driver = driver
        self.vk_link_selector = ".icon_social_vk"
        self.facebook_link_selector = ".icon_social_fb"
        self.ok_link_selector = ".icon_social_ok"

    def go_group_by_selector(self, selector):
        link = self.driver.find_element_by_css_selector(selector)
        link.click()
        WebDriverWait(self.driver, _MAX_WAIT_TIME).until(
            lambda x: len(x.window_handles) == 2
        )
        self.driver.switch_to_window(self.driver.window_handles[1])

    def go_group_vk(self):
        self.go_group_by_selector(self.vk_link_selector)

    def go_group_facebook(self):
        self.go_group_by_selector(self.facebook_link_selector)

    def go_group_ok(self):
        self.go_group_by_selector(self.ok_link_selector)

    def click_button_subscription_horo(self):
        button = self.driver.find_element_by_css_selector(".cell_right > button")
        button.click()

    def unsubscribe_horo(self):
        self.click_button_subscription_horo()
        WebDriverWait(self.driver, _MAX_WAIT_TIME).until_not(
            lambda x: self.is_subscription_horo()
        )

    def subscribe_horo(self):
        self.click_button_subscription_horo()
        WebDriverWait(self.driver, _MAX_WAIT_TIME).until(
            lambda x: self.is_subscription_horo()
        )

    def is_subscription_horo(self):
        element = self.driver.find_element_by_css_selector(".cell_right .button__text")

        return element.value_of_css_property("display") == "none"


class LadyUnitPage:
    def __init__(self, driver):
        self.driver = driver
        self.images = ".grid__item:not(.hidden_small) .photo__pic"

        self.images_slider = ".js-slider__item:not(.js-slider__clone)"

    def get_scale_image(self, index):
        element = self.driver.find_elements_by_css_selector(self.images)[index]
        return element.value_of_css_property("transform")

    def move_to_image(self, index):
        image = self.driver.find_elements_by_css_selector(self.images)[index]
        action = webdriver.ActionChains(self.driver)
        action.move_to_element(image).perform()
        #лучше способа подписатьсь на события я не нашел
        self.driver.execute_script("""
                   window.status_scale_image = false;
                   var image = $(".grid__item:not(.hidden_small) .photo__pic")[""" + str(index) + """]

                   image.addEventListener("transitionend",
                   function(e){
                        window.status_scale_image = true;
                   })
        """)
        WebDriverWait(self.driver, _MAX_WAIT_TIME).until(
            lambda x: self.driver.execute_script("return window.status_scale_image;")
        )

    def click_slider_left(self):
        slader_left_button = self.driver.find_element_by_class_name("js-slider__prev")
        slader_left_button.click()

    def click_slider_right(self):
        slader_right_button = self.driver.find_element_by_class_name("js-slider__next")
        slader_right_button.click()

    def get_transform(self, index):
        element = self.driver.find_elements_by_css_selector(self.images_slider)[index]
        return element.value_of_css_property("transform")