'''

class AllForm(BaseComponent):
    NAME = "//input[@name='fr.name']"
    SURNAME = "//input[@name='fr.surname']"
    SAVE_BUTTON = "//input[@id='hook_FormButton_button_savePopLayerEditUserProfileNew']"
    CLOSE_BUTTON = "//input[@id='buttonId_button_close']"
    
    PROFILE1 = "//a[@class='compact-profile_a ellip-i']"
    PROFILE2 = "//a[@class='mctc_name_tx bl']"



    def test1 (self):
        #зайти в настройки и нажать изменить личные данные

        self.driver.find_element_by_xpath(self.NAME).send_keys("Имя1")
        self.driver.find_element_by_xpath(self.SURNAME).send_keys("Фамилия1")
        self.driver.find_element_by_xpath(self.SAVE_BUTTON).click()

        self.driver.find_element_by_xpath(self.CLOSE_BUTTON).click()

        # вроверить в настройках
        self.driver.find_element_by_xpath(self.PROFILE1) # значение проверить "Имя1 Фамилия1"
        self.driver.find_element_by_xpath(self.PROFILE1).click()

        self.driver.find_element_by_xpath(self.PROFILE2)  # значение проверить


    ERROR1 = "//span[@class='input-e']"

    def test2(self):
        self.driver.find_element_by_xpath(self.NAME).send_keys("Имя_2")
        self.driver.find_element_by_xpath(self.SURNAME).send_keys("Фамилия_2")
        self.driver.find_element_by_xpath(self.SAVE_BUTTON).click()

        e1 = self.driver.find_element_by_xpath(self.ERROR1)[1]  # значение проверить "Пожалуйста, используйте только буквы."
        e2 = self.driver.find_element_by_xpath(self.ERROR1)[2]  # значение проверить "Пожалуйста, используйте только буквы."


    DAYS = "//select[@id='field_bday']"
    DAY = "//option[@value='5']"
    DAY_ERROR = "//option[@value='29']"

    MONTHS = "//select[@id='field_bmonth']"
    MONTH = "//option[@value='3']"
    MONTH_ERROR = "//option[@value='2']"

    YEARS = "//select[@id='field_byear']"
    YEAR = "//option[@value='1996']"
    YEAR_ERROR = "//option[@value='2001']"

    DATE = "//div[@value='user-profile_i_value ellip']"

    def test3(self):
        self.driver.find_element_by_xpath(self.DAYS).click()
        self.driver.find_element_by_xpath(self.DAY).click()

        self.driver.find_element_by_xpath(self.MONTHS).click()
        self.driver.find_element_by_xpath(self.MONTH).click()

        self.driver.find_element_by_xpath(self.YEARS).click()
        self.driver.find_element_by_xpath(self.YEAR).click()

        self.driver.find_element_by_xpath(self.CLOSE_BUTTON).click()

        # перейти в профиль
        self.driver.find_element_by_xpath(self.PROFILE1).click()

        d = self.driver.find_element_by_xpath(self.DATE)[1]  # значение проверить "5 марта 1996 (22 года)"

    def test4(self):
        self.driver.find_element_by_xpath(self.DAYS).click()
        self.driver.find_element_by_xpath(self.DAY_ERROR).click()

        self.driver.find_element_by_xpath(self.MONTHS).click()
        self.driver.find_element_by_xpath(self.MONTH_ERROR).click()

        self.driver.find_element_by_xpath(self.YEARS).click()
        self.driver.find_element_by_xpath(self.YEAR_ERROR).click()


        e3 = self.driver.find_element_by_xpath(self.ERROR1)[1]  # значение проверить "День вашего рождения указан некорректно."


    NUMBER = "//input[@name='st.layer.code']"
    OK_BUTTON = "//input[@class='button-pro form-actions_yes']"

    def test5(self):
        self.driver.find_element_by_xpath(self.NUMBER).send_keys("9999977771")
        self.driver.find_element_by_xpath(self.OK_BUTTON).click()

        self.driver.find_element_by_xpath(self.OK_BUTTON)  # значение проверить "Подтвердить код"


    NUMBER_ERROR = "//div[@id='formErrorsContainer']"
    def test6(self):
        self.driver.find_element_by_xpath(self.NUMBER).send_keys("999997777")
        self.driver.find_element_by_xpath(self.OK_BUTTON).click()

 #       self.driver.find_element_by_xpath(self.NUMBER_ERROR)  # значение проверить "Ошибки: ..??"
    '''