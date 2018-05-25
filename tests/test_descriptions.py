from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.photo_manipulation import PhotoManipulationTest
from util import config


class PhotoDescriptionTest(PhotoManipulationTest):
    DESCRIPTION_LIMIT = 255

    DESCRIPTION_ADD_LNK = 'plp_descrAddLnk'
    DESCRIPTION_CHANGE_LNK = 'plp_descrChgLnk'

    DESCRIPTION_INPUT_ID = 'plp_descrInp'
    DESCRIPTION_SAVE_BUTTON_ID = 'plp_descrInpBtn'
    DESCRIPTION_CANCEL_BUTTON_ID = 'plp_descrCancel'
    DESCRIPTION_CONTENT_ID = 'plp_descrCntText'

    DESCRIPTION_CHARS_COUNTER_ID = 'plp_descrInp_counter'
    DESCRIPTION_WARNING_ID = 'plp_descrInpErCntText'

    EMPTY_INPUT = ''
    SHORT_INPUT = 'w' * (DESCRIPTION_LIMIT // 4)
    MEDIUM_INPUT = 'q' * (DESCRIPTION_LIMIT // 2)
    LONG_INPUT = 'e' * (DESCRIPTION_LIMIT - 1)
    LIMIT_INPUT = 'r' * DESCRIPTION_LIMIT
    OVERHEAD_INPUT = 'y' * (DESCRIPTION_LIMIT + 1)
    HUGE_INPUT = 'u' * (DESCRIPTION_LIMIT * 2)

    SAME_INPUT = 'input shall be the same'

    def setUp(self):
        super(PhotoDescriptionTest, self).setUp()
        self.to_photos()
        self.open_overlay()

    def tearDown(self):
        self.driver.back()
        super(PhotoDescriptionTest, self).tearDown()

    def test_short_description_submit(self):
        self.set_description(self.SHORT_INPUT)
        new_description = self.get_description()
        self.assertEquals(self.SHORT_INPUT, new_description, self.SAME_INPUT)

    def test_medium_description_submit(self):
        self.set_description(self.MEDIUM_INPUT)
        self.assertEquals(self.MEDIUM_INPUT, self.get_description(), self.SAME_INPUT)

    def test_long_description_submit(self):
        self.set_description(self.LONG_INPUT)
        self.assertEquals(self.LONG_INPUT, self.get_description(), self.SAME_INPUT)

    def test_limit_description_submit(self):
        self.set_description(self.LIMIT_INPUT)
        self.assertEquals(self.LIMIT_INPUT, self.get_description(), self.SAME_INPUT)

    def test_overhead_description_submit(self):
        self.set_description(self.OVERHEAD_INPUT)
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.visibility_of_element_located((By.ID, self.DESCRIPTION_WARNING_ID)))
        self.assertEquals(self.driver.find_element_by_id(
            self.DESCRIPTION_WARNING_ID).text, 'Текст слишком длинный. Давайте сделаем его покороче!')

    def test_huge_description_submit(self):
        self.set_description(self.HUGE_INPUT)
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.visibility_of_element_located((By.ID, self.DESCRIPTION_WARNING_ID)))
        self.assertEquals(self.driver.find_element_by_id(
            self.DESCRIPTION_WARNING_ID).text, 'Текст слишком длинный. Давайте сделаем его покороче!')

    def set_description(self, description_string):
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.element_to_be_clickable((By.ID, self.DESCRIPTION_ADD_LNK)))
        self.driver.find_element_by_id(self.DESCRIPTION_ADD_LNK).click()
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.visibility_of_element_located((By.ID, self.DESCRIPTION_INPUT_ID)))
        self.driver.find_element_by_id(self.DESCRIPTION_INPUT_ID).send_keys(description_string)
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.visibility_of_element_located((By.ID, self.DESCRIPTION_SAVE_BUTTON_ID)))
        self.driver.find_element_by_id(self.DESCRIPTION_SAVE_BUTTON_ID).click()

    def change_description(self, description_string):
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.element_to_be_clickable((By.ID, self.DESCRIPTION_CHANGE_LNK)))
        self.driver.find_element_by_id(self.DESCRIPTION_CHANGE_LNK).click()
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.visibility_of_element_located((By.ID, self.DESCRIPTION_INPUT_ID)))
        self.driver.find_element_by_id(self.DESCRIPTION_INPUT_ID).clear()
        self.driver.find_element_by_id(self.DESCRIPTION_INPUT_ID).send_keys(description_string)
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.visibility_of_element_located((By.ID, self.DESCRIPTION_SAVE_BUTTON_ID)))
        self.driver.find_element_by_id(self.DESCRIPTION_SAVE_BUTTON_ID).click()

    def get_description(self):
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.presence_of_element_located((By.ID, self.DESCRIPTION_CONTENT_ID)))
        return self.driver.find_element_by_id(self.DESCRIPTION_CONTENT_ID).text
