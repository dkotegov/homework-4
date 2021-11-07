import re


def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)


def fill_amount_list_and_sort_last_list(products, reverse):
    return list(map(lambda x: int(x.text[0:-1].replace(" ", "")), products)), \
           sorted(map(lambda x: int(x.text[0:-1].replace(" ", "")), products), reverse=reverse)


def fill_name_list_and_sort_last_list(products):
    return list(map(lambda x: x.text, products)), natural_sort(list(map(lambda x: x.text, products)))
