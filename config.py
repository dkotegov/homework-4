from selenium import webdriver


class Config:
    consts = {
        'firefoxPath': 'drivers/geckodriver',
        'loginPath': 'https://mailer.ru.com/signin',
    }

    selectors = {
        'enter': '.submit.btn.btn--primary.btn--medium.h-full-width',
        'email': 'input[name="email"]',
        'password': 'input[name="password"]',
        'send_page': 'a[name="navbar-send"]',
        'to': 'input[name="to"]',
        'theme': 'input[name="theme"]',
        'message': 'textarea[name="text"]',
        'button': 'button.submit.btn.btn--primary.btn--medium.h-full-width',
        'search_input': '#search-input',
        'search_list': '#search-result-list > span',
        'plus': '#add-folder-recived',
        'label_field': 'input[name="folderName"]',
        'label_button': 'button.btn.btn--medium.btn--primary.h-full-width',
        'letter': 'article.brick.entry.format-standard',
        'not_read_button': 'a.not-read-button',
        'add_button': '#button-form-add-letter-folder',
        'submit_button': '#choose-folder button.btn.h-full-width',
        'empty_letter': '.main-columns.project_scroll',
        'logout': 'a[name="navbar-exit"]',
        'open_profile': 'a[name="navbar-profile"]',
        'check_email': 'div.form-field > p',
    }

    def __init__(self, browser):
        self.browser = browser

    def useBrowser(self):
        if self.browser == 'Firefox':
            return webdriver.Firefox(executable_path=self.consts['firefoxPath'])
