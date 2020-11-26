

def get_names_from_sub_item_html(html):
    names = []
    item_html_list = html.split('class="follow_login">')[1:]
    for i in item_html_list:
        names.append(i.split('</div>')[0])
    return names
