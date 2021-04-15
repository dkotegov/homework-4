from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from components.base_component import BaseComponent
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


class NavbarLocators:
    def __init__(self):
        self.login_menu_btn = '//img[@class="header__arrow"]'
        self.login_btn = '//*[contains(text(),"Вход")]'
        self.exit_btn = '//*[contains(text(),"Выйти")]'
        self.reg_btn = '//*[contains(text(),"Регистрация")]'
        self.my_list_btn = '//a[@href="/mylist"]'
        self.search_magnifier_to_open = '//img[@class="header__search-img control__item"]'
        self.search_magnifier_to_search = '//img[@class="search-line__img"]'
        self.search_line = '//div[@class="search-line search-line_visible"]'
        self.search_line_hidden = '//div[@class="search-line hidden"]'
        self.search_line_input = '//input[@class="search-line__input"]'
        self.search_prompt_window = '//div[@class="prompt-window"]'
        self.prompt_label = '//a[@class="prompt-window__label"]'
        self.avatar = '//img[@class="header__avatar"]'


class NavbarForm(BaseComponent):
    def __init__(self, driver):
        super(NavbarForm, self).__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.locators = NavbarLocators()
        self.actions = ActionChains(driver)

    def click_login_menu(self):
        """
        Вызывает подменю для входа
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.element_to_be_clickable((By.XPATH, self.locators.login_menu_btn))
        )
        submit.click()

    def click_login_button(self):
        """
        Кликает на кнопку "Вход"
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.login_btn))
        )
        submit.click()

    def click_exit_button(self):
        """
        Кликает на кнопку "Вход"
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.exit_btn))
        )
        submit.click()
    
    def click_reg_button(self):
        """
        Кликает на кнопку "Регистрация"
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.reg_btn))
        )
        submit.click()
    
    def click_search_magnifier_to_open(self):
        """
        Кликает на лупу поиска
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.search_magnifier_to_open))
        )
        submit.click()
    
    def click_search_magnifier_to_search(self):
        """
        Кликает на лупу поиска для поиска
        """
        submit = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.search_magnifier_to_search))
        )
        # due to ElementClickInterceptedException
        self.driver.execute_script("arguments[0].click();", submit)
    
    def press_Enter_to_search(self):
        """
        Нажимает Enter в строке поиска для её закрытия
        """
        search_input = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.search_line_input))
        )
        search_input.send_keys(Keys.ENTER)
    
    def set_search_line_text(self, text: str):
        """
        Вводит текст в поле поиска
        """
        search_input = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.search_line_input))
        )
        search_input.send_keys(text)
    
    def choise_prompt_label(self):
        """
        Кликает на лупу поиска для закрытия строки поиска
        """
        label = WebDriverWait(self.driver, 30, 0.1).until(
            EC.presence_of_element_located((By.XPATH, self.locators.prompt_label))
        )
        label.click()

    def check_auth_is_right(self) -> bool:
        """
        Ождиает пока не откроется главная страница на которой будет вкладка "Мой список"
        """
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.my_list_btn)))
        return element.text

    def check_exit_is_right(self) -> bool:
        """
        Ождиает пока не откроется главная страница на которой будет вкладка "Мой список"
        """
        try:
            element = self.wait.until(
                EC.invisibility_of_element_located((By.XPATH, self.locators.exit_btn))
            )
        except TimeoutException:
            return False
        return True
    
    def check_search_line_appearance(self) -> bool:
        """
        Ождиает пока не откроется строка поиска
        """
        try:
            element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.locators.search_line)))
        except TimeoutException:
            return False
        return True
    
    def check_search_line_disappearance(self) -> bool:
        """
        Ождиает пока не закроется строка поиска
        """
        try:
            element = self.wait.until(
                EC.presence_of_element_located((By.XPATH, self.locators.search_line_hidden)))
        except TimeoutException:
            return False
        return True
    

    def check_search_prompt_window_appearance(self) -> bool:
        """
        Ождиает пока не откроется окно с подсказками поиска
        """
        try:
            element = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, self.locators.search_prompt_window)))
        except TimeoutException:
            return False
        return True

    def current_avatar(self):
        element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.locators.avatar)))
        return element.get_attribute("src")
