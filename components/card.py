from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from components.base_component import BaseComponent


class CardLocators:
    def __init__(self):
        self.item = '//button[@class="item__card"]'
        self.item_img = '//img[@class="item__img"]'
        self.info_block_btn = '//img[@class="more-btn__img item__btn-img"]'
        self.player_btn = '//img[@class="item__play-btn-img item__btn-img"]'


class Card(BaseComponent):
    def __init__(self, driver):
        super(Card, self).__init__(driver)
        self.wait = WebDriverWait(self.driver, 20)
        self.locators = CardLocators()
        self.actions = ActionChains(driver)
    
    def click(self):
        """
        Кликает на карточку
        """
        card = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.item))
        )
        card.click()
    
    def move_to(self):
        """
        Наводит мышку на карточку
        """
        card = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.item))
        )
        self.actions.move_to_element(card).perform()
    
    def click_info_block_btn(self):
        """
        Кликает на кнопку карточки "Подробнее"
        """
        card = WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, self.locators.info_block_btn))
        )
        card.click()

    def click_player_btn(self):
        """
        Кликает на кнопку карточки "Воспроизвести"
        """
        card = WebDriverWait(self.driver, 30, 0.1).until(
            EC.visibility_of_element_located((By.XPATH, self.locators.player_btn))
        )
        card.click()
