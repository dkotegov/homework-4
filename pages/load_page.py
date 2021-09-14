import os

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from pages.main_page import Page


class HomePage(Page):
    PATH = ''
    ALL_HIGHLIGHT = '#TOP_TOOLBAR_ID .Toolbar__item_select--gsHw6 > ' \
                    '.Toolbar__container--SIIvi '
    CHECK_ELEMENT_HIGHLIGHT = '//div[@class="DataListCheckbox__root--vpsSl ' \
                              'DataListCheckbox__root_checked--2m4AC"] '
    ELEMENT = '//div[@class="VirtualList__colItem--2T_t2"]'
    LOAD = '#TOP_TOOLBAR_ID .Toolbar__leftControls--WE2LL > ' \
           '.Toolbar__item--28MNd:nth-child(2) > .Toolbar__container--SIIvi '
    DELETE = '//div[contains(@title,"Удалить")]'
    MORE = '//div[@data-name="more"]'
    HIGHLIGHT_OUT = '//div[text()="Снять выыделение"]'
    SAVE_ICON = '//div[@class="DataListItemThumb__pin--3amKK"]'
    FAVORITE_ICON = '//div[@class="DataListItemThumb__favorites--Tf2hs"]'
    LINK_ICON = '//div[@class="DataListItemThumb__weblink--30Uyy"]'
    LOAD_FROM_MENU = '//div[@data-name="download"]'
    FAVORITE_ADD = '//div[@data-name="addToFavorite"]'
    FAVORITE_ADD_TOOLBAR = '//div[contains(@data-name,' \
                           '"addToFavorites")]//div[contains(@class,' \
                           '"Toolbar__container--SIIvi")] '
    FAVORITE_REMOVE_TOOLBAR = '//div[contains(@data-name,' \
                              '"removeFromFavorites")]//div[contains(@class,' \
                              '"Toolbar__container--SIIvi")] '
    REMOVE_FAVORITE = '//div[@data-name="removeFromFavorites"]'
    COPY_FROM_MENU = '//div[@data-name="copy"]'
    RENAME_ELEMENT = '//div[@data-name="rename"]'
    SHARE_USER = '//div[@data-name="share"]'
    NEW_TAB = '//div[@data-name="newTab"]'
    LINK_SHARE = '//div[@data-name="publish"]'
    MOVE = '//div[@data-name="move"]'
    REMOVE = '//div[@data-name="remove"]'
    INPUT_POLE = '//input[@placeholder="Введите имя папки"]'
    POLE_RENAME = '//div[contains(@class,"ui fluid focus input")]//input[' \
                  'contains(@type,"text")] '
    BUTTON_RENAME = '//button[text()="Переименовать"]'
    BUTTON_CREATE = '//button[text()="Создать"]'
    BUTTON_CREATE_AND_SHARE = '//button[text()="Создать и поделиться"]'
    BUTTON_UPLOAD = '//div[text()="Загрузить"]'
    BUTTON_UPLOAD_BLUE = '//div[@class="Upload__area--3rqeF"]'
    BUTTON_CREATE_FOLDER = '//button[@data-name="create"]'
    BUTTON_COPY = '//button[text()="Скопировать"]'
    BUTTON_MOVE = '//button[text()="Переместить"]'
    BUTTON_CLEAR = '//button[text()="Очистить"]'
    ALL_FILE = '.Breadcrumbs__item--cAPlH:nth-child(1) .Breadcrumb__text--1Qzms'
    VIEW = '//div[@data-name="view"]'
    SORT = '//div[@data-name="sort"]'
    SORT_ALFAVIT = '//div[@data-name="sortName"]'
    SORT_SIZE = '//div[@data-name="sortSize"]'
    SORT_DATE = '//div[@data-name="sortDate"]'
    VIEW_LIST = '//div[@data-name="viewList"]'
    VIEW_TABLE = '//div[@data-name="viewThumbs"]'
    NAME_FOLDERS = '//div[@class="TreeNode__root--22m4E ' \
                   'TreeNode__root_selectDlg--cT_dx"]//div[' \
                   '@class="TreeNode__title--3_ehQ"] '
    MSG_INF = '//div[@class="Snackbars__text - -BNIVb"]'
    FAVORITE_CHECK = '//div[@class="DataListItemThumb__favorites--Tf2hs ' \
                     'DataListItemThumb__favorites_active--18o9C"] '
    LINK_CHECK = '//div[@class="DataListItemThumb__weblink--30Uyy ' \
                 'DataListItemThumb__weblink_active--1KmUm"] '
    DROP_USER_ROOT_MENU = '//div[@class="SharingNewDropdown__root--1Qe_z ' \
                          'undefined"] '
    TYPE_SELECT = '//div[text()="Смотреть и загружать файлы"]'
    DROP_TIME_MENU = '//div[@class="SharingNewDropdown__root--1Qe_z undefined"]'
    NAME_FILE = '//div[@class="Name__name--13u3t"]'
    CREATE_DOC_MENU = '//div[@class="DataListItemCreateNew__root--3OmvE ' \
                      'DataListItemCreateNew__rootThumb--2zkxa"] '
    CREATE_DOC = '//div[@data-name="createDoc"]'
    CREATE_TABL = '//div[@data-name="createCell"]'
    CREATE_PPT = '//div[@data-name="createPpt"]'
    CREATE_DOCX = '//div[@data-name="createDocx"]'
    CREATE_TABLX = '//div[@data-name="createXlsx"]'
    CREATE_PPTX = '//div[@data-name="createPptx"]'
    FAST_ACCESS = '//div[text()="Быстрый доступ"]'
    BASKET = '//div[text()="Корзина"]'
    RECOMMENDATIONS = '//div[text()="Mail.ru рекомендует"]'
    FROM_MAIL = '//div[text()="Из почты"]'
    INCREASE_THE_VOLUME = '//button[@class="ui fluid primary button ' \
                          'Button__btn_octavius--38SD2"] '
    DISABLE_ADS = '//a[@data-name="disableads"]'
    SHARE_LINK = '//input[@class="CopyWeblink__input--LxI1C"]'
    DELETE_BUTTON = '//button[text()="Удалить"]'
    DROPBOX_USER = '//div[@class="SharingNewDropdown__text--BKfE5"]'
    DROPBOX_TIME_SHARE = '//div[@class="SharingNewDropdown__text--BKfE5"]'
    LOGOUT = '//a[contains(text(),"выход")]'
    CLOSE_WINDOW = '//div[@class="Dialog__close--1rKyk"]'
    UPLOAD_FILE = '//input[@class="UploadDialog__input--1pPCA"]'
    UPLOAD = '//div[@id="TOP_TOOLBAR_ID"]//div[@data-name="upload"]'
    CREATE_TOOLBAR = '//div[@id="TOP_TOOLBAR_ID"]//div[@data-name="create"]'
    UPLOAD_BLUE_BUTTON = '//div[@class="Upload__area--3rqeF"]'
    UPLOAD_BLUE_BUTTON_CIRCLE = '//div[@class="Upload__circle--3zdwT"]'
    CLOSE_DIALOG = '//div[@class="Bubble__close--1cFFu"]'
    INFO_MESSANGE = '//div[@class="Snackbars__snackbar--a-agp ' \
                    'Snackbars__closable--2wGjU"]//div' \
                    '[contains(text(),"Загрузка успешно завершена")]'
    INFO_MESSANGE_RE = '//div[@class="Snackbars__snackbar--a-agp ' \
                       'Snackbars__closable--2wGjU"]//div[contains(text(),' \
                       '"Все файлы восстановлены")] '
    CREATE_FOLDER_MENU = '//div[contains(text(),"Папку")]'
    CREATE_FOLDER_SHARE_MENU = '//div[contains(text(),"Общую папку")]'
    ACTIVE_SUBSCRIPTION = '//div[text()="Активные подписки"]'
    HISTORY = '//span[contains(text(),"История покупок")]'
    CLEAR_BASKET = '//div[contains(@data-name,"clear")]//div[contains(@class,' \
                   '"Toolbar__container--SIIvi")] '
    RESTORE_BASKET = '//div[contains(@data-name,"restoreAll")]//div[contains(' \
                     '@class,"Toolbar__container--SIIvi")] '
    ELEMENT_BASKET = '//a[@class="DataListItem__root--CNJMg ' \
                     'DataListItem__root_row--D49DR"] '
    SHARE = '//div[@data-qa-modal="sharing-new"]'
    OUTLINE = '//div[@class="Outline"]'
    CLOUD = '//a[@class="x-ph__link"][contains(text(),"Облако")]'
    BASKET_ELEMENT = '.DataListItemRow__root--39hIM'
    EMPTY_TRASH = '//div[text()="Корзина пуста"]'
    PAYMENT_HISTORY = '//div[contains(@class,"PaymentHistory__empty--3K4Fa")]'
    CHECK_SUB = '//div[@class="SidebarSubscriptionItem__description--W94gM"]'
    FAVORITE_ICON_ADDED = "//div[@class='DataListItemThumb__favorites--Tf2hs " \
                          "DataListItemThumb__favorites_active--18o9C']"
    SELECT_MAIL = '//a[@class="TabMenuItem__item--FfF2c TabMenuItem__item_active--2RJGw' \
                  ' TabMenuItem__item_bottomLine--1nDx2"]//div[@class="TabMenuItem__name--50rg8"]'
    DEFAULT_OFFER = '//a[@class="TabMenuItem__item--FfF2c TabMenuItem__item_active--2RJGw"]' \
                    '//div[@class="TabMenuItem__name--50rg8"]'
    CLOSE_UPLOAD_WINDOWS = '//div[@class="Controls__close--2Y4Yr"]'
    CLOSE_WINDOW_UPLOAD = '//div[@class="Progress__icon--Y98lE"]//*[' \
                          'local-name()="svg"] '

    def open_drop_menu(self, name):
        ActionChains(self.driver).context_click(name).perform()
        return name.text

    def select_element(self):
        elements = self.take_all_elements()
        elements[1].click()
        return elements[1].text

    def take_all_highlight(self):
        self.driver.find_element_by_css_selector(self.ALL_HIGHLIGHT).click()

    def take_all_elements(self):
        return self.driver.find_elements_by_xpath(self.ELEMENT)

    def check_highlight_elements(self):
        return self.driver.find_elements_by_xpath(self.CHECK_ELEMENT_HIGHLIGHT)

    def take_off_all_highlight(self):
        self.driver.find_element_by_xpath(self.HIGHLIGHT_OUT).click()

    def save_elements(self):
        self.driver.find_element_by_css_selector(self.LOAD).click()

    def save_elements_by_icon(self):
        self.driver.find_element_by_xpath(self.SAVE_ICON).click()

    def copy_element(self):
        self.driver.find_element_by_xpath(self.COPY_FROM_MENU).click()

    def take_folders(self):
        return self.driver.find_elements_by_xpath(self.NAME_FOLDERS)

    def click_element_folder(self, name):
        self.driver.find_element_by_xpath(
            f'//div[@data-name="/{name}"]').click()

    def create_folder_home_page(self):
        self.driver.find_element_by_xpath(self.CREATE_FOLDER_MENU).click()

    def create_folder_share_home_page(self):
        self.driver.find_element_by_xpath(self.CREATE_FOLDER_MENU).click()

    def click_element(self, name):
        self.driver.find_element_by_xpath(f'//a[@data-qa-name="{name}"]').click()

    def click_element_fol(self, name):
        self.driver.find_element_by_xpath(f'//a[@data-qa-name={name}]').click()

    def double_click_element(self, name):
        ActionChains(self.driver).double_click(
            self.driver.find_element_by_xpath(
                f'//div[text()="{name}"]')).perform()

    def find_element(self, name):
        try:
            WebDriverWait(self.driver, 1).until(
                EC.invisibility_of_element_located(
                    (By.XPATH, f'//div[text()="{name}"]')))
            self.driver.find_element_by_xpath(f'//div[text()="{name}"]')
        except NoSuchElementException:
            return False

    def find(self, name):
        return self.driver.find_element_by_xpath(f'//div[text()="{name}"]')

    def click_button_copy(self):
        self.driver.find_element_by_xpath(self.BUTTON_COPY).click()

    def click_button_rename(self):
        self.driver.find_element_by_xpath(self.BUTTON_RENAME).click()

    def click_create(self):
        self.driver.find_element_by_xpath(self.BUTTON_CREATE).click()

    def click_create_and_share(self):
        self.driver.find_element_by_xpath(self.BUTTON_CREATE_AND_SHARE).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.SHARE)))

    def click_replace(self):
        self.driver.find_element_by_xpath(self.BUTTON_MOVE).click()

    def click_upload(self):
        self.driver.find_element_by_xpath(self.UPLOAD).click()

    def click_upload_blue_button(self, name):
        ActionChains(self.driver). \
            drag_and_drop(
            os.path.abspath(f"./data/{name}"),
            self.driver.find_element_by_xpath(self.UPLOAD_BLUE_BUTTON)). \
            perform()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.LOGOUT).click()

    def click_basket(self):
        self.driver.find_element_by_xpath(self.BASKET).click()

    def click_clear_basket(self):
        self.driver.find_element_by_xpath(self.CLEAR_BASKET).click()

    def click_button_clear(self):
        self.driver.find_element_by_xpath(self.BUTTON_CLEAR).click()

    def click_button_restore(self):
        self.driver.find_element_by_xpath(self.RESTORE_BASKET).click()

    def click_active_sub(self):
        self.driver.find_element_by_xpath(self.ACTIVE_SUBSCRIPTION).click()

    def click_recommend(self):
        self.driver.find_element_by_xpath(self.RECOMMENDATIONS).click()

    def click_mail(self):
        self.driver.find_element_by_xpath(self.FROM_MAIL).click()

    def click_view(self):
        self.driver.find_element_by_xpath(self.VIEW).click()

    def click_sort(self):
        self.driver.find_element_by_xpath(self.SORT).click()

    def select_view_table(self):
        self.driver.find_element_by_xpath(self.VIEW_TABLE).click()

    def select_view_list(self):
        self.driver.find_element_by_xpath(self.VIEW_LIST).click()

    def select_sort_alfa(self):
        self.driver.find_element_by_xpath(self.SORT_ALFAVIT).click()

    def select_sort_size(self):
        self.driver.find_element_by_xpath(self.SORT_SIZE).click()

    def select_sort_date(self):
        self.driver.find_element_by_xpath(self.SORT_DATE).click()

    def click_history_buy(self):
        self.driver.find_element_by_xpath(self.HISTORY).click()

    def click_close_window(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, self.CLOSE_WINDOW)))
        self.driver.find_element_by_xpath(self.CLOSE_WINDOW).click()

    def click_close_dialog(self):
        self.driver.find_element_by_xpath(self.CLOSE_DIALOG).click()

    def click_button_delete(self):
        self.driver.find_element_by_xpath(self.DELETE_BUTTON).click()

    def click_disable_ads(self):
        self.driver.find_element_by_xpath(self.DISABLE_ADS).click()

    def create_from_toolbar(self):
        self.driver.find_element_by_xpath(self.CREATE_TOOLBAR).click()

    def create_folder(self):
        self.driver.find_element_by_xpath(self.BUTTON_CREATE_FOLDER).click()

    def create_document(self):
        self.driver.find_element_by_xpath(self.CREATE_DOC).click()

    def create_table(self):
        self.driver.find_element_by_xpath(self.CREATE_TABL).click()

    def create_presentation(self):
        self.driver.find_element_by_xpath(self.CREATE_PPT).click()

    def create_documentx(self):
        self.driver.find_element_by_xpath(self.CREATE_DOCX).click()

    def create_tablex(self):
        self.driver.find_element_by_xpath(self.CREATE_TABLX).click()

    def create_presentationx(self):
        self.driver.find_element_by_xpath(self.CREATE_PPTX).click()

    def click_all_file(self):
        self.driver.find_element_by_css_selector(self.ALL_FILE).click()

    def open_cloud(self):
        self.driver.find_element_by_xpath(self.CLOUD).click()

    def click_swap(self, name):
        self.driver.find_element_by_xpath(f'//a[@data-qa-name="{name}"]'). \
            click()

    def input_info(self, info):
        self.driver.find_element_by_xpath(self.INPUT_POLE).send_keys(info)

    def input_new_name(self, info):
        self.driver.find_element_by_xpath(self.POLE_RENAME). \
            send_keys(Keys.CONTROL + 'a')
        self.driver.find_element_by_xpath(self.POLE_RENAME).send_keys(info)

    def input_file(self, name):
        self.driver.find_element_by_xpath(self.UPLOAD_FILE). \
            send_keys(os.path.abspath(f"./data/{name}"))

    def move_element(self):
        self.driver.find_element_by_xpath(self.MOVE).click()

    def share_for_user(self):
        self.driver.find_element_by_xpath(self.SHARE_USER).click()

    def share_link(self):
        self.driver.find_element_by_xpath(self.LINK_SHARE).click()

    def take_share(self):
        return self.driver.find_element_by_xpath(self.SHARE_LINK). \
            get_attribute('value')

    def open_dropbox_user(self):
        dropbox = self.driver.find_elements_by_xpath(self.DROPBOX_USER)
        dropbox[0].click()

    def open_dropbox_time_share(self):
        dropbox = self.driver.find_elements_by_xpath(self.DROPBOX_USER)
        dropbox[1].click()

    def change_dropbox_item(self, name):
        self.driver.find_element_by_xpath(f"//div[text()='{name}']").click()

    def open_new_tab(self):
        self.driver.find_element_by_xpath(self.NEW_TAB).click()

    def rename_element(self):
        self.driver.find_element_by_xpath(self.RENAME_ELEMENT).click()

    def wait_rename(self, name):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, f'//a[@data-qa-name="{name}"]')))

    def wait_create_element(self, name):
        self.open_cloud()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, f'//a[@data-qa-name="{name}"]')))

    def wait(self):
        self.driver.implicitly_wait(4)

    def wait_load(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, self.INFO_MESSANGE)))
        return self.driver.find_element_by_xpath(self.INFO_MESSANGE).text

    def wait_restore(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, self.INFO_MESSANGE_RE)))
        return self.driver.find_element_by_xpath(self.INFO_MESSANGE_RE).text

    def add_to_favorite(self):
        self.driver.find_element_by_xpath(self.FAVORITE_ADD).click()

    def add_to_favorite_toolbar(self):
        self.driver.find_element_by_xpath(self.FAVORITE_ADD_TOOLBAR).click()

    def remove_to_favorite(self):
        self.driver.find_element_by_xpath(self.REMOVE_FAVORITE).click()

    def remove_to_favorite_toolbar(self):
        self.driver.find_element_by_xpath(self.FAVORITE_REMOVE_TOOLBAR).click()

    def check_favorite(self, name, add):
        if add:
            self.driver.find_elements_by_xpath(
                f"//a[@data-qa-name={name}]//div["
                "@class='DataListItemThumb__favorites--Tf2hs "
                "DataListItemThumb__favorites_active--18o9C']")
        else:
            self.driver.find_elements_by_xpath(
                f"//a[@data-qa-name={name}]//div[@class='FavoriteIcon__root"
                "--wzRgi FavoriteIcon__root_color_red--GaRxB']")

    def click_add_favorite_icon(self, add):
        if add:
            self.driver.find_element_by_xpath(self.FAVORITE_ICON).click()
        else:
            self.driver.find_element_by_xpath(self.FAVORITE_ICON_ADDED).click()

    def check_link(self):
        return self.driver.find_elements_by_xpath(self.LINK_CHECK)

    def check_sub(self):
        return self.driver.find_element_by_xpath(self.CHECK_SUB).text

    def check_history_buy(self):
        return self.driver.find_element_by_xpath(self.PAYMENT_HISTORY).text

    def check_select_offer(self):
        return self.driver.find_element_by_xpath(self.DEFAULT_OFFER).text

    def check_select_filter_mail(self):
        return self.driver.find_element_by_xpath(self.SELECT_MAIL).text

    def check_url(self):
        self.driver.switch_to_window(self.driver.window_handles[1])
        return self.driver.current_url

    def close_window_upload(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.XPATH, self.CLOSE_WINDOW_UPLOAD)))
        self.driver.find_element_by_xpath(self.CLOSE_UPLOAD_WINDOWS).click()

    def save_element_from_the_menu(self):
        browser_downloads = "chrome://downloads/"
        self.driver.find_element_by_xpath(self.LOAD_FROM_MENU).click()
        self.driver.execute_script("window.open();")
        self.swap_tab()
        self.driver.get(browser_downloads)

    def check_empty_basket(self):
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(
            (By.XPATH, self.EMPTY_TRASH)))

    def check_element_basket(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, self.BASKET_ELEMENT)))
        self.driver.find_elements_by_css_selector(self.BASKET_ELEMENT)

    def swap_tab(self):
        self.driver.switch_to_window(self.driver.window_handles[1])

    def swap_first(self):
        self.driver.switch_to_window(self.driver.window_handles[0])

    def open_more(self):
        self.driver.find_element_by_xpath(self.MORE).click()

    def del_elements(self):
        self.driver.find_element_by_xpath(self.REMOVE).click()
