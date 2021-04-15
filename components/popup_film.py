from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from components.base_component import BaseComponent


class AuthLocators:
    def __init__(self):
        self.root = '//div[@class="content__info-block-wrapper"]'
        # self.film_button = '//div[@class="content__slider-item"]/button'
        self.popup_button = '//a[@class="preview__btn info-btn"]'
        self.popup_like_button = '//button[@class="modal__like-btn like-btn item__btn"]'
        self.popup_like_button_image = '//button[@class="modal__like-btn like-btn item__btn"]/img'
        self.popup_dislike_button = '//button[@class="modal__dislike-btn dislike-btn item__btn"]'
        self.popup_dislike_button_image = '//button[@class="modal__dislike-btn dislike-btn item__btn"]/img'
        self.genre_anchor = '//a[@class="genre-item__value item-link"]'
        self.actor_anchor = '//a[@class="cast-item__link item-link"]'
        self.director_anchor = '//a[@class="director-item__value item-link"]'
        self.same_film = '//div[@class="content__grid similar__grid"]/div/button'
        self.popup_paragraphs = '//*[@class="modal__headline margin"]'
        self.season_button = '//button[@class="modal__season-button"]'
        self.series_button = '//div[@class="modal__grid modal__season-grid"]/div/div/button'
        self.popup = '//div[@class="content-popup"]'
        self.popup_add_my_list_button = '//button[@class="modal__add-btn add-btn item__btn"]'
        self.popup_add_my_list_button_image = '//button[@class="modal__add-btn add-btn item__btn"]/img'


class PopupFilm(BaseComponent):
    def __init__(self, driver):
        super(PopupFilm, self).__init__(driver)

        self.wait = WebDriverWait(self.driver, 20)
        self.locators = AuthLocators()
        self.like_image_src = ""
        self.dislike_image_src = ""
        self.same_film_id = ""
        self.season_number = ""
        self.player_url = ""
        self.add_my_list_image_src = ""
        self.genre_url = "https://www.flicksbox.ru/movies"
        self.actor_url = "https://www.flicksbox.ru/actor"
        self.director_url = "https://www.flicksbox.ru/director"
    
    def check_appearance(self) -> bool:
        """
        Ождиает пока не откроется информационный попап
        """
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.popup)))
        return element.text

    def open_popup(self):
        """
        Открывает попап фильма
        """
        film = WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, self.locators.popup_button))
        )
        film.click()

    def click_like_button(self):
        """
        Нажимает на кнопку Like
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.locators.popup_like_button))
        )
        self.like_image_src = submit.get_attribute("src")
        submit.click()

    def check_like_clicked(self) -> bool:
        """
        Проверяет, изменилась ли картинка на кнопке Like после нажатия
        """
        is_liked = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.popup_like_button_image))
        )
        return is_liked.get_attribute("src") != self.like_image_src

    def click_add_my_list_button(self):
        """
        Нажимает на кнопку Like
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.locators.popup_add_my_list_button))
        )
        self.add_my_list_image_src = submit.get_attribute("src")
        submit.click()

    def check_add_my_list_clicked(self) -> bool:
        """
        Проверяет, изменилась ли картинка на кнопке Like после нажатия
        """
        is_added = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.popup_add_my_list_button_image))
        )
        return is_added.get_attribute("src") != self.add_my_list_image_src

    def click_dislike_button(self):
        """
        Нажимает на кнопку DisLike
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.locators.popup_dislike_button))
        )
        self.dislike_image_src = submit.get_attribute("src")
        submit.click()

    def check_dislike_clicked(self) -> bool:
        """
        Проверяет, изменилась ли картинка на кнопке DisLike после нажатия
        """
        is_liked = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.popup_dislike_button_image))
        )
        return is_liked.get_attribute("src") != self.dislike_image_src

    def click_genre_anchor(self):
        """
        Нажимает на жанр
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.genre_anchor))
        )
        submit.click()

    def check_genre_redirect(self) -> bool:
        """
        Проверяет, открыта ли страница жанра
        """
        is_liked = self.wait.until(
            lambda driver: self.genre_url in driver.current_url
        )
        return is_liked

    def click_actor_anchor(self):
        """
        Нажимает на актера
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.actor_anchor))
        )
        submit.click()

    def check_actor_redirect(self) -> bool:
        """
        Проверяет, открыта ли страница актера
        """
        is_liked = self.wait.until(
            lambda driver: self.actor_url in driver.current_url
        )
        return is_liked

    def click_director_anchor(self):
        """
        Нажимает на режиссера
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.director_anchor))
        )
        submit.click()

    def check_director_redirect(self) -> bool:
        """
        Проверяет, открыта ли страница режиссера
        """
        is_liked = self.wait.until(
            lambda driver: self.director_url in driver.current_url
        )
        return is_liked

    def is_same_films(self) -> bool:
        """
        Проверяет, есть ли похожие фильмы в попвпе
        """
        paragraphs = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.popup_paragraphs))
        )
        for elem in paragraphs:
            if elem.text == "Похожее":
                return True
        return False

    def click_same_film(self):
        """
        Нажимает на фильм из "Похожее"
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.same_film))
        )
        self.same_film_id = submit.get_attribute("data-id")
        submit.click()

    def check_same_film_name(self) -> bool:
        """
        Проверяет, открыт ои попар фильма
        """
        is_liked = self.wait.until(
            lambda driver: "mid=" + self.same_film_id in driver.current_url
        )
        self.same_film_id = ""
        return is_liked

    def click_season_if_exist(self) -> bool:
        """
        Нажимает на сезон, если сезонов больше чем 1
        """
        paragraphs = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locators.season_button))
        )
        if len(paragraphs) >= 2:
            self.season_number = paragraphs[1].text
            paragraphs[1].click()
            return True
        else:
            return False

    def check_season_changed(self) -> bool:
        """
        Проверяет, изменилтсь ли серии в попапе
        """
        seria = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.series_button))
        )
        if seria.get_attribute("data-season") == self.season_number:
            is_season_changed = True
        else:
            is_season_changed = False
        self.season_number = ""
        return is_season_changed

    def click_episode(self):
        """
        Нажимает на кнопку серию
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.series_button))
        )
        serial_id = submit.get_attribute("data-id")
        serial_season = submit.get_attribute("data-season")
        serial_episode = submit.get_attribute("data-episode")
        self.player_url = 'https://www.flicksbox.ru/watch/' + serial_id + '?season=' + serial_season + '&episode=' + serial_episode
        submit.click()

    def check_player_is_open(self) -> bool:
        """
        Проверяет, отерыт ли плеер
        """
        is_redirect = self.wait.until(
            lambda driver: self.player_url in driver.current_url
        )
        self.player_url = ""
        return is_redirect
