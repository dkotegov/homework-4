def not_in(expect, list):
    for item in list:
        if expect == item.text:
            return False
    return True