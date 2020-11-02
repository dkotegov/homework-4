import os
import requests
import urllib.parse


class DatabaseFiller():
    PATH = 'http://skydelivery.site/api/v1/'
    REST_PHOTO_PATH = 'data/test_rest_photo.jpg'
    TAG_PHOTO_PATH = 'data/YHiqP4sJEKjLdrknQzeYq5.svg'
    PROD_PHOTO_PATH = 'data/test_prod_photo.jpg'
    ADDRESS = 'Россия, Москва, Старокирочный переулок, 16/2с1'
    COOKIE_NAME = 'SkyDelivery'
    LOGIN_PATH = 'signin/'
    PRODUCTS_PATH = 'product/'
    PRODUCT_PATH = 'products/{}'
    RESTAURANT_PATH = 'restaurants/{}'
    RESTAURANT_TAG_PATH = 'restaurants/{}/tag/{}'
    TAG_PATH = 'rest_tags'
    LOGIN = os.environ['ADMIN_LOGIN']
    PASSWORD = os.environ['ADMIN_PASSWORD']
    rests_id = []

    def admin_auth(self):
        self.session = requests.Session()
        response = self.session.post(urllib.parse.urljoin(self.PATH, self.LOGIN_PATH),
                                     json={
                                         'phone': self.LOGIN,
                                         'password': self.PASSWORD
                                     })

        if response.status_code != requests.codes['ok']:
            raise RuntimeError

        self.csrf_token = response.headers.get('X-Csrf-Token')

    def create_restaurant(self, title, address, radius):
        with open(self.REST_PHOTO_PATH, 'rb') as photo:
            response = self.session.post(urllib.parse.urljoin(self.PATH, self.RESTAURANT_PATH.format('')),
                                         headers={'X-Csrf-Token': self.csrf_token},
                                         data={
                                             'Name': title,
                                             'Description': "This is {}".format(title),
                                             'Address': address,
                                             'Radius': radius
                                         },
                                         files={'image': photo}
                                         )

        if response.status_code != requests.codes['ok']:
            raise RuntimeError

    def get_restaurant_id_by_name(self, rest_name):
        response = self.session.get(urllib.parse.urljoin(self.PATH, self.RESTAURANT_PATH.format('')),
                                    params={'count': 1000, 'page': 1}
                                    )

        if response.status_code != requests.codes['ok']:
            raise RuntimeError

        json_resp = response.json()
        id = 0
        for rest in json_resp['restaurants']:
            if rest['name'] == rest_name:
                id = rest['id']
                break

        return id

    def add_tag_to_restaurant(self, tag, restaurant):
        restaurant_id = self.get_restaurant_id_by_name(restaurant)
        tag_id = self.get_tag_by_name(tag)

        response = self.session.post(
            urllib.parse.urljoin(self.PATH, self.RESTAURANT_TAG_PATH.format(restaurant_id, tag_id)),
            headers={'X-Csrf-Token': self.csrf_token},
        )

        if response.status_code != requests.codes['ok']:
            raise RuntimeError

    def create_tag(self, tagname):
        with open(self.TAG_PHOTO_PATH, 'rb') as photo:
            response = self.session.post(
                urllib.parse.urljoin(self.PATH, self.TAG_PATH),
                headers={'X-Csrf-Token': self.csrf_token},
                data={
                    'Name': tagname,

                },
                files={'image': photo}
            )

        if response.status_code != requests.codes['ok']:
            raise RuntimeError

    def get_tag_by_name(self, tagname):
        response = self.session.get(urllib.parse.urljoin(self.PATH, self.TAG_PATH))

        if response.status_code != requests.codes['ok']:
            raise RuntimeError

        json_resp = response.json()
        id = 0
        for rest in json_resp['rest_tags']:
            if rest['name'] == tagname:
                id = rest['id']
                break

        return id

    def create_test_restaurants(self, count):
        for i in range(count):
            self.create_restaurant('Test rest №{}'.format(i), self.ADDRESS, 5)

        response = self.session.get(urllib.parse.urljoin(self.PATH, self.RESTAURANT_PATH.format('')),
                                    params={'count': 1000, 'page': 1}
                                    )

        if response.status_code != requests.codes['ok']:
            raise RuntimeError

        json_resp = response.json()
        for rest in json_resp['restaurants']:
            if 'Test rest' in rest['name']:
                self.rests_id.append(rest['id'])

    def create_product(self, rest_id, title, price):
        with open(self.PROD_PHOTO_PATH, 'rb') as photo:
            rest_path = urllib.parse.urljoin(self.PATH, self.RESTAURANT_PATH.format(rest_id)) + '/'
            response = self.session.post(urllib.parse.urljoin(rest_path, self.PRODUCTS_PATH),
                                         headers={'X-Csrf-Token': self.csrf_token},
                                         data={
                                             'Name': title,
                                             'Price': price,
                                         },
                                         files={'image': photo}
                                         )

        if response.status_code != requests.codes['ok']:
            raise RuntimeError

    def create_products_for_rests(self, count, price):
        for id in self.rests_id:
            for i in range(count):
                self.create_product(id, 'Test prod №{}'.format(i), price)

    def delete_product(self, id):
        prod_path = urllib.parse.urljoin(self.PATH, self.PRODUCT_PATH.format(id)) + '/'
        response = self.session.delete(urllib.parse.urljoin(prod_path, "delete"),
                                       headers={'X-Csrf-Token': self.csrf_token}
                                       )

        if response.status_code != requests.codes['ok']:
            raise RuntimeError

    def delete_rest_products(self, rest_id):
        rest_path = urllib.parse.urljoin(self.PATH, self.RESTAURANT_PATH.format(rest_id)) + '/'
        response = self.session.get(urllib.parse.urljoin(rest_path, self.PRODUCTS_PATH),
                                    params={'count': 1000, 'page': 1}
                                    )

        if response.status_code != requests.codes['ok']:
            raise RuntimeError

        json_resp = response.json()
        for prod in json_resp['products']:
            self.delete_product(prod['id'])

    def delete_restaurant(self, id):
        response = self.session.delete(urllib.parse.urljoin(self.PATH, self.RESTAURANT_PATH.format(id)),
                                       headers={'X-Csrf-Token': self.csrf_token}
                                       )

        if response.status_code != requests.codes['ok']:
            raise RuntimeError

    def delete_restaurant_by_name(self, title):
        id = self.get_restaurant_id_by_name(title)

        if id == 0:
            raise RuntimeError

        self.delete_rest_products(id)
        self.delete_restaurant(id)

    def delete_all_rests(self):
        for id in self.rests_id:
            self.delete_rest_products(id)
            self.delete_restaurant(id)

        self.rests_id = []


# Tests of functionality helpers
if __name__ == '__main__':
    filler = DatabaseFiller()

    filler.admin_auth()
    filler.delete_restaurant_by_name("Test restaurant")
    # filler.create_test_restaurants(1)
    # filler.create_products_for_rests(1, 100)
    # filler.delete_all_rests()
