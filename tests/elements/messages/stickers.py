# coding=utf-8

from selenium.webdriver.common.by import By

from tests.elements.base import BaseElement


class Stickers(BaseElement):
    SMILES_TAB_LINK = (By.CSS_SELECTOR, "a.js-tabs-t:nth-child(3)")
    SAD_SMILE = (By.CSS_SELECTOR,
                 "#collection_nav_id_recent_smiles > ul:nth-child(2) > li:nth-child(1) > img:nth-child(1)")
