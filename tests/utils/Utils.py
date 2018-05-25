import hashlib
import os
import urllib


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def md5(image_name):
        hash_md5 = hashlib.md5()
        with open(image_name, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    @staticmethod
    def download_image(src, image_name):
        urllib.urlretrieve(src, image_name)

    @staticmethod
    def delete_image(src):
        os.remove(src)
