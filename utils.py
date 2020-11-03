import os

from selenium.webdriver import DesiredCapabilities, Remote, FirefoxProfile, ChromeOptions


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

    else:
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
