# -*- coding: utf-8 -*-

from components.component import Component


class AwardsBlock(Component):
    OSCAR_BTN = '//a[@class="awards__item__logo__img" and @href="/awards/oscar/"]'
    GLOBUS_BTN = '//a[@class="awards__item__logo__img" and @href="/awards/golden_globus/"]'
    EMMY_BTN = '//a[@class="awards__item__logo__img" and @href="/awards/emmy/"]'
    CANNES_BTN = '//a[@class="awards__item__logo__img" and @href="/awards/cannes/"]'
    MSK_KF_BTN = '//a[@class="awards__item__logo__img" and @href="/awards/mmkf/"]'
    ODES_KF_BTN = '//a[@class="awards__item__logo__img" and @href="/awards/oiff/"]'
    VEN_KF_BTN = '//a[@class="awards__item__logo__img" and @href="/awards/venetsianskii_kinofestival/"]'

    OSCAR_LINK = '//a[contains(text(),"Оскар")]'
    GLOBUS_LINK = '//a[contains(text(),"Золотой глобус")]'
    EMMY_LINK = '//a[contains(text(),"Эмми")]'
    CANNES_LINK = '//a[contains(text(),"Каннский кинофестиваль")]'
    MSK_KF_LINK = '//a[contains(text(),"Московский кинофестиваль")]'
    ODES_KF_LINK = '//a[contains(text(),"Одесский кинофестиваль")]'
    VEN_KF_LINK = '//a[contains(text(),"Венецианский кинофестиваль")]'

    BASE_URL = 'https://afisha.mail.ru/'
    OSCAR_BTN_URL = BASE_URL + 'awards/oscar/'
    GLOBUS_BTN_URL = BASE_URL + 'awards/golden_globus/'
    EMMY_BTN_URL = BASE_URL + 'awards/emmy/'
    CANNES_BTN_URL = BASE_URL + 'awards/cannes/'
    MSK_KF_BTN_URL = BASE_URL + 'awards/mmkf/'
    ODES_KF_BTN_URL = BASE_URL + 'awards/oiff/'
    VEN_KF_BTN_URL = BASE_URL + 'awards/venetsianskii_kinofestival/'

    def click_oscar_btn(self):
        self.click(self.OSCAR_BTN)

    def click_globus_btn(self):
        self.click(self.GLOBUS_BTN)

    def click_emmy_btn(self):
        self.click(self.EMMY_BTN)

    def click_cannes_btn(self):
        self.click(self.CANNES_BTN)

    def click_msk_kf_btn(self):
        self.click(self.MSK_KF_BTN)

    def click_ven_kf_btn(self):
        self.click(self.VEN_KF_BTN)

    def click_odes_kf_btn(self):
        self.click(self.ODES_KF_BTN)

    def click_oscar_link(self):
        self.click(self.OSCAR_LINK)

    def click_globus_link(self):
        self.click(self.GLOBUS_LINK)

    def click_emmy_link(self):
        self.click(self.EMMY_LINK)

    def click_cannes_link(self):
        self.click(self.CANNES_LINK)

    def click_msk_kf_link(self):
        self.click(self.MSK_KF_LINK)

    def click_ven_kf_link(self):
        self.click(self.VEN_KF_LINK)

    def click_odes_kf_link(self):
        self.click(self.ODES_KF_LINK)
