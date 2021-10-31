def get_file_text(file_path):
    file = open(file_path)
    text = file.read()
    file.close()
    return text
