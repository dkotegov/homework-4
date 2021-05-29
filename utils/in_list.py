def in_list(expect, list):
    for item in list:
        if expect == item.text:
            return True
    return False