from config import config

def log_d(text):
    if not config.get("debug", False):
        return

    result = config.get("executor.browser.name", "CHROME") + ": " + text
    print(result)
