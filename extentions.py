from datetime import datetime

def now_time():
    hour = datetime.now().hour
    minutes = datetime.now().minute
    seconds = datetime.now().second
    time = str(hour) + ':' + str(minutes) + ':' + str(seconds)
    return time

