from consts import *

def get_state(url):
    if url in STATES:
        return STATES[url]
    return None
