from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import exceptions

from tests.pages.primary.component import Component
from tests.pages.primary.statuses_page import StatusesPage
from util import config


class PhotoToolbar(Component):
    def get_left_toolbar(self):
        return PhotoLeftToolbar(self.driver)

    def get_right_toolbar(self):
        return PhotoRightToolbar(self.driver)


class PhotoRightToolbar(Component):
    DELETE_BUTTON_XPATH = '//div[@id="hook_Block_DeleteRestorePhoto"]/a[@class="ic-w lp"]'

    MARK_FRIENDS_BUTTON_XPATH = '//span[contains(@class, "js-createPhotoPins")]'
    MARK_TGT_ID = '__plpcte_target'
    MARK_LIST_ID = 'plp_photoContainer'
    MARK_SELF_ID = 'plpp_markSelf'
    MARK_FINISH_BUTTON_XPATH = '//button[contains(@class, "js-cancelEditMode")]'
    MARK_FRIEND_BY_ID_XPATH = '//div[contains(@class, "plpp_friend")][@friendid="'

    def delete_photo(self):
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.DELETE_BUTTON_XPATH)))
        self.driver.find_element_by_xpath(self.DELETE_BUTTON_XPATH).click()

    def mark_self(self):
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.MARK_FRIENDS_BUTTON_XPATH)))
        self.driver.find_element_by_xpath(self.MARK_FRIENDS_BUTTON_XPATH).click()
        self.driver.find_element_by_id(self.MARK_TGT_ID)
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.MARK_SELF_ID)))
        self.driver.find_element_by_id(self.MARK_SELF_ID).click()
        self.driver.find_element_by_xpath(self.MARK_FINISH_BUTTON_XPATH).click()

    def mark_friend(self, friend_id):
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.MARK_FRIENDS_BUTTON_XPATH)))
        self.driver.find_element_by_xpath(self.MARK_FRIENDS_BUTTON_XPATH).click()
        self.driver.find_element_by_id(self.MARK_TGT_ID)
        WebDriverWait(self.driver, config.WAITING_TIME, 0.1) \
            .until(expected_conditions.visibility_of_element_located((By.ID, self.MARK_LIST_ID)))
        try:
            self.driver.find_element_by_xpath(self.MARK_FRIEND_BY_ID_XPATH + friend_id + '"]').click()
        except NoSuchElementException:
            return False

        return True


class PhotoLeftToolbar(Component):
    SHARE_NOW_XPATH = '//div[contains(@id, "hook_Block_ReshareNow_")]/a'
    RESHARE_BUTTON_XPATH = '//button[@data-type="RESHARE"]'

    RESHARE_COUNTER_XPATH = '//button[@data-type="RESHARE"]/span[contains(@class, "widget_count")]'

    STATUSES_XPATH = '//a[contains(@href, "/statuses")]'

    PUT_LIKE_XPATH = '//span[@data-type="PHOTO"]'
    THUMBS_UP_LIKE_XPATH = '//a[@title="Класс!"][@data-l="t,klassOverPhoto"]'
    THUMBS_UP_UNLIKE_XPATH = '//a[@title="Отменить"][@data-l="t,unklassOverPhoto"]'

    LIKES_COUNTER_XPATH = '//span[@data-type="PHOTO"][contains(@class, "controls-list_lk")]' \
                          '/span[contains(@class, "widget_count js-count")]'
    LIKERS_LIST_OPEN_XPATH = '//a[@data-l="t,likes"][@href="/feed"][@class="ucard-mini-list_all_lk"]'
    LIKERS_LIST_CLOSE_ID = 'nohook-modal-close'

    LIKERS_LIST_ID = 'hook_Block_ReactedUsersListBlock'
    LIKER_NAME_HOLDER_XPATH = '//div[@class="ucard-v l"]/div[@class="caption"]/div[@class="ellip"]/a'

    DATA_REACTION_ICON_XPATH = '//span[@data-reaction-id="'
    DATA_REACTION_IDS = ['10', '3', '1', '2', '4']

    DATA_REACTION_COUNTER_XPATH_BEGIN = '//a[@class="filter_i"][contains(@hrefattrs, "st.layer_reaction='
    DATA_REACTION_COUNTER_XPATH_END = '"]/span[@class="filter_count"]'

    DATA_REACTIONS_HOLDER_CLASS = 'reactions'

    PHOTO_AUTHOR_NAME_XPATH = '//a[@data-l="t,author.name"][contains(@class, "ucard_info_name")]'

    def share(self):
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.RESHARE_BUTTON_XPATH)))
        self.driver.find_element_by_xpath(self.RESHARE_BUTTON_XPATH).click()
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.SHARE_NOW_XPATH)))
        self.driver.find_element_by_xpath(self.SHARE_NOW_XPATH).click()
        self.driver.refresh()
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.RESHARE_BUTTON_XPATH)))

    def unshare(self):
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.STATUSES_XPATH)))
        self.driver.find_element_by_xpath(self.STATUSES_XPATH).click()
        statuses = StatusesPage(self.driver)
        statuses.unshare_last()

    def shares_count(self):
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.RESHARE_BUTTON_XPATH)))
        return self.driver.find_element_by_xpath(self.RESHARE_COUNTER_XPATH).text

    def put_like(self):
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.PUT_LIKE_XPATH)))
        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath(self.PUT_LIKE_XPATH)).click().pause(config.WAITING_TIME).perform()
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.PUT_LIKE_XPATH)))
        self.driver.refresh()

    def put_unlike(self):
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.PUT_LIKE_XPATH)))
        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath(self.PUT_LIKE_XPATH)).click().pause(config.WAITING_TIME).perform()
        self.driver.refresh()

    def put_like_thumbs(self):
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.THUMBS_UP_LIKE_XPATH)))
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(
            self.THUMBS_UP_LIKE_XPATH)).click().perform()

    def put_unlike_thumbs(self):
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.THUMBS_UP_UNLIKE_XPATH)))
        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_xpath(self.THUMBS_UP_UNLIKE_XPATH)).click().perform()

    def get_likes_count(self):
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.LIKES_COUNTER_XPATH)))
        return self.driver.find_element_by_xpath(self.LIKES_COUNTER_XPATH).text

    def get_likers_list(self):
        self.open_likers_list()
        liker_names = self.get_liker_names()
        self.close_likers_list()
        return liker_names

    def get_reactions_count(self):
        reaction_counts = []
        self.open_likers_list()
        for reaction in self.DATA_REACTION_IDS:
            reaction_counts.append(self.get_likers_count_by_reactions(reaction))
        self.close_likers_list()
        return reaction_counts

    def get_liker_names(self):
        liker_names = []
        try:
            self.open_likers_list()
            WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
                expected_conditions.visibility_of_element_located((By.XPATH, self.LIKER_NAME_HOLDER_XPATH)))
            liker_hrefs = self.driver.find_elements_by_xpath(self.LIKER_NAME_HOLDER_XPATH)
            for href in liker_hrefs:
                liker_names.append(href.text)
            print(liker_hrefs)
            self.close_likers_list()
        except exceptions.TimeoutException:
            pass
        return liker_names

    def get_likers_count_by_reactions(self, reaction):
        xpath = self.DATA_REACTION_COUNTER_XPATH_BEGIN + reaction + self.DATA_REACTION_COUNTER_XPATH_END
        try:
            WebDriverWait(self.driver, config.WAITING_TIME, 0.1).until(
                expected_conditions.presence_of_element_located((By.XPATH, xpath)))
            return self.driver.find_element_by_xpath(xpath).text
        except exceptions.TimeoutException:
            return 0

    def open_likers_list(self):
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.LIKES_COUNTER_XPATH)))
        likes_counter = self.driver.find_element_by_xpath(self.LIKES_COUNTER_XPATH)
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.LIKERS_LIST_OPEN_XPATH)))
        likers_list_open = self.driver.find_element_by_xpath(self.LIKERS_LIST_OPEN_XPATH)
        open_likers_list = ActionChains(self.driver).move_to_element(likes_counter)\
            .pause(config.WAITING_TIME).move_to_element(likers_list_open).click()
        open_likers_list.perform()

    def close_likers_list(self):
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.element_to_be_clickable((By.ID, self.LIKERS_LIST_CLOSE_ID)))
        ActionChains(self.driver).move_to_element(
            self.driver.find_element_by_id(self.LIKERS_LIST_CLOSE_ID)).click().perform()

    def set_reaction(self, reaction_id):
        xpath = self.DATA_REACTION_ICON_XPATH + reaction_id + '"]'
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.presence_of_element_located(self.PUT_LIKE_XPATH))
        like_btn = self.driver.find_element_by_xpath(self.PUT_LIKE_XPATH)
        change_reaction = ActionChains(self.driver).move_to_element(like_btn)\
            .pause(1).move_to_element(self.driver.find_element_by_xpath(xpath)).click()
        change_reaction.perform()

    def get_photo_author_name(self):
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.visibility_of_element_located((By.XPATH, self.PHOTO_AUTHOR_NAME_XPATH)))
        return self.driver.find_element_by_xpath(self.PHOTO_AUTHOR_NAME_XPATH).text
