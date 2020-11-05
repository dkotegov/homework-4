from romanov.app.driver import connect


class CommonSteps:
    @staticmethod
    def open_app():
        connect.driver.get('https://zinterest.ru/')
