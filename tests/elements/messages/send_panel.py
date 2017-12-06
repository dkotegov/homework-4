# coding=utf-8

from selenium.webdriver.common.by import By

from tests.elements.base import BaseElement


class SendPanel(BaseElement):
    MESSAGE_INPUT = (By.XPATH, "//div[@name='st.txt']")
    SEND_BUTTON = (By.CSS_SELECTOR, "button.comments_add-controls_save:nth-child(1)")
    STICKERS_BUTTON = (By.CSS_SELECTOR,
                       ".ic.ic_smile.smiles_w.comments_smiles_trigger.js-comments_smiles_trigger.__new")
