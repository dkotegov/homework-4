from config import config


def log_d(text):
    result = config.get("browser.name", "unknown") + ": " + text
    print(result)