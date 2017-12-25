from collections import defaultdict
from itertools import repeat


def constant_factory(value):
    return repeat(value).__next__


def default_dict_factory(*args, default=None, **kwargs):
    return defaultdict(constant_factory(default), *args, **kwargs)


class PassValueDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getitem__(self, item):
        try:
            return super().__getitem__(item)
        except KeyError:
            return self.__missing__(item)

    def __missing__(self, key):
        return key
