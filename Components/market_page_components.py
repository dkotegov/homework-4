# -*- coding: utf-8 -*-
from Components.component import Component


class CatalogPopup(Component):
    CREATE_CATALOG = '//a[@class="market-albums_new-lk"]'
    CATALOG_NAME = '//input[@id="field_name"]'
    UPLOAD_IMAGE = '//input[@class="html5-upload-link"]'

    SAVE_BUTTON = '//input[@id="hook_FormButton_button_save"]'
    CANCEL_BUTTON = '//input[@id="button_cancel"]'
    CLOSE_BUTTON = '//a[@id="nohook_modal_close"]'

    def open_popup(self):
        super(CatalogPopup, self).click_element(self.CREATE_CATALOG)

    def set_catalog_name(self, name=u'Каталог'):
        super(CatalogPopup, self).input_text_to_element(self.CATALOG_NAME, name)

    def upload_icon(self, file_name):
        super(CatalogPopup, self).upload_image(self.UPLOAD_IMAGE, file_name)

    def save(self):
        super(CatalogPopup, self).click_element(self.SAVE_BUTTON)

    def cancel_saving(self):
        super(CatalogPopup, self).click_element(self.CANCEL_BUTTON)

    def close_popup(self):
        super(CatalogPopup, self).click_element(self.CLOSE_BUTTON)


class CatalogWidget(Component):
    # OPEN_CATALOG = '//a[@class="photo-crop_cnt"]'
    CATALOG_NAME = '//a[@class="o"]'
    NUMBER_OF_PRODUCTS = '//div[contains(@class,"photo-sc_i_cnt_data_counter")]'

    def get_catalog_name(self):
        return super(CatalogWidget, self).get_element_text(self.CATALOG_NAME)

    def get_number_of_products(self):
        return super(CatalogWidget, self).get_element_text(self.NUMBER_OF_PRODUCTS)

    def open_catalog(self):
        super(CatalogWidget, self).click_element(self.CATALOG_NAME)


class CatalogPanel(Component):
    CATALOG_NAME = '//div[@class="fs-14"]'
    NUMBER_OF_PRODUCTS = '//div[@class="mt-x lstp-t"]'

    EDIT_BUTTON = '//a[contains(@hrefattrs,"SelectionManage")]'
    REMOVE_BUTTON = '//a[contains(@hrefattrs,"SelectionRemove")]'

    def get_catalog_name(self):
        return super(CatalogPanel, self).get_element_text(self.CATALOG_NAME)

    def get_number_of_products(self):
        return super(CatalogPanel, self).get_element_text(self.NUMBER_OF_PRODUCTS)

    def edit_catalog(self):
        super(CatalogPanel, self).click_element(self.EDIT_BUTTON)

    def remove_catalog(self):
        super(CatalogPanel, self).click_element(self.REMOVE_BUTTON)


class RemoveCatalogPopup(Component):
    SAVE_PRODUCTS = '//input[@id="field_deleteAdverts_off"]'
    REMOVE_PRODUCTS = '//input[@id="field_deleteAdverts_on"]'

    REMOVE_BUTTON = '//input[@id="button_remove"]'
    CANCEL_BUTTON = '//input[@id="button_cancel"]'
    CLOSE_BUTTON = '//a[@id="nohook_modal_close"]'

    def save_products(self):
        super(RemoveCatalogPopup, self).click_element(self.SAVE_PRODUCTS)

    def remove_products(self):
        super(RemoveCatalogPopup, self).click_element(self.REMOVE_PRODUCTS)

    def submit_remove(self):
        super(RemoveCatalogPopup, self).click_element(self.REMOVE_BUTTON)

    def cancel_saving(self):
        super(RemoveCatalogPopup, self).click_element(self.CANCEL_BUTTON)

    def close_popup(self):
        super(RemoveCatalogPopup, self).click_element(self.CLOSE_BUTTON)
