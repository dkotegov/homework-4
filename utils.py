import os
import ntpath

from selenium.webdriver import DesiredCapabilities, Remote, FirefoxProfile, ChromeOptions

from Auth import AuthPage
from TrashBin import TrashBinPage


def get_remote_driver(browser):
    if browser == 'CHROME':
        profile = ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0,
                 'download.default_directory': os.getcwd() + '/Files/tmp',
                 'directory_upgrade': True,
                 "download.prompt_for_download": False,
                 'extensions_to_open': ''}
        profile.add_experimental_option('prefs', prefs)

        return Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
            options=profile
        )

    elif browser == "FIREFOX":
        profile = FirefoxProfile()
        profile.set_preference("browser.helperApps.neverAsk.saveToDisk",
                               "multipart/x-zip,application/zip,application/x-zip-compressed,application/x-compressed" +
                               ",application/msword,application/csv,text/csv,image/png ,image/jpeg, application/pdf," +
                               " text/html,text/plain,  application/excel, application/vnd.ms-excel, " +
                               "application/x-excel, application/x-msexcel, application/octet-stream")
        profile.set_preference('browser.download.folderList', 2)  # custom location
        profile.set_preference('browser.download.manager.showWhenStarting', False)
        profile.set_preference('browser.download.dir', os.getcwd() + '/Files/tmp')

        return Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy(),
            browser_profile=profile
        )
    else:
        raise RuntimeError("invalid browser name: " + browser)


def standard_set_up_auth():
    browser = os.environ.get('BROWSER', 'CHROME')
    driver = get_remote_driver(browser)

    login = os.environ['LOGIN']
    password = os.environ['PASSWORD']

    auth_page = AuthPage(driver)
    auth_page.auth(login, password)

    return driver


def standard_tear_down_cleanup(driver):
    trash_bin_page = TrashBinPage(driver)
    trash_bin_page.open()
    trash_bin_page.home_utils.close_mini_banner_if_exists()
    trash_bin_page.delete.clear_trash_bin()

    driver.quit()


def get_filename(filepath) -> str:
    head, tail = ntpath.split(filepath)

    filename = tail or ntpath.basename(head)

    return filename


def get_file_extension(filepath) -> str:
    _, file_extension = os.path.splitext(filepath)
    return file_extension
