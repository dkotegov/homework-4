import yaml

from hamcrest import *


class Config:
    def __init__(self, conf_dict):
        self.cfg = conf_dict

    def get(self, key, default=None):
        paths = key.split(".")

        obj = self.cfg
        for key in paths:
            if key not in obj:
                assert_that(default, not_none(), "cannot find " + str(key))
                return default
            obj = obj[key]

        return obj

    def __getitem__(self, item):
        return self.get(item, default=None)


config = None


def parse_config(filename):
    global config

    with open(filename) as stream:
        try:
            config_file = yaml.load(stream)
            assert_that(config_file, not_none(), "cannot parse config")

            config = Config(config_file)
        except yaml.YAMLError as exc:
            print(exc)


parse_config("./config/okdev.yaml")
