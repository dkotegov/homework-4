# -*- coding: utf-8 -*-
import re

from Components.component import Component


class CatalogPopup(Component):
    POPUP = '//div[@class="modal-new_center"]'
    IMAGE = '//img[contains(@class,"add-happening_poster_img") and contains(@src,"i.mycdn.me")]'

    CATALOG_NAME = '//input[@id="field_name"]'
    ERROR_MESSAGE = '//div[contains(@class,"form_i__error")]/span[@class="input-e"]'
    UPLOAD_IMAGE = '//input[@class="html5-upload-link"]'

    CREATE_BUTTON_ON_CATALOG_PANEL = '//a[@class="market-albums_new-lk"]'
    DISABLED_CREATE_BUTTON_ON_CATALOG_PANEL = '//span[@class="market-albums_new-lk __disabled"]'
    CREATE_BUTTON_ON_CATALOG_STUB = '//a[@class="button-pro"]'
    CREATE_BUTTON_ON_PRODUCT_PANEL = '//div[@class="portlet_h_inf"]/a'

    SAVE_BUTTON = '//input[@id="hook_FormButton_button_save"]'
    CANCEL_BUTTON = '//a[@id="button_cancel"]'
    CLOSE_BUTTON = '//a[@id="nohook_modal_close"]'

    def open_popup_from_catalog_panel(self):
        super(CatalogPopup, self).click_element(self.CREATE_BUTTON_ON_CATALOG_PANEL)

    def is_disabled_creation(self):
        return super(CatalogPopup, self).is_exist_element(self.DISABLED_CREATE_BUTTON_ON_CATALOG_PANEL)

    def open_popup_from_catalog_stub(self):
        super(CatalogPopup, self).click_element(self.CREATE_BUTTON_ON_CATALOG_STUB)

    def open_popup_from_product_panel(self):
        super(CatalogPopup, self).click_element(self.CREATE_BUTTON_ON_PRODUCT_PANEL)

    def set_catalog_name(self, name=u'Каталог'):
        super(CatalogPopup, self).input_text_to_element(self.CATALOG_NAME, name)

    def upload_catalog_image(self, file_name='image_512x512.jpg'):
        super(CatalogPopup, self).upload_image(self.UPLOAD_IMAGE, file_name)

    def waiting_until_image_upload(self):
        super(CatalogPopup, self).is_exist_element(self.IMAGE)

    def get_image_src(self):
        return super(CatalogPopup, self).find_element(self.IMAGE).get_attribute("src")

    def get_error_message(self):
        return super(CatalogPopup, self).get_element_text(self.ERROR_MESSAGE)

    def save(self):
        super(CatalogPopup, self).click_element(self.SAVE_BUTTON)

    def waiting_until_close(self):
        super(CatalogPopup, self).waiting_until_invisible(self.POPUP)

    def cancel_saving(self):
        super(CatalogPopup, self).click_element(self.CANCEL_BUTTON)

    def close_popup(self):
        super(CatalogPopup, self).click_element(self.CLOSE_BUTTON)


class ProductPopup(Component):
    POPUP = '//div[@id="mtLayerMain"]'

    PRODUCT_NAME = '//div[@class="posting-form_itx_w"]/input'
    PRODUCT_PRICE = '//input[contains(@class,"js-advert-price")]'
    PRODUCT_ABOUT = '//div[@id="d.posting_form_text_field"]'
    PRODUCT_CATALOG = '//div[contains(@class,"pform_map") and contains(@class,"__active")]'

    CREATE_PRODUCT_BUTTON = '//a[contains(@href,"post")]'
    SUBMIT_BUTTON = '//input[contains(@id,"submit")]'

    def open_popup(self):
        super(ProductPopup, self).click_element(self.CREATE_PRODUCT_BUTTON)

    def waiting_opening(self):
        super(ProductPopup, self).is_exist_element(self.PRODUCT_CATALOG)

    def set_product_name(self, name=u'Товар'):
        super(ProductPopup, self).input_text_to_element(self.PRODUCT_NAME, name)

    def set_product_about(self, about=u'Описание товара'):
        super(ProductPopup, self).input_text_to_element(self.PRODUCT_ABOUT, about)

    def set_product_price(self, price='100'):
        super(ProductPopup, self).input_text_to_element(self.PRODUCT_PRICE, price)

    def submit(self):
        super(ProductPopup, self).click_element(self.SUBMIT_BUTTON)

    def waiting_until_close(self):
        super(ProductPopup, self).waiting_until_invisible(self.POPUP)


class CatalogWidget(Component):
    WIDGET_PANEL = '//div[@data-module="AdvertSort"]'

    CATALOG_NAME = '//a[@class="o"]'
    NUMBER_OF_PRODUCTS = '//div[contains(@class,"photo-sc_i_cnt_data_counter")]'
    CATALOG_IMAGE = '//img[@class="photo-crop_img"]'
    CATALOG_IMAGE_STUB = '//a[@class="photo-crop_cnt"]/div[contains(@class,"stub-img")]'

    def is_exist_catalog_widget(self):
        return super(CatalogWidget, self).is_exist_element(self.WIDGET_PANEL)

    def is_not_exist_catalog_widget(self):
        return super(CatalogWidget, self).is_not_exist_element(self.WIDGET_PANEL)

    def get_catalog_name(self):
        return super(CatalogWidget, self).get_element_text(self.CATALOG_NAME)

    def get_number_of_products(self):
        return super(CatalogWidget, self).get_element_text(self.NUMBER_OF_PRODUCTS)

    def get_image_src(self):
        return super(CatalogWidget, self).find_element(self.CATALOG_IMAGE).get_attribute("src")

    def open_catalog(self):
        super(CatalogWidget, self).click_element(self.CATALOG_NAME)

    def is_exist_image(self):
        return super(CatalogWidget, self).is_exist_element(self.CATALOG_IMAGE)

    def is_exist_image_stub(self):
        return super(CatalogWidget, self).is_exist_element(self.CATALOG_IMAGE_STUB)


class ProductWidget(Component):
    WIDGET_PANEL = '//div[contains(@class,"market-compact-list")]'

    PRODUCT_NAME = '//div[@class="market-card_n"]/a'

    MARK_PRODUCT_AS_OUT_OF_STOCK = '//a[contains(@hrefattrs,"MARK_AS_OUT_OF_STOCK")]'
    MARK_PRODUCT_AS_NOT_SOLD = '//a[contains(@hrefattrs,"MARK_AS_NOT_SOLD")]'
    DELETE_PRODUCT = '//a[contains(@hrefattrs,"DELETE")]'
    PIN_PRODUCT = '//a[contains(@class,"market-card_pin")]'

    def is_exist_catalog_widget(self):
        return super(ProductWidget, self).is_exist_element(self.WIDGET_PANEL)

    def is_not_exist_catalog_widget(self):
        return super(ProductWidget, self).is_not_exist_element(self.WIDGET_PANEL)

    def get_product_name(self):
        return super(ProductWidget, self).get_element_text(self.PRODUCT_NAME)

    def mark_product_as_out_of_stock(self):
        super(ProductWidget, self).click_element(self.MARK_PRODUCT_AS_OUT_OF_STOCK)

    def delete_product(self):
        super(ProductWidget, self).click_element(self.DELETE_PRODUCT)

    def pin_product(self):
        super(ProductWidget, self).click_element(self.PIN_PRODUCT)

    def unpin_product(self):
        super(ProductWidget, self).click_element(self.PIN_PRODUCT)


class CatalogPanel(Component):
    CATALOG_PANEL = '//div[contains(@class,"market-panel")]'

    CATALOG_NAME = '//div[@class="caption"]/div[contains(@class,"fs-14")]'
    NUMBER_OF_PRODUCTS = '//div[@class="caption"]/div[contains(@class,"mt-x")]'
    CATALOG_IMAGE = '//div[contains(@class,"market-panel")]//img[@class="photo_img"]'
    CATALOG_IMAGE_STUB = '//div[@class="photo"]/div[contains(@class,"stub-img")]'

    EDIT_BUTTON = '//a[contains(@hrefattrs,"SelectionManage")]'
    REMOVE_BUTTON = '//a[contains(@hrefattrs,"SelectionRemove")]'

    def waiting_opening(self):
        return super(CatalogPanel, self).is_exist_element(self.CATALOG_PANEL)

    def get_catalog_name(self):
        return super(CatalogPanel, self).get_element_text(self.CATALOG_NAME)

    def get_number_of_products(self):
        number_of_products_str = super(CatalogPanel, self).get_element_text(self.NUMBER_OF_PRODUCTS)
        return int(re.search(r'\d+', number_of_products_str).group())

    def get_image_src(self):
        return super(CatalogPanel, self).find_element(self.CATALOG_IMAGE).get_attribute("src")

    def edit_catalog(self):
        super(CatalogPanel, self).click_element(self.EDIT_BUTTON)

    def remove_catalog(self):
        super(CatalogPanel, self).click_element(self.REMOVE_BUTTON)

    def is_exist_image(self):
        return super(CatalogPanel, self).is_exist_element(self.CATALOG_IMAGE)

    def is_exist_image_stub(self):
        return super(CatalogPanel, self).is_exist_element(self.CATALOG_IMAGE_STUB)


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
        return super(CatalogCounter, self).get_element_text(self.CATALOGS_COUNTER)


class ProductCounter(Component):
    PRODUCTS_COUNTER = '//span[@class="filter_count"]'

    def get_number_of_all_products(self):
        return super(ProductCounter, self).get_element_text(self.PRODUCTS_COUNTER)


class CatalogStub(Component):
    STUB = '//div[@class="stub-empty  __without-icon"]'
    CREATE_LATER = u'//a[text()="Позже"]'

    def is_exist_catalog_stub(self):
        return super(CatalogStub, self).is_exist_element(self.STUB)

    def is_not_exist_catalog_stub(self):
        return super(CatalogStub, self).is_not_exist_element(self.STUB)

    def create_catalog_later(self):
        return super(CatalogStub, self).click_element(self.CREATE_LATER)


class ProductStub(Component):
    STUB = '//div[@class="stub-empty __adverts "]'

    def is_exist_product_stub(self):
        return super(ProductStub, self).is_exist_element(self.STUB)

    def is_not_exist_product_stub(self):
        return super(ProductStub, self).is_not_exist_element(self.STUB)
