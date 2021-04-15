import os

from selenium.webdriver.common.by import By

from testutils import Component
from datetime import datetime, timedelta


class DatePicker(Component):
    class Selectors:
        day = lambda date: f'button[data-test-id="date-{date}"]'

    def choose_day(self, from_today=0):
        date = datetime.now() + timedelta(days=from_today)
        if os.environ.get("LOCALE") == "ENG":
            date_str = f'{date.month}/{date.day}/{date.year}'
        else:
            date_str = date.strftime('%d.%m.%Y')

        selector = self.Selectors.day(date_str)
        self._wait_visible(By.CSS_SELECTOR, selector)
        self._wait_clickable(By.CSS_SELECTOR, selector)
        self._find(selector).click()
        self._dis_wait_visible(By.CSS_SELECTOR, selector)
