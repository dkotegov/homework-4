# -*- coding: utf-8 -*-
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

    def open_from_catalog_panel(self):
        super(CatalogPopup, self).click_element(self.CREATE_BUTTON_ON_CATALOG_PANEL)

    def is_disabled_creation(self):
        return super(CatalogPopup, self).is_exist_element(self.DISABLED_CREATE_BUTTON_ON_CATALOG_PANEL)

    def open_from_catalog_stub(self):
        super(CatalogPopup, self).click_element(self.CREATE_BUTTON_ON_CATALOG_STUB)

    def open_from_product_panel(self):
        super(CatalogPopup, self).click_element(self.CREATE_BUTTON_ON_PRODUCT_PANEL)

    def set_name(self, name=u'Каталог'):
        super(CatalogPopup, self).input_text_to_element(self.CATALOG_NAME, name)

    def upload_catalog_image(self, file_name='image_512x512.jpg'):
        super(CatalogPopup, self).upload_image(self.UPLOAD_IMAGE, file_name)

    def waiting_image_upload(self):
        super(CatalogPopup, self).is_exist_element(self.IMAGE)

    def get_image_src(self):
        image_src = super(CatalogPopup, self).find_element(self.IMAGE).get_attribute("src")
        return Component.get_first_part_of_image_src(image_src)

    def get_error_message(self):
        return super(CatalogPopup, self).get_element_text(self.ERROR_MESSAGE)

    def save(self):
        super(CatalogPopup, self).click_element(self.SAVE_BUTTON)

    def waiting_closing(self):
        super(CatalogPopup, self).waiting_until_invisible(self.POPUP)

    def cancel_saving(self):
        super(CatalogPopup, self).click_element(self.CANCEL_BUTTON)

    def close(self):
        super(CatalogPopup, self).click_element(self.CLOSE_BUTTON)


class CreateProductPopup(Component):
    POPUP = '//div[@id="mtLayerMain"]'

    PRODUCT_NAME = '//div[@class="posting-form_itx_w"]/input'
    PRODUCT_PRICE = '//input[contains(@class,"js-advert-price")]'
    PRODUCT_ABOUT = '//div[@id="d.posting_form_text_field"]'
    PRODUCT_CATALOG = '//div[contains(@class,"pform_map") and contains(@class,"__active")]'

    CREATE_PRODUCT_BUTTON = '//a[contains(@href,"post")]'
    SUBMIT_BUTTON = '//input[contains(@id,"submit")]'

    def open(self):
        super(CreateProductPopup, self).click_element(self.CREATE_PRODUCT_BUTTON)

    def waiting_opening(self):
        super(CreateProductPopup, self).is_exist_element(self.PRODUCT_CATALOG)

    def set_name(self, name):
        super(CreateProductPopup, self).input_text_to_element(self.PRODUCT_NAME, name)

    def set_about(self, about):
        super(CreateProductPopup, self).input_text_to_element(self.PRODUCT_ABOUT, about)

    def set_price(self, price):
        super(CreateProductPopup, self).input_text_to_element(self.PRODUCT_PRICE, price)

    def submit(self):
        super(CreateProductPopup, self).click_element(self.SUBMIT_BUTTON)

    def waiting_closing(self):
        super(CreateProductPopup, self).waiting_until_invisible(self.POPUP)


class CatalogWidget(Component):
    WIDGET_PANEL = '//div[@data-module="AdvertSort"]'

    CATALOG_NAME = '//a[@class="o"]'
    NUMBER_OF_PRODUCTS = '//div[contains(@class,"photo-sc_i_cnt_data_counter")]'
    CATALOG_IMAGE = '//img[@class="photo-crop_img"]'
    CATALOG_IMAGE_STUB = '//a[@class="photo-crop_cnt"]/div[contains(@class,"stub-img")]'

    def is_exist(self):
        return super(CatalogWidget, self).is_exist_element(self.WIDGET_PANEL)

    def is_not_exist(self):
        return super(CatalogWidget, self).is_not_exist_element(self.WIDGET_PANEL)

    def get_name(self):
        return super(CatalogWidget, self).get_element_text(self.CATALOG_NAME)

    def get_number_of_products(self):
        return super(CatalogWidget, self).get_element_text(self.NUMBER_OF_PRODUCTS)

    def get_image_src(self):
        image_src = super(CatalogWidget, self).find_element(self.CATALOG_IMAGE).get_attribute("src")
        return Component.get_first_part_of_image_src(image_src)

    def open_catalog(self):
        super(CatalogWidget, self).click_element(self.CATALOG_NAME)

    def is_exist_image(self):
        return super(CatalogWidget, self).is_exist_element(self.CATALOG_IMAGE)

    def is_exist_image_stub(self):
        return super(CatalogWidget, self).is_exist_element(self.CATALOG_IMAGE_STUB)


class ProductWidget(Component):
    WIDGET_PANEL = '//div[contains(@class,"market-compact-list")]'

    PRODUCT_NAME = '//div[@class="market-card_n"]/a'
    PRODUCT_PRICE = '//div[@class="media-price_cnt"]'

    MARK_PRODUCT_AS_OUT_OF_STOCK = '//a[contains(@hrefattrs,"MARK_AS_OUT_OF_STOCK")]'
    RETURN_ON_SALE = '//a[contains(@hrefattrs,"MARK_AS_NOT_SOLD")]'
    DELETE_PRODUCT = '//a[contains(@hrefattrs,"DELETE")]'
    PIN_PRODUCT = '//a[contains(@class,"market-card_pin")]'

    PIN_TIP_BLOCK = '//div[@id="hook_Block_TipBlock"]/div[contains(@class, "__active")]'
    PIN_TEXT = u'//div[text()="Товар закреплён"]'
    UNPIN_TEXT = u'//div[text()="Товар откреплён"]'

    def is_exist(self):
        return super(ProductWidget, self).is_exist_element(self.WIDGET_PANEL)

    def is_not_exist(self):
        return super(ProductWidget, self).is_not_exist_element(self.WIDGET_PANEL)

    def get_name(self):
        return super(ProductWidget, self).get_element_text(self.PRODUCT_NAME)

    def get_price(self):
        product_price_str = super(ProductWidget, self).get_element_text(self.PRODUCT_PRICE)
        return Component.get_number_from_string(product_price_str)

    def get_price_text(self):
        return super(ProductWidget, self).get_element_text(self.PRODUCT_PRICE)

    def make_actions_visible(self):
        self.driver.execute_script(
            'document.getElementsByClassName("market-card_popup")[0].style = "visibility: visible; opacity: 1;";'
        )

    def mark_as_out_of_stock(self):
        self.make_actions_visible()
        super(ProductWidget, self).waiting_until_visible(self.MARK_PRODUCT_AS_OUT_OF_STOCK)
        super(ProductWidget, self).click_element(self.MARK_PRODUCT_AS_OUT_OF_STOCK)

    def return_on_sale(self):
        self.make_actions_visible()
        super(ProductWidget, self).waiting_until_visible(self.RETURN_ON_SALE)
        super(ProductWidget, self).click_element(self.RETURN_ON_SALE)

    def remove(self):
        self.make_actions_visible()
        super(ProductWidget, self).waiting_until_visible(self.DELETE_PRODUCT)
        super(ProductWidget, self).click_element(self.DELETE_PRODUCT)

    def make_pin_button_visible(self):
        self.driver.execute_script(
            'document.getElementsByClassName("market-card_pin")[0].style = "visibility: visible; opacity: 1;";'
        )

    def pin(self):
        self.make_pin_button_visible()
        super(ProductWidget, self).waiting_until_visible(self.PIN_PRODUCT)
        super(ProductWidget, self).click_element(self.PIN_PRODUCT)

    def unpin(self):
        super(ProductWidget, self).click_element(self.PIN_PRODUCT)

    def waiting_pin(self):
        super(ProductWidget, self).is_exist_element(self.PIN_TEXT)
        super(ProductWidget, self).waiting_until_invisible(self.PIN_TIP_BLOCK)

    def waiting_unpin(self):
        super(ProductWidget, self).is_exist_element(self.UNPIN_TEXT)
        super(ProductWidget, self).waiting_until_invisible(self.PIN_TIP_BLOCK)


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

    def get_name(self):
        return super(CatalogPanel, self).get_element_text(self.CATALOG_NAME)

    def get_number_of_products(self):
        number_of_products_str = super(CatalogPanel, self).get_element_text(self.NUMBER_OF_PRODUCTS)
        return Component.get_number_from_string(number_of_products_str)

    def get_image_src(self):
        image_src = super(CatalogPanel, self).find_element(self.CATALOG_IMAGE).get_attribute("src")
        return Component.get_first_part_of_image_src(image_src)

    def edit(self):
        super(CatalogPanel, self).click_element(self.EDIT_BUTTON)

    def remove(self):
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

    def submit_removing(self):
        super(RemoveCatalogPopup, self).click_element(self.REMOVE_BUTTON)

    def cancel_removing(self):
        super(RemoveCatalogPopup, self).click_element(self.CANCEL_BUTTON)

    def close(self):
        super(RemoveCatalogPopup, self).click_element(self.CLOSE_BUTTON)

    def waiting_closing(self):
        super(RemoveCatalogPopup, self).waiting_until_invisible(self.POPUP)


class SubmitProductActionPopup(Component):
    POPUP = '//div[@class="modal-new_center"]'

    REMOVE_BUTTON = '//input[@id="hook_FormButton_save"]'
    CANCEL_BUTTON = '//a[@id="cancel"]'
    CLOSE_BUTTON = '//a[@id="nohook_modal_close"]'

    def submit(self):
        super(SubmitProductActionPopup, self).click_element(self.REMOVE_BUTTON)

    def cancel(self):
        super(SubmitProductActionPopup, self).click_element(self.CANCEL_BUTTON)

    def close(self):
        super(SubmitProductActionPopup, self).click_element(self.CLOSE_BUTTON)

    def waiting_closing(self):
        super(SubmitProductActionPopup, self).waiting_until_invisible(self.POPUP)


class CatalogCounter(Component):
    CATALOGS_COUNTER = '//span[@class="portlet_h_count"]'

    def is_not_exist(self):
        return super(CatalogCounter, self).is_not_exist_element(self.CATALOGS_COUNTER)

    def get_number_of_catalogs(self):
        number_of_catalogs_str = super(CatalogCounter, self).get_element_text(self.CATALOGS_COUNTER)
        return int(number_of_catalogs_str)


class ProductCounter(Component):
    PRODUCTS_COUNTER = '//span[@class="filter_count"]'

    def is_not_exist(self):
        return super(ProductCounter, self).is_not_exist_element(self.PRODUCTS_COUNTER)

    def get_number_of_all_products(self):
        number_of_products_str = super(ProductCounter, self).get_element_text(self.PRODUCTS_COUNTER)
        return int(number_of_products_str)


class CatalogStub(Component):
    STUB = '//div[@class="stub-empty  __without-icon"]'
    CREATE_LATER = u'//a[text()="Позже"]'

    def is_exist(self):
        return super(CatalogStub, self).is_exist_element(self.STUB)

    def is_not_exist(self):
        return super(CatalogStub, self).is_not_exist_element(self.STUB)

    def create_catalog_later(self):
        return super(CatalogStub, self).click_element(self.CREATE_LATER)


class ProductStub(Component):
    STUB = '//div[@class="stub-empty __adverts "]'

    def is_exist(self):
        return super(ProductStub, self).is_exist_element(self.STUB)

    def is_not_exist(self):
        return super(ProductStub, self).is_not_exist_element(self.STUB)
