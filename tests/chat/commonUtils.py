

def get_last_msg_from_chat_history(html):
    return html.split('<div class="message_data chat_align-left chat_my_message ">')[-1].split('</div>')[0]


def get_last_msg_date_from_chat_history(html):
    return html.split('<span class="message_data_time">')[-1].split('</span>')[0]

