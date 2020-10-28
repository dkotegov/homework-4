class Steps(object):
    def __init__(self, page):
        self.page = page

    def do_redirect(self, to):
        self.page.waitRedirect(to)

    def open(self):
        self.page.open()

    def do_not_wait_alert(self):
        return self.page.do_not_wait_alert()

    def accept_alert_text(self):
        return self.page.accept_alert_text()
