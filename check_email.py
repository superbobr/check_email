def check_email(string):
    flag = True
    if ' ' in string:
        flag = False
    if '@' not in string:
        flag = False
    else:
        index = string.find('@')
        if string[index + 1] == '.':
            flag = False
        result = string.find('.', index + 1)
        if result == -1:
            flag = False
    return flag