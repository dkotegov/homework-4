from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from components.base_component import BaseComponent
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class PlayerLocators:
    def __init__(self):
        self.watch_page = '//div[@class="watch__page"]'
        self.pause_btn = 'button.player-bar__play-btn'
        self.play_btn = "//*[@data-event='videoPlay']"
        self.player_bar = '//div[@class="player__container"]'
        self.mute_btn = "//*[@data-event='volumeOn']"
        self.sound_on_btn = "//*[@data-event='mute']"
        self.volume_btn = 'button.player-bar__volume-btn'
        self.volume_slider = '//div[@class="player-bar__volume-bar"]'
        self.share_btn = 'button.player-bar__share-btn'
        self.share_popup = '//div[@class="player-bar__share-popup"]'
        self.close_share_popup_btn = 'img.share__close-btn'
        self.close_player_btn = 'button.watch__back-btn'
        self.page_wrapper = '//div[@class="main"]'
        self.next_ep_btn = 'button.player-bar__next-content-btn'
        self.prev_ep_btn = 'button.player-bar__prev-content-btn'
        self.current_ep_lbl = 'span.player-bar__episode-number'


class Player(BaseComponent):
    def __init__(self, driver):
        self.driver = driver
        super(Player, self).__init__(driver)
        self.wait = WebDriverWait(self.driver, 20)
        self.locators = PlayerLocators()
        self.actions = ActionChains(driver)
    
    def check_appearance(self) -> bool:
        """
        Ождиает пока не откроется страница просмотра
        """
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.watch_page)))
        return element.text

    def move_to_player_bar(self):
        """
        Наводит мышку на панель плеера
        """
        player_bar = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.player_bar))
        )
        self.actions.move_to_element(player_bar).perform()

    def click_on_btn_pause(self):
        """
        Кликает на кнопку в панели плеера 'пауза'
        """
        element = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.locators.pause_btn)))
        element.click()

    def click_on_space(self):
        """
        Кликает на пробел
        """
        watch_page = WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, '//body'))
        )
        watch_page.send_keys(Keys.SPACE)

    def click_on_screen(self):
        """
        Кликает в пространство
        """
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, '//body')))
        element.click()

    def check_paused(self) -> bool:
        """
        Проверяет, поставилось ли видео на паузу
        """
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.play_btn)))
        if element:
            return True
        return False

    def click_on_sound(self):
        """
        Кликает на кнопку звука
        """
        element = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.locators.volume_btn)))
        element.click()

    def check_mute(self) -> bool:
        """
        Проверяет, выключен ли звук в видео
        """
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.mute_btn)))
        if element:
            return True
        return False

    def click_on_mute(self):
        """
        Кликает на кнопку выключенного звука
        """
        element = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.locators.volume_btn)))
        element.click()

    def check_sound(self) -> bool:
        """
        Проверяет, включен ли звук в видео
        """
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.sound_on_btn)))
        if element:
            return True
        return False

    def move_to_volume_btn(self):
        """
        Наводит мышку на кнопку звука
        """
        element = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.locators.volume_btn))
        )
        self.actions.move_to_element(element).perform()

    def check_volume_slider(self) -> bool:
        """
        Ождиает пока не откроется ползунок со звуком
        """
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.sound_on_btn)))
        if element:
            return True
        return False

    def click_on_share_btn(self):
        """
        Нажимает на кнопку 'поделиться'
        """
        element = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.locators.share_btn)))
        element.click()

    def check_share_popup(self) -> bool:
        """
        Ождиает пока не откроется попап с ссылкой на видео
        """
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.share_popup)))
        if element:
            return True
        return False

    def click_on_close_share_popup(self):
        """
        Кликает на закрытие попапа с ссылкой
        """
        element = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.locators.close_share_popup_btn)))
        element.click()

    def check_disappear_share_popup(self) -> bool:
        """
        Проверяет, есть ли попап на странице
        """
        try:
            WebDriverWait(self.driver, 3, 0.1).until(
                EC.presence_of_element_located((By.XPATH, self.locators.share_popup))
            )
        finally:
            return True

    def click_on_close_player_btn(self):
        """
        Кликает на кнопку 'назад'
        """
        element = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.locators.close_player_btn)))
        element.click()

    def check_disappear_player(self) -> bool:
        """
        Проверяет, есть ли плеер на странице
        """
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.page_wrapper)))
        if element:
            return True
        return False

    def click_on_next_ep_btn(self):
        """
        Кликает на кнопку 'следующий эпизод'
        """
        element = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.locators.next_ep_btn))
        )
        element.click()

    def check_next_ep(self) -> bool:
        """
        Проверяет, включился ли следующий эпизод
        """
        element = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.locators.current_ep_lbl)))
        if element:
            return element.text == "S1:E2"
        return False

    def click_on_prev_ep_btn(self):
        """
        Кликает на кнопку 'предыдущий эпизод'
        """
        element = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.locators.prev_ep_btn))
        )
        element.click()

    def check_prev_ep(self) -> bool:
        """
        Проверяет, включился ли предыдущий эпизод
        """
        element = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.locators.current_ep_lbl)))
        if element:
            return element.text == "S1:E1"
        return False

