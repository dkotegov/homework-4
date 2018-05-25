from tests.Components.Component import Component


class ListOfPhotos(Component):
    PHOTOS_UL = '//ul[@class="ugrid_cnt"]/li[@class="ugrid_i"]'

    def check_photo_in_album_by_id(self, new_photo_id):
        links = self.driver.find_elements_by_xpath(self.PHOTOS_UL)
        for link in links:
            current_photo_id = link.find_element_by_tag_name('img').get_attribute('id')
            result_id = current_photo_id.split('_')[1]
            if result_id == new_photo_id:
                return True
        return False
