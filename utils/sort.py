import re


def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)


def fill_amount_list_and_sort_last_list(products, reverse):
    list_not_sorted = []
    list_sorted = []
    for item in products:
        list_not_sorted.append(int(item.text[0:-1].replace(" ", "")))
        list_sorted.append(int(item.text[0:-1].replace(" ", "")))
    list_sorted = sorted(list_sorted, reverse=reverse)
    return list_not_sorted, list_sorted


def fill_name_list_and_sort_last_list(products):
    list_not_sorted = []
    list_sorted = []
    for item in products:
        list_not_sorted.append(item.text)
        list_sorted.append(item.text)
    list_sorted = natural_sort(list_sorted)
    return list_not_sorted, list_sorted
