# -*- coding: utf-8 -*-
from Components.component import Component


class CatalogPopup(Component):
    POPUP = '//div[@class="modal-new_center"]'
    IMAGE = '//img[@class="add-happening_poster_img" and contains(@src,"i.mycdn.me")]'
    IMAGE_SRC = '//img[@class="add-happening_poster_img" and contains(@src,"i.mycdn.me")]/@src'

    CREATE_CATALOG = '//a[@class="market-albums_new-lk"]'
    CATALOG_NAME = '//input[@id="field_name"]'
    UPLOAD_IMAGE = '//input[@class="html5-upload-link"]'

    SAVE_BUTTON = '//input[@id="hook_FormButton_button_save"]'
    CANCEL_BUTTON = '//a[@id="button_cancel"]'
    CLOSE_BUTTON = '//a[@id="nohook_modal_close"]'

    def open_popup(self):
        super(CatalogPopup, self).click_element(self.CREATE_CATALOG)

    def set_catalog_name(self, name=u'Каталог'):
        super(CatalogPopup, self).input_text_to_element(self.CATALOG_NAME, name)

    def upload_catalog_image(self, file_name):
        super(CatalogPopup, self).upload_image(self.UPLOAD_IMAGE, file_name)

    def waiting_until_image_upload(self):
        super(CatalogPopup, self).is_exist_element(self.IMAGE)

    def get_image_src(self):
        return self.driver.find_element_by_xpath(self.IMAGE).get_attribute("src")

    def save(self):
        super(CatalogPopup, self).click_element(self.SAVE_BUTTON)

    def waiting_until_close(self):
        super(CatalogPopup, self).waiting_until_invisible(self.POPUP)

    def cancel_saving(self):
        super(CatalogPopup, self).click_element(self.CANCEL_BUTTON)

    def close_popup(self):
        super(CatalogPopup, self).click_element(self.CLOSE_BUTTON)


class CatalogWidget(Component):
    WIDGET_PANEL = '//div[@data-module="AdvertSort"]'

    CATALOG_NAME = '//a[@class="o"]'
    NUMBER_OF_PRODUCTS = '//div[contains(@class,"photo-sc_i_cnt_data_counter")]'
    CATALOG_IMAGE = '//img[@class="photo-crop_img"]'

    def is_exist_catalog_widget(self):
        return super(CatalogWidget, self).is_exist_element(self.WIDGET_PANEL)

    def get_catalog_name(self):
        return super(CatalogWidget, self).get_element_text(self.CATALOG_NAME)

    def get_number_of_products(self):
        return super(CatalogWidget, self).get_element_text(self.NUMBER_OF_PRODUCTS)

    def get_image_src(self):
        return self.driver.find_element_by_xpath(self.CATALOG_IMAGE).get_attribute("src")

    def open_catalog(self):
        super(CatalogWidget, self).click_element(self.CATALOG_NAME)


class CatalogPanel(Component):
    CATALOG_NAME = '//div[@class="fs-14"]'
    NUMBER_OF_PRODUCTS = '//div[@class="mt-x lstp-t"]'
    CATALOG_IMAGE = '//div[contains(@class,"market-panel")]//img[@class="photo_img"]'

    EDIT_BUTTON = '//a[contains(@hrefattrs,"SelectionManage")]'
    REMOVE_BUTTON = '//a[contains(@hrefattrs,"SelectionRemove")]'

    def get_catalog_name(self):
        return super(CatalogPanel, self).get_element_text(self.CATALOG_NAME)

    def get_number_of_products(self):
        return super(CatalogPanel, self).get_element_text(self.NUMBER_OF_PRODUCTS)

    def get_image_src(self):
        return self.driver.find_element_by_xpath(self.CATALOG_IMAGE).get_attribute("src")

    def edit_catalog(self):
        super(CatalogPanel, self).click_element(self.EDIT_BUTTON)

    def remove_catalog(self):
        super(CatalogPanel, self).click_element(self.REMOVE_BUTTON)


class RemoveCatalogPopup(Component):
    POPUP = '//div[@class="modal-new_center"]'

    SAVE_PRODUCTS = '//input[@id="field_deleteAdverts_off"]'
    REMOVE_PRODUCTS = '//input[@id="field_deleteAdverts_on"]'

    REMOVE_BUTTON = '//input[@name="button_remove"]'
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

    def waiting_until_close(self):
        super(RemoveCatalogPopup, self).waiting_until_invisible(self.POPUP)


class CatalogCounter(Component):
    CATALOGS_COUNTER = '//span[@class="portlet_h_count"]'

    def get_number_of_catalogs(self):
        super(CatalogCounter, self).get_element_text(self.CATALOGS_COUNTER)


class ProductCounter(Component):
    PRODUCTS_COUNTER = '//span[@class="filter_count"]'

    def get_number_of_all_products(self):
        super(ProductCounter, self).get_element_text(self.PRODUCTS_COUNTER)


class CatalogStub(Component):
    STUB = '//div[@class="stub-empty  __without-icon"]'

    def is_exist_catalog_stub(self):
        return super(CatalogStub, self).is_exist_element(self.STUB)
